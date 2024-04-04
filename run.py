# run.py  program to calculate the average numbers of 
# runs to get a 1 and snake eyes when rolling two dice.

import random

first_1 = 0
snake=0
dfirst_1 = {}
dsnake = {}
for r in range(1,20):
    dfirst_1[r]=0
    
for r in range(1,50):
    dsnake[r]=0



for roll in range(100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    first_1+=1
    snake +=1
    
    if dice1 == 1 or dice2 == 1:
        print(f"first 1 in {first_1} rolls")
        dfirst_1[first_1]=dfirst_1[first_1]+1
        first_1=0
    elif dice1 == 1 and dice2 == 1:
        print(f"first snake in {snake} rolls")
        dsnake[snake] = dsnake[snake]+1
        snake = 0

   
print("dfirst_1",dfirst_1)  
print("dsnake",dsnake)

