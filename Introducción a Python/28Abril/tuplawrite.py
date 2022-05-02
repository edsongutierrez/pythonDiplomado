import pickle

tupla = ("javascript", "php", ["react", "laravel"])

with open('tupla.bin','wb') as fh:
        pickle.dump(tupla,fh)

print('done...')
