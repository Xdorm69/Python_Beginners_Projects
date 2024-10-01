# to create a dice roll game
# two dice every time

import random

def roll():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    return d1 , d2

while True:
    res = input("Want to play more y | n\n")
    if (res == 'y' or res == 'Y'):
        print(roll())
    else:
        break
print("Game Over")
