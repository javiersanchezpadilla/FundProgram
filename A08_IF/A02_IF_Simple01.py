""" Nivel Muy Sencillo (Solo if Básico)
    En este nivel, un simple if es suficiente para validar y mostrar un resultado.

    Ejercicio 1: Saludo de Bienvenida
    Pide al usuario que ingrese su nombre. Usa un if para imprimir un saludo 
    personalizado solo si el nombre ingresado no está vacío.
"""

print('Saludo de bienvenida')
nombre = input('Dame tu nombre ')

# Si el tamaño de la cadena es cero entonces no hay información, por lo tanto e
# es una cadena vacia.

if len(nombre) > 0:
    print(f'Hola bienvenido {nombre}')
