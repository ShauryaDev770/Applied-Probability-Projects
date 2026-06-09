import math as m
import matplotlib.pyplot as plt
import numpy as np


plt.title("Coin Toss Simulator")
prob = []
number=[]
n =0
while n<=20: 
    combinations = (m.factorial(20))/(m.factorial(n)*m.factorial(20-n))
    n+=1
    r= ((((0.5)**20)*combinations)*100)
    prob.append(r)
    number.append(n)

x = number
y = prob

max_idx = np.argmax(y)  
x_max = x[max_idx]
y_max = y[max_idx]

plt.plot(x,y)
plt.grid()
plt.plot(x_max, y_max, marker="o", color="blue", markersize=8, label="Global Maxima")
plt.vlines(x=x_max, ymin=0, ymax=y_max, colors="red", linestyles="dashed", alpha=0.7)
plt.hlines(y=y_max, xmin=0, xmax=x_max, colors="red", linestyles="dashed", alpha=0.7)
plt.xlabel("Number of Heads")
plt.ylabel("Probability")
plt.show()
 
