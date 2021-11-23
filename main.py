from random import randint
import random
from scoreFunctions import *
from stateFunctions import printBoard

state = initializeState()
finalBoard = ['R'] * 21 + ['Y'] * 21
random.shuffle(finalBoard)
for i in range(6):
    for j in range(7):
        color = 'R'
        if randint(0, 1) == 0:
            color = 'Y'
        state = insertAtColumn(state, j, color)

printBoard(state)
printBoard(finalBoard)
print(calculateScore(finalBoard, 'Y'))
print(calculateScore(state, 'Y'))
