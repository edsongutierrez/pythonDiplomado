from math import exp
import numpy as np
import matplotlib.pyplot as plt

def funcion1(x):
    return exp(2-x)-7 * x

def funcion2(x):
    return -exp(2-x)-7

x0 = 3
x1 = (x0 - funcion1(x0) /funcion2(x0))
print('x1: ', x1)

x2 = (x1 - funcion1(x1) / funcion2(x1))
print('x2: ', x2)

x3 = (x2 - funcion1(x2) / funcion2(x2))
print('x3: ', x3)

x = np.linspace(x0, x3, 150)
y = ((718281828)**(2-x)) - 7*x

fig, ax = plt.subplots()
ax.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()