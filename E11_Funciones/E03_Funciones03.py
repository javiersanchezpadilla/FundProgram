""" Crea una función llamada “reducir_lista()” que tome una lista de números (lista_numeros) 
    como argumento y devuelva la misma lista, pero eliminando duplicados (dejando uno solo 
    de los números si hay repetidos) y eliminando el valor más alto, el orden de los elementos 
    puede modificarse, por ejemplo para [1, 2, 15, 7, 2] puede quedar [1, 2, 7]
    crea una función llamada “promedio” que pueda recibir como argumento la lista devuelta 
    por la anterior función y que calcule el promedio de los valores de la misma. 
    Debe devolver el resultado sin imprimirlo.

"""

lista_numeros = [1,2,3,4,5,3,2,3,4,1,2,3,4,45,33,22,11,988,33,988,988,988]
lista_resultado = []

def reducir_lista(listaParam):
    largo_lista = len(listaParam) - 1
    listaParam.sort()

    while largo_lista >0:
        if listaParam[largo_lista - 1] == listaParam[largo_lista]:
            listaParam.pop(largo_lista)
        largo_lista -= 1
    # elimna el ultimo elemento de la lista
    listaParam.pop(-1)
    return listaParam


def promedio(listaParam):
    elementos = len(listaParam)
    suma = 0
    for n in listaParam:
        suma += n
    promedio = suma / elementos
    return promedio


lista_resultado = reducir_lista(lista_numeros)
print(lista_resultado)
valor = promedio(lista_resultado)
print(valor)
