import random

win_count = 0
lose_count = 0

flag = True

while flag:

    #comp logic 
    c = random.randint(1,100)
    if c < 33 :
        c = '🪨' 
    elif c >= 33 and c < 66:
        c = '📃'
    else:
        c = '✂️'

    res = input("Enter a response\nrock | paper | scissor \n(r / p / s)\n")

    if c == '🪨' and res == 'r':
        print("Game Drawn")
        print("Win Count : " , win_count , 'Lose Count : ' , lose_count)
        
        
    elif c == '🪨' and res == 'p':
        print("You have Won")
        print("You Chose 📃 and comp chose 🪨")
        win_count+=1
        print("Win Count : " , win_count , 'Lose Count : ' , lose_count)
        
    elif c == '🪨' and res == 's':
        print("You have Lost")
        print("You Chose ✂️ and comp chose 🪨")
        lose_count+=1
        print("Win Count : " , win_count , 'Lose Count : ' , lose_count)


    
    elif c == '📃' and res == 'r':
        print("You have Lost")
        print("You Chose 🪨 and comp chose 📃")
        lose_count+=1
        print("Win Count : " , win_count , 'Lose Count : ' , lose_count)
    elif c == '📃' and res == 's':
        print("You have Won")
        print("You Chose ✂️ and comp chose 📃")
        win_count+=1
        print("Win Count : " , win_count , 'Lose Count : ' , lose_count)
    elif c == '📃' and res == 'p':
        print("Game Drawn")
        print("You Chose 📃 and comp chose 📃")
        print("Win Count : " , win_count , 'Lose Count : ' , lose_count)

    

    elif c == '✂️' and res == 'r':
        print("You have Won")
        print("You Chose 🪨 and comp chose ✂️")
        win_count+=1
        print("Win Count : " , win_count , 'Lose Count : ' , lose_count)
    elif c == '✂️' and res == 's':
        print("Game Drawn")
        print("You Chose ✂️ and comp chose ✂️")
        print("Win Count : " , win_count , 'Lose Count : ' , lose_count)
    elif c == '✂️' and res == 'p':
        print("You Have Lost")
        print("You Chose 📃 and comp chose ✂️")
        lose_count+=1
        print("Win Count : " , win_count , 'Lose Count : ' , lose_count)
        #pass Logic
    else:
        flag = False

print("Game Over")  