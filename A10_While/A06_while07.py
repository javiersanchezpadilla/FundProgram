""" Contador Regresivo
    Objetivo: Iniciar un contador desde un número dado por el usuario (ej. 10) hasta llegar a 1, imprimiendo cada paso.
    Mecanismo: Un while que se ejecuta mientras el número sea mayor que 0. La variable debe decrementar dentro del ciclo."""


numero = int(input("Ingresa un número para iniciar el contador regresivo: "))
while numero > 0:
    print(numero)
    numero -= 1         # Decrementa el número en 1 en cada iteración

print("¡Despegue!")

