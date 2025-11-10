""" Uso de continue en un ciclo for
    el uso de continue en los ciclos de Python es un salto para pasar a la siguiente iteración del ciclo, 
    sin terminar de ejecutar el código que viene después en la iteración actual.

    Uso de continue
    El continue solo se usa dentro de los ciclos (for o while) y su función principal es:

    1. Detener la ejecución del bloque de código actual.
    2. Volver al inicio del ciclo.
    3. Comenzar la siguiente repetición (o "iteración") del ciclo.
"""


print("Iterando sobre un rango de números del 1 al 10, saltando los números pares:")
for numero in range(1, 11):
    if numero % 2 == 0:
        continue  # Saltar los números pares
    print(numero)   
