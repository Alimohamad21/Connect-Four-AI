from stateFunctions import getChipAtIndex


def calculateHorizontals(boardState, color):    # function to calculate horizontal connected fours
    score = 0
    for i in range(6):
        count = 0
        for j in range(7):
            if getChipAtIndex(boardState, i, j) == color:
                count += 1
            else:
                count = 0
            if count >= 4:
                score += 1
    return score


def calculateDownToUpDiagonal(boardState, color):
    score = 0
    for j in range(4):
        for i in range(5, 2, -1):

            if getChipAtIndex(boardState, i, j) == getChipAtIndex(boardState, i - 1, j + 1) == getChipAtIndex(
                    boardState, i - 2, j + 2) == getChipAtIndex(boardState, i - 3, j + 3) == color:
                score += 1

    return score


def calculateUpToDownDiagonal(boardState, color):
    score = 0
    for j in range(4):
        for i in range(3):
            if getChipAtIndex(boardState, i, j) == getChipAtIndex(boardState, i + 1, j + 1) == getChipAtIndex(
                    boardState, i + 2, j + 2) == getChipAtIndex(boardState, i + 3, j + 3) == color:
                score += 1

    return score


def calculateVerticals(boardState, color):   # function to calculate vertical connected fours
    score = 0
    for j in range(7):
        count = 0
        for i in range(6):
            if getChipAtIndex(boardState, i, j) == color:
                count += 1
            else:
                count = 0
            if count >= 4:
                score += 1
    return score


def calculateDiagonals(boardState, color):   # function to calculate diagonal connected fours
    return calculateUpToDownDiagonal(boardState, color) + calculateDownToUpDiagonal(boardState, color)


def calculateScore(boardState, color):     # function to calculate the total score for a player
    return calculateHorizontals(boardState, color) + calculateVerticals(boardState, color) + calculateDiagonals(boardState, color)
