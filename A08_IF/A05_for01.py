""" Ejemplo del uso de un bucle for para iterar sobre una secuencia de números.
    En este ejemplo, se utiliza un bucle for para imprimir los números del 1 al 10.
"""

print("Imprimiendo cada letra de la cadena usando un bucle for:")
for letra in "Python es un lenguaje de programación":
    print(letra)


print("\nIterando sobre una cadena de texto:")
cadena = "Hola Mundo"
for caracter in cadena:
    print(caracter)

print("\nIterando sobre otra cadena de texto:")
cadena = "123456789"
for digito in cadena:       # Recordar que en este momento digito es una cadena de texto
    digito = int(digito)    # Convertimos la cadena a numero entero
    print(digito + 10)


print("Imprimiendo numeros del 1 al 10 usando un bucle for:")
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)    


print("\nIterando sobre los elementos de una lista:")
lista = ['manzana', 'banana', 'cereza']
for fruta in lista:
    print(fruta)


print("\nIterando sobre los elementos de otra lista:")
lista2 = [10, 20, 30, 40, 50]
for numero in lista2:
    print(numero)


print("\nIterando sobre los elementos de otra lista:")
lista3 = [1, 'dos', 3.0, True]
for elemento in lista3:
    print(elemento)


print("\nIterando sobre los elementos de una tupla:")
mi_tupla = (100, 200, 300)
for valor in mi_tupla:
    print(valor)


print("\nIterando sobre los elementos de un conjunto:")
mi_conjunto = {1, 2, 3, 4, 5}
for numero in mi_conjunto:
    print(numero)   


print("\nIterando sobre los elementos de un diccionario:")
print( "Usando solo las claves del diccionario:" )
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
for clave in mi_diccionario:
    print(clave) 


print("Extrayendo Usando solo las claves del diccionario:")
print("Pero ademas mostrando el elemento del diccionario asociado a la clave:" )
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
for clave in mi_diccionario:
    print(clave, mi_diccionario[clave]) 


print("\nUsando items() para obtener claves y valores:" )
for clave, valor in mi_diccionario.items():
    print(clave, valor) 


