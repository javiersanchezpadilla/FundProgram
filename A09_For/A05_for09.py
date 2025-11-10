""" Ejemplo de uso del ciclo for para iterar sobre diferentes tipos de colecciones en Python.
    Se muestran ejemplos de iteración sobre tuplas.
    LAs tuplas son estructuras inmutables pero iterables"""

print("\nIterando sobre los elementos de una tupla:")

mi_tupla = (100, True, [1, 2, 3], 'Hola', {'clave': 'valor', 'numero': 42})

contador = 0

for valor in mi_tupla:
    contador += 1
    print(f"Elemento del ciclo {contador}: ", end="")
    print(valor)
