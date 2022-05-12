import statistics

def sum(numeros):
    total = 0
    for x in numeros:
        total += x
    return total

print("sum: ",sum((9, 1, 3.12, 7, 9.54)))

def avg(l): 
    avg = sum(l) / len(l) 
    return avg
  
lista = [3,5,6,8,7] 
res = avg(lista) 
  
print("avg: ", res)

print("min: ", min(lista))

print("max: ", max(lista))

def rango(x):
    list = []
    for i in range(x): 
        list.append(i)
    return list

print("range: ", rango(9))

list = [12, 24, 36, 48, 60]
std = statistics.pstdev(list)
print("srd: " + str(std))

set1 =[1, 2, 9, 6, 4, 2, 4, 6, 3, 6]
mode = statistics.mode(set1)
print("mode: ", mode)


