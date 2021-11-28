import sys
import time

import pygame
import pygame_menu

from constants import *
from minimaxAlgorithms import decide
from scoreFunctions import *
from stateFunctions import *

isUserTurn = True
prune = True
k = 5


def main():
    global SCREEN, menu
    pygame.init()

    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    menu = pygame_menu.Menu('CONNECT FOUR', WINDOW_WIDTH, WINDOW_HEIGHT,
                            theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input('K :', default=k, onchange=setK)
    menu.add.selector('', [('Minimax with alpha-beta pruning', 1), ('Minimax without alpha-beta pruning', 2)],
                      onchange=setPruning)
    menu.add.button('Play', game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(SCREEN)


def setPruning(a, b):
    global prune
    prune = not prune


def setK(kInput):
    global k
    k = kInput


def game():
    global SCREEN, boardState, isUserTurn, redScore, yellowScore, k, prune, gameStarted, menu, gameEnded
    redScore = 0
    yellowScore = 0
    boardState = initializeBoard()
    try:
        k = int(k)
    except:
        print('Invalid k')
    print(f'K= {k}')
    print(f'PRUNING: {prune}')
    SCREEN.fill(BLACK)
    drawBoard()
    selectedColumn = 0
    gameOver = False
    while True:
        if isFull(boardState):
            if yellowScore > redScore:
                message = 'YOU WIN !'
            elif yellowScore < redScore:
                message = 'AI WINS !'
            else:
                message = 'DRAW'
            displayGameState(message)
            if gameOver:
                time.sleep(3)
                menu.mainloop(SCREEN)
            gameOver = True
            # menu.mainloop(SCREEN)
        elif isUserTurn:
            message = 'YOUR TURN'
        else:
            message = 'AI TURN'
        displayGameState(message)
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if isUserTurn:
            if y > 100:
                if x // 100 == selectedColumn:
                    if not isColumnFull(boardState, selectedColumn):
                        playableRow = getPlayableRow(boardState, selectedColumn)
                        drawFade(playableRow, selectedColumn)
                else:
                    selectedColumn = x // 100
                    drawBoard()
            else:
                drawBoard()
        else:
            myArr = decide(boardState, k, prune)
            boardState = myArr[0]
            nodesExpanded, runTime = myArr[1], myArr[2]
            print(f'MINIMAX NODES EXPANDED: {nodesExpanded}\tRUN TIME: {runTime} seconds')
            redScore = calculateScore(boardState, 'R')
            drawBoard()
            isUserTurn = True
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and isUserTurn and y > 100:
                if not isColumnFull(boardState, selectedColumn):
                    boardState = insertAtColumn(boardState, selectedColumn, 'Y')
                    isUserTurn = False
                    yellowScore = calculateScore(boardState, 'Y')
                    drawBoard()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def drawFade(playableRow, selectedColumn):
    pygame.draw.circle(SCREEN, FADED_YELLOW, (
        int(selectedColumn * SQUARE_SIZE + SQUARE_SIZE / 2),
        int(playableRow * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)),
                       RADIUS)


def displayGameState(text):
    displayedText = f'YOUR SCORE: {yellowScore}     {text}    AI SCORE:{redScore}'
    pygame.draw.rect(SCREEN, GREY,
                     (0, 0, WINDOW_WIDTH, 100))
    font = pygame.font.SysFont('Arial', 24)
    SCREEN.blit(font.render(displayedText, True, RED), (50, 30))


# inkfree for you win

def drawBoard():
    color = None
    for j in range(COLUMN_COUNT):  # drawing the rectangle of the board
        for i in range(ROW_COUNT):
            element = getElementAtIndex(boardState, i, j)
            if element == 'E':
                color = GREY
            elif element == 'Y':
                color = YELLOW
            elif element == 'R':
                color = RED
            pygame.draw.rect(SCREEN, BLUE,
                             (j * SQUARE_SIZE, i * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(SCREEN, color, (
                int(j * SQUARE_SIZE + SQUARE_SIZE / 2), int(i * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)),
                               RADIUS)  # drawing the circles inside rectangle of the board
    pygame.display.update()
