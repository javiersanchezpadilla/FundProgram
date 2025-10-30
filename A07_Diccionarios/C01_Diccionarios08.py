""" PAra conocer las llaves de un diccionario
    En este ejercicio usaremos los siguiente métodos

    keys()      Muestra una lista con los nombres de las llaves de los elementos de un diccionario.
    values()    Muestra una lista con los valores contenidos en un diccionario.
    items()     Muestra una lista los elementos de un diccionario
"""

dic = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}

print(dic)                  # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(dic.keys())           # dict_keys([1, 2, 3, 4, 5])

                            # Si requiero solo conocer los valores contenidos dentro del diccionario
print(dic.values())         # dict_values(['a', 'b', 'c', 'd', 'e'])

                            # Si quiero conocer la composicion de un diccionario
print(dic.items())          # Muestra una lista de tuplas donde cada tupla contiene la llave y valor
                            # dict_items([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')])
