# E for empty
# Y for YELLOW FOR PLAYER
# R for RED FOR OPPONENT
def initializeBoard():   # function to initialize at a certain board
    return 'E' * 42


def getChipAtIndex(boardState, i, j):    # function to get a chip at index i,j
    return boardState[i * 7 + j]


def columnIsFull(boardState, j):   # function to check if a certain column is full
    if boardState[j] == 'E':
        return False
    else:
        return True


def isFull(boardState):     # function to check if the board is full
    for j in range(7):
        if not columnIsFull(boardState, j):
            return False
    return True


def getPlayableRow(boardState, j):   # function to get the first playable position in a certain row
    for i in range(5, -1, -1):
        if getChipAtIndex(boardState, i, j) == 'E':
            return i


def insertAtColumn(boardState, j, color):   # function to insert a chip at a certain column
    i = getPlayableRow(boardState, j)
    index = 7*i+j
    return boardState[:index] + color + boardState[index + 1:]


def printBoard(boardState):       # function to print the whole board
    for i in range(6):
        for j in range(7):
            print(getChipAtIndex(boardState, i, j), end='\t')
        print('\n')
    print('-------------------------')


def getChildren(boardState, color):   # function to expand the board's children by generating all possible moves
    children = []
    for j in range(7):
        if not columnIsFull(boardState, j):
            children.append(insertAtColumn(boardState, j, color))
    return children
