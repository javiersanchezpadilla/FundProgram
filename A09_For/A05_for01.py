""" La instrucción for en Python es fundamentalmente un iterador. Se usa para automatizar tareas repetitivas 
    sobre un conjunto de datos.

    1. Sintaxis Básica
    La estructura siempre tiene esta forma:

            for elemento in secuencia:
                # Bloque de código a repetir
                # 'elemento' toma el valor de cada ítem de la 'secuencia' en cada repetición

    Donde:
            for: Indica el inicio del ciclo.
            elemento: Es una variable temporal que Python crea. En cada repetición del ciclo, esta variable 
            guarda el valor del ítem actual que se está revisando en la secuencia.
            in: Indica que vamos a buscar dentro de una secuencia.
            secuencia: Es la colección de datos (lista, tupla, cadena, etc.) que se va a recorrer.


    Ejemplo del uso de un bucle for sobre una cadena de texto.
    Recordar que las cadenas son elmeentos iterables.
"""

print("Imprimiendo cada letra de la cadena usando un bucle for:")

for letra in "Python es un lenguaje de programación":
    print(letra)
