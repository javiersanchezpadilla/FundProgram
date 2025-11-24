""" Reglas Básicas del Slicing en NumPy
    El formato general del slicing es: [inicio:fin:paso], donde el elemento 
    en la posición fin no se incluye (es un límite superior exclusivo).

    Arreglos Unidimensionales (Vectores)
    El slicing es idéntico al de las listas de Python:
"""

import numpy as np
a = np.array([10, 20, 30, 40, 50, 60])

# Obtener los elementos desde el índice 2 hasta el 4 (sin incluir el 5)
segmento_a = a[2:5]
print(segmento_a)
# Salida: [30, 40, 50]

# Obtener los elementos del inicio hasta el índice 3
segmento_b = a[:4]
print(segmento_b)
# Salida: [10, 20, 30, 40]

# Obtener todos los elementos, saltando de 2 en 2
segmento_c = a[::2]
print(segmento_c)
# Salida: [10, 30, 50]


