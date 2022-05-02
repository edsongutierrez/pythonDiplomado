import pickle

with open('diccionario.bin','rb') as fh:
        diccionario = pickle.load(fh) 

print(type(diccionario))
print(diccionario)

print('done...')
