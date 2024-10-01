# make a die roll game
# optional features 
# to ask user how many die he wants to roll
# add a counter

import random

while True:
    res = input("want to play the game y | n\n").lower()
    if res == 'y':
        n = int(input("How many die you want to roll?\n"))
        def roll(n):
            dies = []
            while n > 0:
                d = random.randint(1,6)
                dies.append(d)
                n-=1
            return dies
        print(roll(n))
    elif res == 'n':
        print("Thanks for playing the game")
    else:
        print("Game Over!!")
        break

    