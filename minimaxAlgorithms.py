import sys

from heuristicFunctions import eval
from scoreFunctions import calculateScore
from stateFunctions import getChildren, isFull
from time import time
from Node import*


def scoreDiff(boardState):
    return calculateScore(boardState, 'R') - calculateScore(boardState, 'Y')



def miniMax_pruning(boardState, alpha, beta, k, color, root):
    if isFull(boardState):
        root.score = scoreDiff(boardState)
        return [boardState, root.score, 1]
    elif not k:
        root.score = eval(boardState)
        return [boardState, root.score, 1]
    maxChild = None
    callNumNodes = 1
    if color == 'R':
        max_eval = -sys.maxsize
        for child in getChildren(boardState,color):
            childNode = Node(root, -sys.maxsize, not root.max_or_min)
            root.addChild(childNode)
            myArr = miniMax_pruning(child, alpha, beta, k - 1, 'Y', childNode)
            child_eval = myArr[1]
            callNumNodes += myArr[2]
            if child_eval > max_eval:
                maxChild = child
                max_eval = child_eval

            if max_eval >= beta:
                root.score = str(max_eval)+" pruned"
                break
            if max_eval >= alpha:
                alpha = max_eval
        root.score = max_eval
    else:
        max_eval = sys.maxsize
        for child in getChildren(boardState, color):
            childNode = Node(root, -sys.maxsize, not root.max_or_min)
            root.addChild(childNode)
            myArr = miniMax_pruning(child, alpha, beta, k - 1, 'R', childNode)
            child_eval = myArr[1]
            callNumNodes += myArr[2]
            if child_eval < max_eval:
                maxChild = child
                max_eval = child_eval
            if max_eval <= alpha:
                root.score = str(max_eval)+" pruned"
                break
            if max_eval < beta:
                beta = max_eval
        root.score = max_eval


    return [maxChild, max_eval, callNumNodes]


def miniMax(boardState, k, color, root):
    if isFull(boardState):
        root.score = scoreDiff(boardState)
        return [boardState, root.score, 1]
    elif not k:
        root.score = eval(boardState)
        return [boardState, root.score, 1]


    maxChild = None
    callNumNodes = 1
    if color == 'R':
        max_eval = -sys.maxsize
        for child in getChildren(boardState, color):
            childNode = Node(root, -sys.maxsize, not root.max_or_min)
            root.addChild(childNode)
            myArr = miniMax(child, k - 1, 'Y', childNode)
            child_eval = myArr[1]
            callNumNodes += myArr[2]

            if child_eval > max_eval:
                maxChild = child
                max_eval = child_eval
        root.score = max_eval

    else:
        max_eval = sys.maxsize
        for child in getChildren(boardState, color):
            childNode = Node(root, sys.maxsize, not root.max_or_min)
            root.addChild(childNode)
            myArr = miniMax(child, k - 1, 'R', childNode)
            child_eval = myArr[1]
            callNumNodes += myArr[2]
            if child_eval < max_eval:
                maxChild = child
                max_eval = child_eval

        root.score = max_eval

    return [maxChild, max_eval, callNumNodes]


def decide(boardState, k=3, prune=True):
    root = Node(None, -sys.maxsize, True)
    if prune:
        start = time()
        myArr = miniMax_pruning(boardState, -sys.maxsize, sys.maxsize, k, 'R',root)
        end = time()

    else:
        start = time()
        myArr = miniMax(boardState, k, 'R', root)
        end = time()
    root.printTree(0)
    return [myArr[0], myArr[2], end - start]

