""" 2. E - Enclosing (Ámbito Encerrado o No Local)
    Aplica a funciones anidadas (una función dentro de otra). Una variable definida en la función 
    externa es accesible para la función interna.

    Accesibilidad: Accesible para la función interna, pero no es global.
"""

def externa():
    y = 20              # Y es 'enclosing' (encerrada)

    def interna():
        print(y)        # La función interna puede acceder a Y
    
    interna()

externa()               # Imprime 20
