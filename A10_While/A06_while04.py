""" Uso de break y continue
    Al igual que en los ciclos for, se pueden usar las instrucciones break y continue dentro de un ciclo while.
        - break: Termina el ciclo inmediatamente, sin importar si la condición sigue siendo True.
        - continue: Salta a la siguiente iteración del ciclo, reevaluando la condición.
"""

contador = 0

while True:
    print(contador)
    if contador >= 5:
        break  # Salir del ciclo cuando el contador alcanza 5
    contador += 1
