#Ejercicio 1
def interpolationx(d, y):
    x = (((d[1][0]) - (d[0][0])) / ((d[1][1]) - (d[0][1]))) * (y - d[0][1]) + d[0][0]
    return x
example1=[[-4, -2],[1, 5]] #[x0, y0], [x1, y1], [x2, 3.7]
#example1=[[1.8, -4.25],[-3.25, -5.1]] #[x0, y0], [x1, y1], [x2, 3.7]
#y=1.8
y=3.7
print("Cuando y = {} , x es: ".format(y),interpolationx(example1, y))
