""" Adivina el Número Secreto
    Objetivo: Generar un número aleatorio (ej. entre 1 y 100). Usar un while para que el usuario intente adivinarlo. 
    Si falla, el programa debe indicar si el número secreto es mayor o menor que el intento.
    Mecanismo: Un while que continúa mientras el intento del usuario sea diferente al número secreto."""

import random

numero_secreto = random.randint(1, 100)                                 # Genera un número aleatorio entre 1 y 100
intento = None                                                          # Inicializa la variable intento

while intento != numero_secreto:
    intento = int(input("Adivina el número secreto (entre 1 y 100): ")) # Solicita al usuario que adivine el número
    if intento < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("El número secreto es menor. Intenta de nuevo.")  
    else:
        print("¡Felicidades! Has adivinado el número secreto.")

