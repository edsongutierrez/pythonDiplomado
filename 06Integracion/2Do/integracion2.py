
def f(x):
    return ((7**-(x)) +3)

a=2
b=-1
r1=f(a)*(b-a)

print('Regla del Rectángulo I=',r1)

m=(a+b)/2
r2=f(m)*(b-a)

print('Regla del punto medio I=',r2)

r3=((b-a)/2)*(f(a)+f(b))

print('Regla del Trapecio I=',r3)

m2=(a+b)/2
r4=((b-a)/6)*(f(a)+4*f(m2)+f(b))

print('Regla de Simpson I=',r4)

