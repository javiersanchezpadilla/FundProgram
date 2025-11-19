""" Crear un programa que solcite al usuario una cadena de texto y
    el programa cuente cuantas vocales tiene la cadena.
    Se debe usar un ciclo for para recorrer la cadena y una estructura condicional
    para verificar si cada caracter es una vocal."""


cadena = input("Ingrese una cadena de texto: ")     # Solicita al usuario una cadena de texto
contador_vocales = 0                                # Inicializa el contador de vocales en 0

for caracter in cadena:                             # Itera sobre cada caracter en la cadena ingresada
    if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u' or \
         caracter == 'A' or caracter == 'E' or caracter == 'I' or caracter == 'O' or caracter == 'U':  # Verifica si el caracter es una vocal
        contador_vocales += 1                       # Incrementa el contador de vocales

print(f"La cadena ingresada tiene {contador_vocales} vocales.")  # Imprime el número total de vocales
