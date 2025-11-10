""" Ejemplo de uso del ciclo for con la instrucción break.
    En este ejemplo se itera sobre una lista de números y se detiene el ciclo al encontrar un número mayor que 50."""

print("\nIterando sobre una lista de números, deteniéndose al encontrar un número mayor que 50:")

numeros = [10, 25, 40, 55, 70, 85]

for num in numeros:
    if num > 50:
        break  # Salir del ciclo cuando se encuentra un número mayor que 50
    print(num)
