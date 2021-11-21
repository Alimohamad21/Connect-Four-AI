from scoreFunctions import *
from stateFunctions import printBoard, insertAtColumn

state = 'E'*42
for i in range(6):
    for j in range(7):
        if(i==3 and j==4):
           state = insertAtColumn(state,j,'R')
        else:
            state = insertAtColumn(state, j, 'Y')

printBoard(state)

print(uptodown_diagonal_count(state, 'Y') )
print(downtoup_diagonal_count(state,'Y'))