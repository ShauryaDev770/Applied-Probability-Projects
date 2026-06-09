'''
Lets say there are 10,000 people playing a gambling game where upon winning, the player gets 10 ruppes. Lets find out the 
probability of going broke at the end.
'''

import random

Gamble = ["Win","Loss"]

def gamble():
    capital = 100
    while True:
        
        final = ()
        r = random.choice(Gamble)
        if r == "Win":
            capital+=10
        if r == "Loss":
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


