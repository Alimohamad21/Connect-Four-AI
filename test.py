import scoreFunctions
from constants import POTENTIAL_SCORES
print("[", end=" ")
for i in range(6):

    for j in range(7):
        state = ['Y'] * 42
        state[i*7+j] = 'R'
        score = 69-scoreFunctions.calculateScore("".join(state), 'Y')
        print(score,  end=",")

print("]")
