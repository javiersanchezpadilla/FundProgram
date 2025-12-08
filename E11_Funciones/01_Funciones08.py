""" Crea una lista formada por las tuplas (índice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada carácter del string Pyton.
    Llama a la lista obtenida con el nombre de variable lista_índices.

    Resultao esperado:
    [(0, 'P'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
"""

lista_indices = list(enumerate(list("Python")))
print(lista_indices)
