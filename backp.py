import random
import numpy as np
def sumn(w):
    return sum(w)

def F(a, b, x):
    return a*x + b
epoh = 4
g = 0.1 
N = 100


a = 7 
b = 10 

ax = random.random()
bx = random.random()

x = np.random.random(N+1)

y = [F(a, b, i)+np.random.random()/10 for i in x]
print(ax, bx)

for i in range(epoh):
    for j in range(N+1):
        delta = y[j] - F(ax, bx, x[j])
        a1 = ax + g*delta*x[j]
        b1 = bx + g*delta
        ax = a1
        bx = b1
print(ax, bx)
