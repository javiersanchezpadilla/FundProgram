""" while en Python como una instrucción para repetir un bloque de código mientras una condición específica sea verdadera.
    A diferencia del ciclo for que itera sobre una secuencia finita, el ciclo while es un ciclo condicional. Su duración 
    no depende del tamaño de una lista, sino de si se sigue cumpliendo una condición.

    Concepto Clave: Ejecución Condicional
    El ciclo while sigue una lógica simple de "mientras esto sea verdad, sigue haciendo esto".

    1. Sintaxis Básica
    La estructura siempre tiene esta forma:

            while condicion_a_evaluar:
                # Bloque de código a repetir
                # Es VITAL que este bloque cambie algo relacionado con la condición
                # para que en algún momento se detenga.

    Donde:
        while: Indica el inicio del ciclo condicional.
        condicion_a_evaluar: Es una expresión que debe resultar en Verdadero (True) o Falso (False).
                                Si es True, el código se ejecuta.
                                Si es False, el ciclo se detiene inmediatamente."""


print("Ejemplo de uso del ciclo while para imprimir una secuencia del 1 hasta el 10")

numero = 1
while numero <= 10:
    print(numero)
    numero += 1             # Actualizamos el número para evitar un ciclo infinito
    # 💀💀💀💀💀

""" IMPORTANTE: Evitar Ciclos Infinitos. Es crucial que el bloque de código dentro del while modifique la 
    condición de alguna manera. Si la condición nunca cambia a False, el ciclo continuará indefinidamente, 
    lo que puede causar que el programa se congele o consuma demasiados recursos."""

