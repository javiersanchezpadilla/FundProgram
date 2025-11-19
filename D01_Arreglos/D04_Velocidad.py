""" En este ejemplo vamos a medir la velocidad de un arreglo contra una lista
     A una lista de 10,000,000 numeros le vamos a sumar a cada valor un total de 10,
     de igual manera a un arreglo de 10,000,000 numeros le vamos a sumar a cada uno
     de ellos un total de 10

"""

import numpy as np 
import time

N = 10000001

mi_lista = list(range(N))           # Generamos la lista con valores desde el 0 hata el 10,000,000
print(mi_lista[:100])               # imprimimos los primeros 100 valores de la lista (del 0 al 99)

tiempo_de_inicio = time.time()      # Tomamos el tiempo inicial de ejecución del programa
indice_lista = 0

for x in mi_lista:
    x += 10
    mi_lista[indice_lista] = x
    indice_lista += 1

# Otra forma de hacer la operacion es así:
# mi_lista = [x+10 for x in mi_lista]

print('\nEl tiempo que tardo la operación con LISTAS fue:', time.time() - tiempo_de_inicio, 'Segundos')
print(mi_lista[:20])                # Imprimimos los primeros 20 valores (del 0 al 19)


mi_arreglo = np.arange(N)
tiempo_de_inicio = time.time()      # Tomamos el tiempo inicial de ejecución del programa

mi_arreglo += 10
print('\nEl tiempo que tardo la operación con ARREGLOS fue:', time.time() - tiempo_de_inicio, 'Segundos')
