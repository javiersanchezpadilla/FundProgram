"""Ejemplo de uso del ciclo while para imprimir cada letra de una cadena:
    En cada iteración se imprime una letra de la cadena hasta recorrer todas las letras."""


print("Ejemplo de uso del ciclo while para imprimir cada letra de una cadena:")
cadena = "Python es un lenguaje de programación"

indice = 0

while indice < len(cadena):
    print(cadena[indice])
    indice += 1                 # Actualizamos el índice para evitar un ciclo infinito 
