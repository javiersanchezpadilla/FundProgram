""" Se requiere que la función ahora no revise un valor, que revise toda una lista 
    y que busque si algún elemento es de tres cifras, pero además se requiere que 
    esos números que cumplan que se almacenen en una lista y que sea regresada esa lista.
    Resultado esperado: [325, 213]
"""

def revisa_3_cifras(lista):
    listaRetorno = []
    for n in lista:
        if n in range(100,1000):
            listaRetorno.append(n)
    return listaRetorno

resultado = revisa_3_cifras([22, 33, 325, 213])
print(resultado)
