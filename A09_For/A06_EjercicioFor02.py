""" Crear un programa que solcite al usuario una cadena de texto y
    el programa cuente cuantas vocales tiene la cadena.
    Se debe usar un ciclo for para recorrer la cadena y una estructura condicional
    para verificar si cada caracter es una vocal."""


cadena = input("Ingrese una cadena de texto: ")     # Solicita al usuario una cadena de texto
cadena = cadena.lower()                             # Convierte la cadena a minúsculas para simplificar la verificación
contador_vocales = 0                                # Inicializa el contador de vocales en 0

for caracter in cadena:                             # Itera sobre cada caracter en la cadena ingresada
                                                    # Verifica si el caracter es una vocal
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':  
        contador_vocales += 1                       # Incrementa el contador de vocales

print(f"La cadena ingresada tiene {contador_vocales} vocales.")  # Imprime el número total de vocales
