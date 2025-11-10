""" Ejemplo de uso del ciclo for con la instrucción break.
    En este ejemplo se itera sobre una lista de nombres y se detiene el ciclo al encontrar un nombre específico."""

print("\nIterando sobre una lista de nombres, deteniéndose al encontrar 'Carlos':")

nombres = ['Ana', 'Luis', 'Carlos', 'Marta', 'Jorge']

for nombre in nombres:
    if nombre == 'Carlos':
        break  # Salir del ciclo cuando se encuentra 'Carlos'
    print(nombre)
