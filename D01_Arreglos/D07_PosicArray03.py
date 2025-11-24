""" Matrices de 4x4 (Cuatro Filas, Cuatro Columnas)
    
    Aquí usamos índices del 0 al 3 en ambas dimensiones.
    
    Índices     Columna 0       Columna 1       Columna 2       Columna 3
    Fila 0      M[0, 0]         M[0, 1]         M[0, 2]         M[0, 3]
    Fila 1      M[1, 0]         M[1, 1]         M[1, 2]         M[1, 3]
    Fila 2      M[2, 0]         M[2, 1]         M[2, 2]         M[2, 3]
    Fila 3      M[3, 0]         M[3, 1]         M[3, 2]         M[3, 3]

    M4x4 = np.arange(1, 17).reshape(4, 4)    

    Esa línea de código es un excelente ejemplo de cómo usar las funciones de NumPy de manera 
    concisa y eficiente para crear matrices. Básicamente, hace tres cosas en un solo paso:
    1) Crea una secuencia de números.
    2) Convierte esa secuencia en un arreglo de NumPy.
    3) Le da la forma de una matriz 4x4.
    
    Aquí está el desglose paso a paso de lo que hace cada parte:
    
    1. np.arange(1, 17)
       ** Función: arange() significa "array range" (rango de arreglo). Es muy similar a la función 
          range() de Python, pero crea un arreglo de NumPy inmediatamente.
       
       ** Argumentos:
            1: Es el número de inicio (incluido).
            17: Es el número de fin (excluido).
            
       ** Resultado de este paso: 
            Se crea un arreglo unidimensional (ndarray) que contiene todos los enteros desde el 1 hasta el 16.
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}. 
            
    2. reshape(4, 4)
        ** Método: reshape() es un método que se aplica al arreglo creado en el paso 1. Su función es cambiar 
           la forma o redimensionar el arreglo.
           
        ** Argumentos: 4, 4: Indica que se quiere una nueva forma con 4 filas y 4 columnas.
        
        ** Condición Crítica: Para que reshape funcione, el número total de elementos debe coincidir. 
           En este caso, 16 elementos (4 * 4 = 16).
           
        ** Resultado de este paso: El arreglo unidimensional se reorganiza en una matriz bidimensional, llenando 
           la matriz por filas (primero la fila 0, luego la fila 1, y así sucesivamente).
           
                 |  1   2   3   4   |
        M4x4  =  |  5   6   7   8   |     rshape(4, 4) se encarga de cambiar la forma de redimensionar el arreglo
                 |  9   10  11  12  |                  en este caso 4 filas por 4 columnas.
                 |  13  14  15  16  |

    En Resumen: La línea es una forma elegante y eficiente de crear una matriz numérica con un patrón secuencial 
    predefinido.
"""

import numpy as np

M4x4 = np.arange(1, 17).reshape(4, 4)
# La matriz contiene números del 1 al 16


print(M4x4[0, 0])       # resultado 1
print(M4x4[0, 1])       # resultado 2
print(M4x4[0, 2])       # resultado 3
print(M4x4[0, 3])       # resultado 4

print(M4x4[1, 0])       # resultado 5
print(M4x4[1, 1])       # resultado 6
print(M4x4[1, 2])       # resultado 7
print(M4x4[1, 3])       # resultado 8

print(M4x4[2, 0])       # resultado 9
print(M4x4[2, 1])       # resultado 10
print(M4x4[2, 2])       # resultado 11
print(M4x4[2, 3])       # resultado 12



# Acceder al elemento 12 (tercera fila, última columna)
elemento = M4x4[2, 3]  # Devuelve 12
