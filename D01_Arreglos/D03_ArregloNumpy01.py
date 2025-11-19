""" Uso de la Librería NumPy.

    NumPy (Numerical Python) es el estándar industrial para el manejo de arreglos 
    multidimensionales (ndarray) y ofrece una velocidad y funcionalidad inigualables 
    para la computación científica y el análisis de datos.

    Para instalar numpy desde la consola de texto debemos ejecutar el comando:

    pip install numpy

    Durante el proceso de instalación de la libreria veran algo similar a esto:
        Collecting numpy
        Downloading numpy-2.3.5-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.1/62.1 kB 861.8 kB/s eta 0:00:00
        Downloading numpy-2.3.5-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.6 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.6/16.6 MB 11.4 MB/s eta 0:00:00
        Installing collected packages: numpy
        Successfully installed numpy-2.3.5

        """
import numpy as np

# Creamos un array de NumPy (ndarray). Por defecto, inferirá el tipo como entero.
mi_array_numpy = np.array([10, 20, 30, 40, 50])

print(f"\nTipo de objeto: {type(mi_array_numpy)}")
print(f"Arreglo inicial de NumPy: {mi_array_numpy}")

# --- Operaciones vectorizadas (la gran ventaja de NumPy) ---

# Multiplicar TODOS los elementos por 2 con una sola instrucción.
# Esto es imposible de hacer directamente con una lista o con el array estándar.
mi_array_multiplicado = mi_array_numpy * 2
print(f"Arreglo multiplicado por 2: {mi_array_multiplicado}")

# Sumar un valor a TODOS los elementos
mi_array_sumado = mi_array_numpy + 5
print(f"Arreglo sumado + 5: {mi_array_sumado}")

# --- Arreglo multidimensional (Matriz) ---

# Crear una matriz (arreglo 2D) de 3x3
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Matriz 3x3:\n{matriz}")
print(f"Dimensiones (shape): {matriz.shape}")