'''
Imagine a room filled with 365 people, now what are the chances that two people have the 
same birthdays? Intuitively, fells high. Great but if we keep on removing people from the 
room, then what are the chances for getting same birthdays?
Lets figure it out.
'''

import matplotlib.pyplot as plt
import math as m

#no_of_people = k
k=0
x = []
y = []

while k<=100:
    k+=1
    x.append(k)

while True:
    for i in x:
        Prob_no_bday_match = (m.perm(365,i))/365**i
        Prob_match = 1 - Prob_no_bday_match
        y.append(Prob_match)

    break

plt.plot(x,y,linestyle = ":")
plt.grid()

plt.show()

