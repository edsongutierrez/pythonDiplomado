import pickle

with open('tupla.bin','rb') as fh:
        tupla = pickle.load(fh) 

print(type(tupla))
print(tupla)

print('done...')
