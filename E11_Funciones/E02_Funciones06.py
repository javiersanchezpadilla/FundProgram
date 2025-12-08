""" Crea una función “suma_menores” que sume los números de una lista (almacenada en la 
    variable “lista_numeros” siempre y cuando sean mayores a 0 y menores a 1000 y devuelva 
    el resultado de dicha suma.

"""

lista_numeros = [1,2,3,4,5,1,-10, 2000, 3000, -1, -1000]

def suma_menores(listaParametro):
    suma = 0
    for n in listaParametro:
        if (n > 0) and (n < 1000):
            suma += n
    return suma

print(suma_menores(lista_numeros))      # Resultado 16

