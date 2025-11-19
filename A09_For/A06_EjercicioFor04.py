""" Crear un programa que solcite al usuario una cadena de texto y
    el programa cuente cuantas vocales tiene la cadena.
    Se debe usar un ciclo for para recorrer la cadena y una estructura condicional
    para verificar si cada caracter es una vocal."""


cadena = input("Ingrese una cadena de texto: ")     # Solicita al usuario una cadena de texto
cadena = cadena.lower()                             # Convierte la cadena a minúsculas para simplificar la verificación

contador_vocales = 0                                # Inicializa el contador de vocales en 0
vocales =  ['a', 'e', 'i', 'o', 'u']                # Define una lista con todas las vocales (solo en minúsculas)

for caracter in cadena:                             # Itera sobre cada caracter en la cadena ingresada
    if caracter in vocales:                         # Verifica si el caracter es una vocal
        contador_vocales += 1                       # Incrementa el contador de vocales

                                                    # Imprime el número total de vocales
print(f"La cadena ingresada tiene {contador_vocales} vocales.")  
