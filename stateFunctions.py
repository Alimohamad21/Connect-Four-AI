# E for empty
# Y for yellow FOR OPPONENT
# R for RED FOR PLAYER
def getRandomBoard():
    return 'E' * 20 + 'R' * 11 + 'Y' * 11


def initializeBoard():
    return 'E' * 42


def getElementAtIndex(boardState, i, j):
    return boardState[i * 7 + j]


def isColumnFull(boardState, j):
    if boardState[j] == 'E':
        return False
    else:
        return True


def isFull(boardState):
    for j in range(7):
        if not isColumnFull(boardState, j):
            return False
    return True


def getPlayableRow(boardState, j):
    for i in range(5, -1, -1):
        if getElementAtIndex(boardState, i, j) == 'E':
            return i


def insertAtColumn(boardState, j, color):
    for i in range(5, -1, -1):
        if getElementAtIndex(boardState, i, j) == 'E':
            index = i * 7 + j
            return boardState[:index] + color + boardState[index + 1:]


def printBoard(boardState):
    for i in range(6):
        for j in range(7):
            print(getElementAtIndex(boardState, i, j), end='\t')
        print('\n')
    print('-------------------------')


def getChildren(boardState):
    children = []
    for j in range(7):
        if not isColumnFull(boardState, j):
            children.append(insertAtColumn(boardState, j, 'Y'))
    return children
