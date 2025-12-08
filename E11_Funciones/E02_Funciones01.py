""" CREA UNA FUNCIÓN LLAMADA invertir_palabra, QUE TOME LOS CARACTERES DE UNA 
    PALABRA DADA COMO ARGUMENTO, INVIERTA EL ORDEN DE SUS CARACTERES Y LOS 
    DEVUELVA DE ESE MODO Y EN MAYÚSCULAS.
    POR EJEMPLO “Python” DEBE DEVOLVER “NOHTYP”
    TAMBIÉN DEBERÁ CREAR UNA VARIABLE LLAMADA “palabra” QUE CONTENGA EL STRING 
    QUE TU PREFIERAS PARA SUMINISTRARLE COMO ARGUMENTO A LA FUNCIÓN CREADA. 
    SE DEBEN USAR LOS MÉTODOS DE STRING YA VISTOS.

    RESULTADO ESPERADO: NOHTYP
"""

palabra = 'Python'

def invertir_palabra(dato):
    copiatxt = dato.upper()
    lista = list (a for a in copiatxt)
    lista.reverse()
    copiatxt = ''.join(lista)
    return copiatxt

invertir_palabra(palabra)
print(invertir_palabra(palabra))
