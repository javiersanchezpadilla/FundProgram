""" Acceder a elementos en matrices (arreglos de NumPy con más de una dimensión) es un 
    concepto fundamental. La clave es recordar que necesitas un índice por cada dimensión.
    En una matriz 2D, el acceso siempre sigue el formato:
    
    matriz[fila, columna]

    Acceso a Elementos por Dimensión1. 2x2 (Dos Filas, Dos Columnas)Esta es la matriz más sencilla. 
    Solo hay cuatro elementos, y para acceder a ellos se usan índices del 0 al 1 en ambas dimensiones.
    
    Índices     Columna 0       Columna 1
    --------------------------------------
    Fila 0      M[0, 0]         M[0, 1]     
    Fila 1      M[1, 0]         M[1, 1]
"""

import numpy as np

M2x2 = np.array([[10, 20],
                 [30, 40]])

print(M2x2[0, 0])       # resultado 10
print(M2x2[0, 1])       # resultado 20
print(M2x2[1, 0])       # resultado 30
print(M2x2[1, 1])       # resultado 40

