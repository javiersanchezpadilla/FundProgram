""" Nivel Avanzado (Lógica Anidada y Conversión)
    Estos ejercicios requieren casting de tipos, operadores complejos o sentencias 
    if anidadas (un if dentro de otro if).
    
    Ejercicio 9: Rango Exclusivo
    Pide al usuario un número entero. Usa un único if con un operador lógico (and o or) para imprimir: 
    "El número NO está en el rango seguro (entre 10 y 50)" solo si el número es menor de 10 O si es mayor de 50.
"""

numero = input("Favor de proporcionar un valor entero: ")
numero = int(numero)

if numero < 10 or numero > 50:
    print("El número NO está en el rango seguro (entre 10 y 50)")

# Otra forma de resolver el problema es considerando el rango seguro
# si el resultado de la evaluacion (numero >= 10 and numero <= 50) es verdadera, al momento
# de negarla se hace falsa y en caso de que el valor no caiga en ese rango al ser false
# y negarla el resultado se hace verdadero
if not (numero >= 10 and numero <= 50):
    print("El número NO está en el rango seguro (entre 10 y 50) con la segunda valdiación")


# Otra forma de resolver el problema
# la expresion numero >= 10 and numero <= 50 se puede simplificar de la siguiente manera:
# numero >= 10  es lo mismo que 10 <= numero (solo la invertimos)
# numero <= 50 queda igual entonces como la expresion contesmpla un AND se puede escribir
if not (10 <= numero <= 50):
    print("El número NO está en el rango seguro (entre 10 y 50) con la tercer valdiación")

