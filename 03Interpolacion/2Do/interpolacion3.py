#Ejecrcicio 3
import sympy as sym

def polinomiointerpolacion(d):
    b1 = ((d[1][1]) - (d[0][1])) / ((d[1][0]) - (d[0][0]))
    b2 = (((d[2][1]) - (d[1][1])) / ((d[2][0]) - (d[1][0])) - (b1)) / ((d[2][0]) - (d[0][0]))
    x = sym.Symbol('x')
    y = d[0][1] + (b1) * (x - (d[0][0])) + (b2) * ((x - (d[0][0])) * (x - (d[1][0])))
    return y

example3 = [[2, 1.43], [3.2, 2.79], [4, 3.56]]

print("Polinomio es ", polinomiointerpolacion(example3))
