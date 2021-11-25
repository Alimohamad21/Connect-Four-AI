import sys
from random import randint

import pygame

from constants import *
from stateFunctions import *
from scoreFunctions import *

boardState = initializeBoard()
isUserTurn = True


def main():
    global SCREEN, CLOCK, boardState, isUserTurn
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    drawBoard()
    selectedColumn = 0
    while True:
        if isFull(boardState):
            print('GAME OVER')
        elif isUserTurn:
            print('YOUR TURN')
        else:
            print('AI TURN')
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
            column = randint(0, 6)
            while isColumnFull(boardState, column):
                column = randint(0, 6)
            boardState = insertAtColumn(boardState, column, 'R')
            drawBoard()
            isUserTurn = True
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and isUserTurn:
                if not isColumnFull(boardState, selectedColumn):
                    boardState = insertAtColumn(boardState, selectedColumn, 'Y')
                    isUserTurn = False
                    print(f"YOUR SCORE: {calculateScore(boardState,'Y')}")
                    print(f"AI SCORE: {calculateScore(boardState,'R')}")
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
