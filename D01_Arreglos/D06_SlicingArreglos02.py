""" SLICING EN MÚLTIPLES DIMENSIONES (MATRICES)
    Aquí es donde el slicing de NumPy se vuelve crucial. Usas una coma (,) 
    para separar las reglas de slicing de cada dimensión (fila, columna, etc.).

    El formato es: [filas, columnas]
    Ejemplo con Matriz 2D (Tabla)

    Cuando haces slicing en un arreglo de NumPy, generalmente no se crea una copia 
    de los datos. En su lugar, el slice es una vista o referencia a la memoria del 
    arreglo original.

    Esto significa que si modificas el slice, también modificas el arreglo original. 
    Esto es una diferencia clave con respecto a las listas de Python y está diseñado 
    para ahorrar memoria y ser más rápido.

"""

import numpy as np

# Creamos una matriz de 3x3
matriz = np.array([
    [1, 2, 3],  # Fila 0
    [4, 5, 6],  # Fila 1
    [7, 8, 9]   # Fila 2
])

                            # Obtener una sola fila (Fila 1)
fila_1 = matriz[1, :]
print(fila_1)               # Salida: [4, 5, 6] (El ':' significa 'todas las columnas')

                            # Obtener una sola columna (Columna 0)
columna_0 = matriz[:, 0]
print(columna_0)            # Salida: [1, 4, 7] (El ':' significa 'todas las filas')

                            # Obtener un subconjunto (el elemento 5 y 6)
submatriz = matriz[1, 1:]   
print(submatriz)            # Salida: [5, 6] (Fila 1, desde la columna 1 hasta el final)    

# MODIFICAR EL SLICE
# ------------------ 
# Cuando haces slicing en un arreglo de NumPy, generalmente no se crea una copia 
# de los datos. En su lugar, el slice es una vista o referencia a la memoria del 
# arreglo original.

# Esto significa que si modificas el slice, también modificas el arreglo original. 
# Esto es una diferencia clave con respecto a las listas de Python y está diseñado 
# para ahorrar memoria y ser más rápido.


submatriz[0] = 99

print(matriz)
                            # El arreglo original ha cambiado:
                            # [[ 1,  2,  3],
                            #  [ 4, 99,  6],  <- ¡El 5 ahora es 99!
                            #  [ 7,  8,  9]]
