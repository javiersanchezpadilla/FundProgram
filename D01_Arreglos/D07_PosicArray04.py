""" Combinando Distintas Matrices (Slicing).
    El objetivo de combinar distintas matrices de distintas dimensiones se logra mediante 
    la extracción de sub-matrices (slicing) y la asignación.Para combinar una parte de 
    una matriz grande en una matriz más pequeña, debes asegurarte de que las dimensiones 
    coincidan.
    
    Ejemplo de Combinación (Extraer 2x2 de una 4x4) Queremos tomar el cuadrante superior 
    derecho de la matriz 4 x 4 y asignarlo a una nueva matriz 2 x 2.
"""
import numpy as np

M4x4 = np.array([[ 1,  2,  3,  4],
                 [ 5,  6,  7,  8],
                 [ 9, 10, 11, 12],
                 [13, 14, 15, 16]])

# 1. Creamos una matriz de destino 2x2
M_destino_2x2 = np.zeros((2, 2), dtype=int)
print('Inicializamos una matriz de 2x2 con ceros')
print(M_destino_2x2)

# 2. Extraemos el cuadrante superior derecho de M4x4 (Filas 0-1, Columnas 2-3)
cuadrante = M4x4[0:2, 2:4]
print('\nLa parte extraida de la matriz de 4x4 en la de 2x2 es:')
print(cuadrante)

# 3. Asignamos el cuadrante a la matriz destino
M_destino_2x2 = cuadrante

print('\nEl resultado final es:')
print(M_destino_2x2)
# Salida:
# [[3, 4],
#  [7, 8]]
