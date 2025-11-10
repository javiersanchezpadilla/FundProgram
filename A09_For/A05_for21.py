""" Uso de continue en un ciclo for
    el uso de continue en los ciclos de Python es un salto para pasar a la siguiente iteración del ciclo, 
    sin terminar de ejecutar el código que viene después en la iteración actual.

    Uso de continue
    El continue solo se usa dentro de los ciclos (for o while) y su función principal es:

    1. Detener la ejecución del bloque de código actual.
    2. Volver al inicio del ciclo.
    3. Comenzar la siguiente repetición (o "iteración") del ciclo.
"""

print("\nIterando sobre un rango de números del 1 al 20, saltando los múltiplos de 3:")
for numero in range(1, 21):
    if numero % 3 == 0:
        continue  # Saltar los múltiplos de 3
    print(numero)   
