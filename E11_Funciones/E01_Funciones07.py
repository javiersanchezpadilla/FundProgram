""" Imprime en pantalla frases como la siguiente:
    f'{nombre} se encuentra en el índice {indice}'
    Donde nombre debe ser cada uno de los nombres de la lista 
    a continuación, y el índice, obtenido mediante enumerate.
    lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", 
                     "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
mis_tuplas = list(enumerate(lista_nombres))

for indice,nombre in mis_tuplas:
    print(f'{nombre} se encuentra en el índice {indice}')
