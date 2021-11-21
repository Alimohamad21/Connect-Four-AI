# E for empty
# Y for yellow FOR OPPONENT
# R for RED FOR PLAYER

state = 'E' * 42


def getElementAtIndex(boardState, i, j):
    return boardState[i * 7 + j]


def isFull(boardState, j):
    if boardState[j] == 'E':
        return False
    else:
        return True


def insert(boardState, j, color):
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
        if not isFull(boardState, j):
            children.append(insert(boardState, j, 'Y'))
    return children


for i in range(6):
    for j in range(7):
        state = insert(state, j, 'Y')
printBoard(state)
