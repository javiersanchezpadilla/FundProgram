""" Nivel Medio (Múltiples if Independientes)
    Aquí se requiere usar varios if independientes o el uso de operadores lógicos (and, or) 
    para ejecutar diferentes acciones basadas en una misma entrada.

    Ejercicio 4: Alerta de Rangos
    Pide al usuario un número entero.
    Usa un if para mostrar "Alerta Baja" solo si el número es menor a 20.
    Usa otro if para mostrar "Alerta Alta" solo si el número es mayor a 80.
    Si el número está entre 20 y 80, no debe aparecer ningún mensaje.
"""

numero = int(input("Dame un numero entero "))

if numero < 20:
    print("Alerta baja, el numero es menor a 20")

if numero > 80:
    print("Alerta alta, el numero es mayor a 80")
