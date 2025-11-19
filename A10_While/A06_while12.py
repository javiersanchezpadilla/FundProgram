""" Cajero Automático Simple
    Objetivo: Simular un saldo inicial. Dentro de un ciclo while, permitir al usuario realizar 
    depósitos y retiros. El ciclo se detiene si el usuario intenta retirar una cantidad mayor a su saldo.
    Mecanismo: Un while que permite transacciones y un if que activa un break si la condición de saldo se viola."""

saldo = 1000.0  # Saldo inicial del usuario

while True:
    print(f"\nSaldo actual: ${saldo:.2f}")
    accion = input("¿Deseas (d)epositar, (r)etirar o (s)alir? ").lower()

    if accion == 'd':
        cantidad = float(input("Ingresa la cantidad a depositar: $"))
        if cantidad > 0:
            saldo += cantidad
            print(f"Has depositado ${cantidad:.2f}. Nuevo saldo: ${saldo:.2f}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    elif accion == 'r':
        cantidad = float(input("Ingresa la cantidad a retirar: $"))
        if cantidad > saldo:
            print("Fondos insuficientes para realizar el retiro.")
        elif cantidad > 0:
            saldo -= cantidad
            print(f"Has retirado ${cantidad:.2f}. Nuevo saldo: ${saldo:.2f}")
        else:
            print("La cantidad a retirar debe ser positiva.")

    elif accion == 's':
        print("Gracias por usar el cajero automático. ¡Hasta luego!")
        break

    else:
        print("Acción no válida. Por favor, elige 'd', 'r' o 's'.")

