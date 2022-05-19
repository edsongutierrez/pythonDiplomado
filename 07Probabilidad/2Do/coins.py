import random 

def flips():
    #cara es 0 y cruz 1
    cara = 0
    cruz = 0
    for i in range(10000):
        x = random.randint(0,1)
        if x == 0:
            cara += 1
        else :
            cruz += 1

    return {'Cara': cara, 'Cruz': cruz} 

print(flips())
