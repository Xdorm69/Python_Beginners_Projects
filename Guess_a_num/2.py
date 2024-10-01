#create a number guessing game

import random 
ans = random.randint(1,100)
while True:
    while True:
        try:
            n = int(input("Enter num between 1 and 100 :\n"))
            break
        except:
            print("Invalid Response")
    if n > ans:
        print(n , 'too big try a smaller num\n')
    elif n < ans:
        print(n , 'too small try a bigger num\n')
    else:
        print("\nCongratulation you have found the ans :" , ans)
        break

print("Game Over")
    




