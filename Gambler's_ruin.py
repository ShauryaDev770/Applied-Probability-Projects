'''
Lets say there are 10,000 people playing a gambling game where upon winning, the player gets 10 ruppes. Lets find out the 
probability of going broke at the end.
But there is a twist, the game is a little biased by 0.01% against them.
'''

import random

def gamble():
    capital = 100
    while True:
        
        final = ()
        r_boolean = random.random() < 0.49
        if r_boolean == True:
            capital+=10
        if r_boolean == False:
            capital-=10
                                          
        if capital ==0 or capital == 200:
            break
        else:
            continue
    final = capital
    return final

n = 0
total =[]
while n<=9999:
    total.append(gamble())   
    n+=1

print(total)
broke = total.count(0)

probability_broke = (broke/10000)*100
print("Probability of going broke: ",probability_broke,"%")


