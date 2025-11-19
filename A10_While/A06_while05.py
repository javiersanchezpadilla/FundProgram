""" Uso de break y continue
    Al igual que en los ciclos for, se pueden usar las instrucciones break y continue dentro de un ciclo while.
        - break: Termina el ciclo inmediatamente, sin importar si la condición sigue siendo True.
        - continue: Salta a la siguiente iteración del ciclo, reevaluando la condición.
"""

numero = 0

while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue        # Saltar los números pares
    print(numero)
