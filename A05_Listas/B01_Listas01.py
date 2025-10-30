""" En estee ejemplo trabajaremos los conceptos básicas para el uso de listas

    Definición y Características
    ----------------------------
    Una lista es una de las estructuras de datos más fundamentales y versátiles en Python.Se define como:
    
    1. El Contenedor de Propósito GeneralLa lista es un contenedor ordenado y mutable que puede guardar una 
       colección de elementos.

    2. Características Clave
    Característica      Descripción                                             Ejemplo Práctico
    Ordenada        El orden de los elementos se mantiene.              ["manzana", "pera"] es diferente de 
                    El elemento que está en la posición 0               ["pera", "manzana"].
                    siempre será el primero.

    Mutable         Puedes cambiar, agregar o eliminar elementos        Puedes usar lista.append("nuevo")
                    después de que la lista ha sido creada.             o lista[1] = "cambio".
                    
    Heterogénea     Puede contener elementos de diferentes tipos        mi_lista = ["Hola", 10, 3.14, True]
                    de datos (enteros, cadenas, booleanos, e 
                    incluso otras listas).

                    
    1. Lista Vacía. Para crear una lista sin elementos:

            inventario_vacio = []

    2. Lista de Cadenas (Strings). Una lista que contiene los nombres de algunas frutas:

            frutas = ["manzana", "banana", "cereza", "uva"]

    3. Lista Heterogénea (Diferentes Tipos). Una lista que combina números, texto y valores booleanos:

            datos_usuario = ["Juan Pérez", 35, True, 1.75]

    4. Lista Anidada (Lista dentro de otra Lista). Una lista donde cada elemento es otra lista (ideal para 
       representar matrices o coordenadas):

            coordenadas = [
                            [10, 20],  # Coordenada X, Y del punto 1
                            [5, 12],   # Coordenada X, Y del punto 2
                            [8, 15]  ]

"""

lista_frutas = ['manzana', 'pera', 'melon', 'sandia', 'uva']

# podemos agregar mas elementos a nuestra lista
lista_frutas.append('piña')
lista_frutas.append('mango')
print(lista_frutas)

# Podemos imprimir los elementos de nuestra list con base a su índice
# indice -->     0         1        2        3       4      5        6
#           ['manzana', 'pera', 'melon', 'sandia', 'uva', 'piña', 'mango']
# el elmento que queremos cambiar esta en el índice 0
print('\nIMPRIMIENDO POSICIONES DE LA LISTA (INDICES)\n')
print('El primer elemento de la lista de frutas es', lista_frutas[0])
print('El segundo elemento de la lista de frutas es', lista_frutas[1])
print('El tercer elemento de la lista de frutas es', lista_frutas[2])
print('El cuarto elemento de la lista de frutas es', lista_frutas[3])
print('El quinto elemento de la lista de frutas es', lista_frutas[4])
print('El sexto elemento de la lista de frutas es', lista_frutas[5])
print('El septimo elemento de la lista de frutas es', lista_frutas[6])

# podemos ubicar la posicion del indice de un elemento
print('\nBUSQUEDA DE INDICES DENTRO DE LA LISTA\n')
posicion = lista_frutas.index('uva')
print('La fruta uva se encuentra dentro de la lista en la posicion', posicion)
print('La fruta mango se encuentra dentro de la lista en la posicion', lista_frutas.index('mango'))
print('La fruta melon se encuentra dentro de la lista en la posicion', lista_frutas.index('melon'))


# podemos hacer slicing
# imprimir desde el elemento 3 hasta el final 
print('\nPODEMOS REALIZAR SLICING CON LA LISTA\n')
print('Valores de la lista', lista_frutas)
print('Imprimir a partir del indice 3', lista_frutas[3:])
print('Imprimir el último valor de la lista', lista_frutas[-1])
print('Imprimir la lista invertida', lista_frutas[::-1])
print('Imprimir de la posicion 2 a la 4', lista_frutas[2:5])
print('Imprimir toda la lista cada dos elementos', lista_frutas[::2])

# cambiar el primer elemento "manzana" por "kiwi", (hacemos referencia su indidice)
print('\nCAMBIAR ELMENTOS DE LA LISTA')
print('List original             ', lista_frutas)
lista_frutas[0] = 'kiwi'
lista_frutas[-1] = 'durazno'
print('La nueva lisa queda asi:  ', lista_frutas)

# Podemos elimiar elementos de la lista
# eliminar el último elemento de la lista, usar POP()
print('\nELIMINA ELEMENTOS DE LA LISTA\n')
print('List original             ', lista_frutas)
lista_frutas.pop()  # Elimina el ultimo elemento
print('List cambiada             ', lista_frutas)
lista_frutas.pop()  # Elimina el ultimo elemento
print('List cambiada             ', lista_frutas)

# podemos borrar elementos dentro de la lista (posicion distinta a la final)
lista_frutas.pop(1)  # Elimina el segundo valor de la lista (0 primer valor, 1 segundo, 2 tercero)
print('Eliminar segundo elemento ', lista_frutas)
lista_frutas.pop(2)
print('Eliminar tercer  elemento ', lista_frutas)

# podemos ordenar las listas
print('\nORDENAMIENTO DE LAS LISTAS')
lista_frutas.sort()
print('Lista ordenada ascendente ', lista_frutas)
lista_frutas.sort(reverse=1)
print('Orden desendente          ', lista_frutas)


# Podemos tener listas de distintos tipos

lista_numeros = [5, 4, 2, 7, 0, 9, 1]
lista_letras = ['a', 'g', 'q', 'z', 'o', 'e']
lista_nombres = ['juan', 'pedro', 'raquel', 'diana', 'jorge']

# podemos crear una lista de listas
lista_combinada = [ 1, 'casa', [[1, 2], [3, 4]], lista_frutas, lista_numeros, lista_letras, lista_nombres]

print('\nACCEDIENDO A LOS ELEMENTOS INDIVIDUALES DE LA LISTA COMBINADA')
print('Lista original:', lista_combinada)
print('Elemento 0 ', lista_combinada[0])
print('Elemento 1 ', lista_combinada[1])
print('Elemento 2 ', lista_combinada[2])
print('Elemento 3 ', lista_combinada[3])
print('Elemento 4 ', lista_combinada[4])
print('Elemento 5 ', lista_combinada[5])
print('Elemento 6 ', lista_combinada[6])

print('\nEl elemento 1 de la lista es ', lista_combinada[1])
print(lista_combinada[1][0])
print(lista_combinada[1][1])
print(lista_combinada[1][2])
print(lista_combinada[1][3])

print('\nEl elemento 2 de la lista es ', lista_combinada[2])
print(lista_combinada[2][0])
print(lista_combinada[2][0][0])
print(lista_combinada[2][0][1])
print(lista_combinada[2][1])
print(lista_combinada[2][1][0])
print(lista_combinada[2][1][1])

print('\nEl elemento 6 de la lista es ', lista_combinada[6])
print(lista_combinada[6][0])
print(lista_combinada[6][0][0])
print(lista_combinada[6][0][1])
print(lista_combinada[6][0][2])
print(lista_combinada[6][0][3])

print(lista_combinada[6][1])
print(lista_combinada[6][1][0])
print(lista_combinada[6][1][1])
print(lista_combinada[6][1][2])
print(lista_combinada[6][1][3])
print(lista_combinada[6][1][4])
