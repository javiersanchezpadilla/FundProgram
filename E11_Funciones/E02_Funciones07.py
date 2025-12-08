""" Crea una función “cantidad_pares” que cuente la cantidad de números pares que existen 
    en una lista “lista_numeros” y devuelva el resultado de dicha lista.


"""
lista_numeros = [1,2,3,4,5,1,5,6,7,9, -1000]

def cantidad_pares(listaParametro):
    pares = 0
    for n in listaParametro:
        if n % 2 == 0:
            pares += 1
    return pares

print(cantidad_pares(lista_numeros))    # Resultado 4


