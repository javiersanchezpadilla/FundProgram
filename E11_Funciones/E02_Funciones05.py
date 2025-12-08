""" Crea una función “todos_positivos” que devuelva true si todos los valors de una lista 
    son positivos y false si al menos uno de los valores es negativo. 
    crea una lista llamada “lista_numeros” con valores positivos y negativos.
"""

lista_numeros = [1,2,3,4,5,1,-10]

def todos_positivos(parametroLista):
    resultado = True
    for n in parametroLista:
        if n < 0:
            resultado = False
    return resultado

print(todos_positivos(lista_numeros))
