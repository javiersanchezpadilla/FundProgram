""" Crea una función llamada “lanzar_moneda” que devuelva el resultado de lanzar una moneda 
    (al azar) dicha función debe poder devolver los resultados “aguila” o “Sol” y no debe 
    recibir argumentos para funciones.
    Crea una segunda función llamada “probar_suerte”, que tome dos argumentos, el primero 
    debe ser el resultado del lanzamiento de la moneda el segundo argumento será una lisa 
    de números cualquiera (debes crear una lista con valores  y llamarla “lista_numeros”,

    Si se le proporciona una “AGUILA”, debe mostrar el mensaje al usuario “La lista se autodestruira” 
    y eliminarla (devolviendo como lista vacia []).
    Si se le proporciona una “SOL”, debe imprimir en pantalla “La lista fue salvada” y devolver la 
    lista intacta.

    Puede usar el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.

"""

from random import randint, choice


aguila_o_sol = {1:'Aguila', 2:'Sol'}
lista_numeros = [1,2,2,4,5,7,8,5,4,6,89,11,5,4,6]


def lanzar_moneda():
    # genera un numero al azar entre 1 y 2 y devuelve aguila o sol
    return aguila_o_sol[randint(1,2)]

def probar_suerte(monedaParam, listaParam):
    if monedaParam == 'Aguila':
        print('La lista se autodestruira')
        listaParam.clear()
    else:
        print('La lista fue salvada')
    return listaParam


monedaLanzada = lanzar_moneda()
probar_suerte(monedaLanzada, lista_numeros)
print(lista_numeros)
