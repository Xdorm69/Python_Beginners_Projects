# hacking a pass
import random

x = random.randint(1000,9999)

while True:
    ans = random.randint(1000 , 9999)
    print("finding....." , ans)
    if ans == x:
        break

print('Password was' , ans)

