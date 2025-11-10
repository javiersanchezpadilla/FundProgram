""" Ejemplo de uso del ciclo for para iterar sobre diferentes tipos de colecciones en Python.
    Se muestran ejemplos de iteración sobre conjuntos.
    Los conjuntos son estructuras de datos que no permiten elementos duplicados y no mantienen un orden específico"""

print("\nIterando sobre los elementos de un conjunto:")

mi_conjunto = {1, 2, 3, 4, 5, True, False, 'Hola', (10, 20)}

contador = 0

for numero in mi_conjunto:
    contador += 1
    print(f"Elemento del ciclo {contador}: ", end="")
    print(numero)   
