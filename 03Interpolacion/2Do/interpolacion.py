import sympy as sym

#Ejercicio 1
def interpolationx(d, y):
    x = (((d[1][0]) - (d[0][0])) / ((d[1][1]) - (d[0][1]))) * (y - d[0][1]) + d[0][0]
    return x
example1=[[-4, -2],[1, 5]] #[x0, y0], [x1, y1], [x2, 3.7]
#example1=[[1.8, -4.25],[-3.25, -5.1]] #[x0, y0], [x1, y1], [x2, 3.7]
#y=1.8
y=3.7
print("Cuando y = {} , x es: ".format(y),interpolationx(example1, y))


#Ejercicio 2
def interpolationy(d, x):
    b1 = (d[1][1] - d[0][1]) / (d[1][0] - d[0][0]) #y1-y0 / x1 - x0
    b2 = (((d[2][1] - d[1][1]) / (d[2][0] - d[1][0])) - b1) / (d[2][0] - d[0][0]) #((y2 - y1 / x2 - x1) - b1) / x2 - x0

    val = (  (((d[3][1]) - (d[2][1])) / ((d[3][0]) - (d[2][0]))) - 
             (((d[2][1]) - (d[1][1])) / ((d[2][0]) - (d[1][0]))) ) / ((d[3][0] ) - (d[1][0]))
    b3 = (val - b2) / ((d[3][0]) - (d[0][0]))

    y = d[0][1] + (((b1) * (x - d[0][0])) + (b2 * (((x - d[0][0]) * (x - d[1][0])))) + ((b3) * ((x - d[0][0]) * (x - d[1][0]) * (x - d[2][0]))))
    return y
example2=[[-2, 4],[-1, -2], [3, 5], [4.3, 11]] # [x0, y0], [x1, y1], [x2, y2], [x3, y3], [7.7, y4]
#example2=[[2,3], [5, -2], [6, 5], [8, -1]] # [x0, y0], [x1, y1], [x2, y2], [x3, y3], [7.7, y4]
#x=7
x=7.7
print("Cuando x = {} , y es: ".format(x), interpolationy(example2 , x))

#Ejecrcicio 3
def polinomiointerpolacion(d):
    b1 = ((d[1][1]) - (d[0][1])) / ((d[1][0]) - (d[0][0]))
    b2 = (((d[2][1]) - (d[1][1])) / ((d[2][0]) - (d[1][0])) - (b1)) / ((d[2][0]) - (d[0][0]))
    x = sym.Symbol('x')
    y = d[0][1] + (b1) * (x - (d[0][0])) + (b2) * ((x - (d[0][0])) * (x - (d[1][0])))
    return y

example3 = [[2, 1.43], [3.2, 2.79], [4, 3.56]]

print("Polinomio es ", polinomiointerpolacion(example3))

