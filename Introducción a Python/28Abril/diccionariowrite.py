import pickle

diccionario = {"México":"Ciudad de México", "Perú": "Lima", "Argentina": "Buenos Aires"}

with open('diccionario.bin','wb') as fh:
        pickle.dump(diccionario,fh)

print('done...')
