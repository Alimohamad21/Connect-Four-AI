import sys

from heuristicFunctions import eval
from scoreFunctions import calculateScore
from stateFunctions import getChildren, isFull


def scoreDiff(boardState):
    return calculateScore(boardState, 'R') - calculateScore(boardState, 'Y')


def evalDiff(boardState):
    return eval(boardState, 'R') - eval(boardState, 'Y')


def miniMax(boardState, alpha, beta, k, color):
    if not k:
        return evalDiff(boardState)
    elif isFull(boardState):
        return scoreDiff(boardState)
    if color == 'R':
        max_eval = -sys.maxsize
        for child in getChildren(boardState):
            child_eval = miniMax(child, alpha, beta, k - 1, 'Y')
            max_eval = max(child_eval, max_eval)
            alpha = max(max_eval, alpha)
            if alpha >= beta:
                break
    else:
        max_eval = sys.maxsize
        for child in getChildren(boardState):
            child_eval = miniMax(child, alpha, beta, k - 1, 'R')
            max_eval = min(max_eval, child_eval)
            beta = min(max_eval, beta)
            if beta <= alpha:
                break
    return max_eval
