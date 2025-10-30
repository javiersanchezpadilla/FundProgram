""" Nivel Avanzado (Lógica Anidada y Conversión)
    Estos ejercicios requieren casting de tipos, operadores complejos o sentencias 
    if anidadas (un if dentro de otro if).
    
    Ejercicio 8: Beca Condicional (Doble Validación)
    Pide al usuario su promedio de notas (decimal) y su nivel socioeconómico (ingresar un número del 1 al 3).
    Usa un if para verificar si el promedio es mayor o igual a 9.0.
    Usa un segundo if independiente para verificar si el nivel socioeconómico es igual a 1.
    Usa un tercer if que combine las dos condiciones anteriores con and para imprimir: "¡Beca Completa Otorgada!".
"""

promedio = int(input("Favor de proporcionar su promedio (0 a 10): "))
nivel_socioeconomico = int(input("Indique su nivel socioeconomico (1,2 o 3): "))

if promedio >= 9:
    print(f"Tiene un promedio mayor o igual de 9 = {promedio} de promedio")
    
if nivel_socioeconomico == 1:
    print("El nivel socioeconomico es 1")

if promedio >= 9 and nivel_socioeconomico == 1:
    print("\n")                                     # Imprimimos una linea en blanco
    print('*' * 32)                                 # Imprimimos el asterisco 32 veces
    print("**  ¡Beca Completa Otorgada!  **")       # Imprimimos el texto 
    print('*' * 32)                                 # Imprimimos el asterisco 32 veces
