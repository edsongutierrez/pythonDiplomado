import math

a = float(input('valor a: '))
b = float(input('valor b: '))
c = float(input('valor c: '))

s = (a+b+c) / 2

if (a+b >= c) :
    r = math.sqrt(s*(s-a)*(s-b)*(s-c)) / s 
    print('El resultado es {:.2f}'.format(r))
else : 
    print('¡Error en obtener el resultado!')
