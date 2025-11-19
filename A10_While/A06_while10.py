""" Menú de Opciones Interactivo
    Objetivo: Mostrar un menú (ej. 1. Sumar, 2. Restar, 3. Salir) y pedir al usuario que seleccione una opción. 
    El programa debe seguir mostrando el menú hasta que elija "Salir".
    Mecanismo: Un while que se mantiene activo mientras la elección del usuario no sea la opción de salida."""

opcion = None                                           # Inicializa la variable para almacenar la opción del usuario
while opcion != '3':                                    # Continúa el ciclo hasta que el usuario elija la opción de salir
    print("Menú de Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    opcion = input("Selecciona una opción (1-3): ")     # Solicita al usuario que seleccione una opción

    if opcion == '1':
        num1 = float(input("Ingresa el primer número para sumar: "))
        num2 = float(input("Ingresa el segundo número para sumar: "))
        print(f"La suma es: {num1 + num2}")
    elif opcion == '2':
        num1 = float(input("Ingresa el primer número para restar: "))
        num2 = float(input("Ingresa el segundo número para restar: "))
        print(f"La resta es: {num1 - num2}")
    elif opcion == '3':
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 3.")

