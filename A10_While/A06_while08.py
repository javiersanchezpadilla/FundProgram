""" Suma Acumulativa
    Objetivo: Pedir números al usuario repetidamente y sumarlos, deteniéndose solo cuando el usuario introduce el número cero (0).
    Mecanismo: Un while True que se rompe con break dentro de un if cuando el número ingresado es 0."""

suma = 0                                                                        # Inicializa la variable para almacenar la suma acumulativa
while True:
    numero = float(input("Ingresa un número para sumar (0 para terminar): "))   # Solicita un número al usuario
    if numero == 0:
        break                                                                   # Sale del ciclo si el número es 0
    suma += numero                                                              # Suma el número ingresado a la suma acumulativa

print(f"La suma total es: {suma}")                                              # Muestra la suma total acumulada
