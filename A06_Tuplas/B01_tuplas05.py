""" Podemos hacer casting con las tuplas, buscar índices y contar valores de las tuplas """


mi_tupla = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
print(mi_tupla)

# Imprimir del primer elemento hasta el indice 5-1 = 4 (el valor 5 no es inclusivo) ('a', 'b', 'c', 'd', 'e')
print(mi_tupla[:5])     
# imprimit desde el primer elemento hasta el final pero saltando de dos en dos ('a', 'c', 'e', 'g')
print(mi_tupla[::2])    
# Imprimir la tupla desde el princiío hasta el final pero con un paso de uno en uno hacia atras ('h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')
print(mi_tupla[::-1])   
# Imprimir desde el índice 3 hasta el 6-1 = 5  ('d', 'e', 'f')
print(mi_tupla[3:6])    


# Podemos buscar la posicion de un elemento del índice dentro de una tupla
print('\nla posicion del indice de la letra "g" dentro de la tupla es:', mi_tupla.index('g'))

# podemos contar el numero de repeticiones de un elemento dentro de una tupla
print('\nEl número de veces que aparece la letra "h" dentro de la tupla es:', mi_tupla.count('h'))

mi_otra_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2, 3, 2, 4, 5, 6, 4, 2, 2, 2, 2, 2)
print('\nEl numero de repeticiones del valor "2" en mi_otra_tupla es', mi_otra_tupla.count(2))

