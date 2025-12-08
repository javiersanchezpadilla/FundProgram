""" Funcion para verificar si un valor es de tres cifras
"""

def revisa_3_cifras(numero):
    return numero in range(100,1000)

resultado = revisa_3_cifras(652)
print(resultado)

