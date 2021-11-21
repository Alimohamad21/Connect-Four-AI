from stateFunctions import *


def calculateRow(boardState, color):
    score = 0
    for i in range(6):
        count = 0
        for j in range(7):
            if getElementAtIndex(boardState, i, j) == color:
                count += 1
            else:
                count = 0
            if count >= 4:
                score += 1
    return score

def downtoup_diagonal_count(boardState, color):
    connected_fours = 0
    for j in range(4):
        for i in range(5, 2, -1):

            if getElementAtIndex(boardState, i, j) == getElementAtIndex(boardState, i - 1, j - 1) == getElementAtIndex(
                    boardState, i - 2, j - 2) == getElementAtIndex(boardState, i - 3, j - 3) == color:
                connected_fours += 1

    return connected_fours


def uptodown_diagonal_count(boardState, color):
    connected_fours = 0
    for j in range(4):
        for i in range(3):
            if getElementAtIndex(boardState, i, j) == getElementAtIndex(boardState, i+1, j+1) == getElementAtIndex(boardState, i+2, j+2) == getElementAtIndex(boardState,i+3,j+3) == color:
                connected_fours += 1

    return connected_fours

def calculateColumn(boardState, color):
    score = 0
    for j in range(7):
        count = 0
        for i in range(6):
            if getElementAtIndex(boardState, i, j) == color:
                count += 1
            else:
                count = 0
            if count >= 4:
                score += 1
    return score


def calculateDiagonal(boardState, color):
    return uptodown_diagonal_count(boardState, color) + downtoup_diagonal_count(boardState, color)


def calculateScore(boardState, color):
    return calculateRow(boardState, color) + calculateColumn(boardState, color) + calculateDiagonal(boardState, color)
