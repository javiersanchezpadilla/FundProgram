""" Se requiere que la función ahora no revise un valor, que revise toda una lista 
    y que busque si algún elemento es de tres cifras.

"""

def revisa_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False


resultado = revisa_3_cifras([22, 33, 325, 23])
print(resultado)
