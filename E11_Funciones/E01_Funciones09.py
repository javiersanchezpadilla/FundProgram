""" Imprime en pantalla únicamente los índices de aquellos nombres de 
    la lista a continuación, que empiecen con la letra “M”:
    lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", 
                     "Marta", "Darío", "Emiliano", "Melisa"]

    Resultado esperado: 0, 2, 5, 8
"""

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i)
