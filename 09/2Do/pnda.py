import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')

print(tuple(iris['sepal length']))
print('\n')
print(dict(iris['sepal width']))
print('\n')
print(list(iris['petal length']))

# Dato: si el archivo se llama 'panda.py' al momento de compilar 
# el archivo marcar error por el read_csv, asi que por eso se
# cambio el nombre del archivo.
