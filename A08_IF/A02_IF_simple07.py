""" Nivel Avanzado (Lógica Anidada y Conversión)
    Estos ejercicios requieren casting de tipos, operadores complejos o sentencias 
    if anidadas (un if dentro de otro if).

    Ejercicio 7: Validación de Clave y Longitud (Anidado)
    Pide al usuario que ingrese una clave numérica de 4 dígitos (como texto).
    Usa un if externo para comprobar si la longitud de la cadena ingresada es exactamente 4.
    Si la longitud es correcta, usa un if anidado para verificar si la clave, una vez convertida 
    a número entero, es igual a 1234. 
    Si ambas condiciones se cumplen, imprime: "Clave Maestra Aceptada".
 """

# debemos ingresar una clave numerica como texto (por eso no se hara el casting a entero int())
clave = input("Ingrese la clave nuemrica: ")

if len(clave) == 4:
    if int(clave) == 1234:
        print("Clave maestra aceptada")
