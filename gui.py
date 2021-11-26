import sys
from random import randint

import stateFunctions
from minimaxAlgorithms import decide
import pygame

from constants import *
from scoreFunctions import *
from stateFunctions import *

boardState = initializeBoard()
isUserTurn = False
redScore = 0
yellowScore = 0


def main():
    global SCREEN, CLOCK, boardState, isUserTurn, redScore, yellowScore, k, prune
    k = int(input('ENTER K: '))
    prune = bool(int(input('ENTER prune 0 or 1: ')))
    stateFunctions.printBoard(POTENTIAL_SCORES)
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    drawBoard()
    selectedColumn = 0
    print(pygame.font.get_fonts())
    while True:
        if isFull(boardState):
            if yellowScore > redScore:
                message = 'YOU WIN !'
            elif yellowScore < redScore:
                message = 'AI WINS :('
            else:
                message = 'DRAW'
        elif isUserTurn:
            message = 'YOUR TURN'
        else:
            message = 'AI TURN'
        displayGameState(message)
        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        # print(f'x:{x} y:{y}')
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
         #   column = randint(0, 6)
         #   while isColumnFull(boardState, column):
         #       column = randint(0, 6)
         #   boardState = insertAtColumn(boardState, column, 'R')
            myArr = decide(boardState, k, prune)
            boardState = myArr[0]
            #print(myArr[1], myArr[2])
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
    message = f'YOUR SCORE: {yellowScore}     {text}    AI SCORE:{redScore}'
    pygame.draw.rect(SCREEN, GREY,
                     (0, 0, WINDOW_WIDTH, 100))
    font = pygame.font.SysFont('Arial', 24)
    SCREEN.blit(font.render(message, True, RED), (50, 30))


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
