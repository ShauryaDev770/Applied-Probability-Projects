import math as m
import matplotlib.pyplot as plt

#n = int(input("Find the probability of n heads in 10 tosses, specify n: "))
plt.title("Coin Toss Simulator")
prob = []
number=[]
n =0
while n<=10: 
    combinations = (m.factorial(10))/(m.factorial(n)*m.factorial(10-n))
    n+=1
    r= ((((0.5)**10)*combinations)*100)
    prob.append(r)
    number.append(n)

x = number
y = prob

plt.bar(x,y)
plt.xlabel("Number of Heads")
plt.ylabel("Probability")
plt.show()

