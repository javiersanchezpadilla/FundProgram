""" Nivel Muy Sencillo (Solo if Básico)
    En este nivel, un simple if es suficiente para validar y mostrar un resultado.

    Ejercicio 2: Revisión de Inventario Mínimo
    Pide al usuario la cantidad de un producto. Usa un if para mostrar el mensaje: 
    "¡Necesitas reponer stock!" solo si la cantidad es menor que 10.
"""

cantidad = input('Cual es la cantidad del producto? ')

if int(cantidad) < 10:
    print("¡Necesitas reponer stock!")
