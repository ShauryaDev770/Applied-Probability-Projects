'''
Analysing the Central Limit Theorm using a dice problem by looking a the number of times 1 was observed after rolling the dice for 100 times.
'''

import matplotlib.pyplot as plt
import math as m

roll = []
prob = []
n=0
while n<=99:
        combination =(m.factorial(100))/(m.factorial(100-n)*m.factorial(n))
        r = (((1/6)**100)*combination)
        n+=1
        prob.append(r)
        roll.append(n)

x = roll
y = prob
plt.bar(x,y)
plt.title("Dice Roll Simulation")
plt.xlabel("Number of times '1' was observed")
plt.ylabel("Probability")
plt.show()




