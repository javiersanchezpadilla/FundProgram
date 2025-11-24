""" Matrices de 3x3 (Tres Filas, Tres Columnas)
    Aquí usamos índices del 0 al 2 en ambas dimensiones.
    
    Índices     Columna 0       Columna 1       Columna 2
    Fila 0      M[0, 0]         M[0, 1]         M[0, 2]
    Fila 1      M[1, 0]         M[1, 1]         M[1, 2]
    Fila 2      M[2, 0]         M[2, 1]         M[2, 2]
"""

import numpy as np

M3x3 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print(M3x3[0, 0])       # resultado 1
print(M3x3[0, 1])       # resultado 2
print(M3x3[0, 2])       # resultado 3

print(M3x3[1, 0])       # resultado 4
print(M3x3[1, 1])       # resultado 5
print(M3x3[1, 2])       # resultado 6

print(M3x3[2, 0])       # resultado 7
print(M3x3[2, 1])       # resultado 8
print(M3x3[2, 2])       # resultado 9


# Acceder al elemento central (5)
elemento = M3x3[1, 1]  # Devuelve 5

# Acceder a la esquina superior derecha (3)
elemento = M3x3[0, 2]  # Devuelve 3

