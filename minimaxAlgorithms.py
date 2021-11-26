import sys

from heuristicFunctions import eval
from scoreFunctions import calculateScore
from stateFunctions import getChildren, isFull
from time import time


def scoreDiff(boardState):
    return calculateScore(boardState, 'R') - calculateScore(boardState, 'Y')


def evalDiff(boardState):
    return eval(boardState)


def miniMax_pruning(boardState, alpha, beta, k, color):
    if not k:
        return [boardState, evalDiff(boardState), 1]
    elif isFull(boardState):
        return [boardState, 1000 * scoreDiff(boardState), 1]
    maxChild = boardState
    callNumNodes = 1
    if color == 'R':
        max_eval = -sys.maxsize
        for child in getChildren(boardState,color):
            myArr = miniMax_pruning(child, alpha, beta, k - 1, 'Y')
            child_eval = myArr[1]
            callNumNodes += myArr[2]
            if child_eval > max_eval:
                maxChild = child
                max_eval = child_eval

            if max_eval >= beta:
                break
            if max_eval >= alpha:
                alpha = max_eval
    else:
        max_eval = sys.maxsize
        for child in getChildren(boardState, color):
            myArr = miniMax_pruning(child, alpha, beta, k - 1, 'R')
            child_eval = myArr[1]
            callNumNodes += myArr[2]
            if child_eval < max_eval:
                maxChild = child
                max_eval = child_eval
            if max_eval <= alpha:
                break
            if max_eval < beta:
                beta = max_eval

    return [maxChild, max_eval, callNumNodes]


def miniMax(boardState, k, color):
    if isFull(boardState):
        return [boardState, 1000 * scoreDiff(boardState), 1]
    elif not k:
        return [boardState, evalDiff(boardState), 1]


    maxChild = boardState
    callNumNodes = 1
    if color == 'R':
        max_eval = -sys.maxsize
        for child in getChildren(boardState, color):
            myArr = miniMax(child, k - 1, 'Y')
            child_eval = myArr[1]
            callNumNodes += myArr[2]
            if child_eval > max_eval:
                maxChild = child
                max_eval = child_eval


    else:
        max_eval = sys.maxsize
        for child in getChildren(boardState, color):
            myArr = miniMax(child, k - 1, 'R')
            child_eval = myArr[1]
            callNumNodes += myArr[2]
            if child_eval < max_eval:
                maxChild = child
                max_eval = child_eval

    return [maxChild, max_eval, callNumNodes]


def decide(boardState):
    start = time()
    myArr = miniMax(boardState, 3, 'R')
    end = time()
    return [myArr[0], myArr[2], end - start]


def decide_pruning(boardState):
    start = time()
    myArr = miniMax_pruning(boardState, -sys.maxsize, sys.maxsize, 3, 'R')
    end = time()
    return [myArr[0], myArr[2], end - start]
