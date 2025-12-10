""" El ámbito de las variables (o scope en inglés) en Python define la parte del código donde una 
    variable es accesible y válida. Es decir, dónde puede ser encontrada y utilizada por el intérprete de Python.

    El concepto más importante para entender el ámbito es la regla LEGB, que determina el orden en el que Python 
    busca una variable.

    La Regla LEGB (Local, Enclosing, Global, Built-in)
    Python busca una variable en estos cuatro niveles de ámbito, siempre en este orden:

    1. L - Local (Ámbito más Interno). Es el ámbito más pequeño y limitado. Una variable es local si es definida 
    dentro de una función o una clase.

    Accesibilidad: Solo es accesible dentro de esa función.
"""

def mi_funcion():
    x = 10                      # X es local a mi_funcion
    print(x) 

mi_funcion()                    # Imprime 10
# print(x)                      # Error: NameError, x no está definida fuera de la función.

