from minimaxAlgorithms import *
from stateFunctions import *


def eval(boardState):
    myScore = calculateScore(boardState, 'R')
    opScore = calculateScore(boardState, 'Y')
    myConnects = possibleBinding(boardState, 'Y')
    opConnects = possibleBinding(boardState, 'R')
    return myScore - opScore + myConnects - opConnects * 1.25


def possibleBinding(boardState, color):
    value = 0
    for j in range(7):
        index = getPlayableRow(boardState, j) * 7 + j
        if index > 41:
            continue
        value += connections(boardState, index, color)
    return value



def connections(boardState, index, color):
    column = index % 7
    l = r = d = m = n = o = p = index
    count = 0
    # Travel Right
    while r % 7 == column & r <= 41:
        if boardState[r] == color:
            count += 1
            r += 1
        else:
            break
    # Travel Left
    while l % 7 == column & l >= 0:
        if boardState[l] == color:
            count += 1
            l -= 1
        else:
            break
    # Travel Down
    while d >= 0:
        if boardState[d] == color:
            count += 1
            d -= 7
        else:
            break

    if index % 7 < 6:
        # Travel 45 degrees
        while m % 7 <= 6 & m <= 41:
            if boardState[m] == color:
                count += 1
                m += 8
                if m % 7 == 6:
                    break
            else:
                break
        # Travel 315 degrees
        while n % 7 <= 6 & n >= 0:
            if boardState[n] == color:
                count += 1
                n -= 6
                if n % 7 == 6:
                    break
            else:
                break
    if index % 7 > 0:
        # Travel 135 degrees
        while o % 7 >= 0 & o <= 41:
            if boardState[o] == color:
                count += 1
                o += 6
                if 0 % 7 == 0:
                    break
            else:
                break
        # Travel 225 degrees
        while p % 7 >= 0 & p >= 0:
            if boardState[p] == color:
                count += 1
                p -= 8
                if p % 7 == 0:
                    break
            else:
                break
    return count
