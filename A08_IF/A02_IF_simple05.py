""" Nivel Medio (Múltiples if Independientes)
    Aquí se requiere usar varios if independientes o el uso de operadores lógicos (and, or) 
    para ejecutar diferentes acciones basadas en una misma entrada.
    
    Ejercicio 5: Requisitos de Acceso
    Pide al usuario su edad y si tiene una membresía (ingresar 'S' para Sí, 'N' para No). 
    Usa un solo if con el operador and para imprimir: "Acceso concedido" solo si la persona tiene 18 años o más Y tiene membresía 'S'.
"""

edad = int(input("Dame tu edad: "))
membresia = input("Cuenta con menbresia (S/N) ?")
membresia = membresia.upper()

if edad >= 18 and membresia == "S":
    print("Acceso concedido.")
