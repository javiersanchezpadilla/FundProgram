""" En este ejemplo se muestra el uso de un bucle for para iterar sobre los elementos de otra lista.
    Las listas son estructuras de datos que pueden contener múltiples elementos, 
    en este caso la lista contiene sub tipos distintos de valores, incluso otras estructuras de datos."""

print("\nIterando sobre los elementos de otra lista:")

lista = [10, ['a', 'b', 'c', 'd'], 'casa', True, {1 ,2 ,3 ,4}, {'nombre':'juan', 'apellido':'gutierrez'}, (100, 200, 300)]

contador = 0
for elemento in lista:
    contador += 1
    print(f"Elemento del ciclo {contador}: ", end="")
    print(elemento)

