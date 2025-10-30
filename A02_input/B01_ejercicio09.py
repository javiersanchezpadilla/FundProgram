""" Conversión Múltiple: Pide un número decimal (flotante). Imprime tres líneas: 
    el número original, el número convertido a entero (truncado), y el número convertido a cadena."""

numero_decimal = input("Escribe un número decimal: ")
numero_truncado = int(float(numero_decimal))
print("Número original (flotante): " + numero_decimal)
print("Número truncado (entero): " + str(numero_truncado))
print("Número como cadena: " + str(numero_decimal))

# Alternativa usando solo una línea de código
# print("Número original (flotante): " + (numero_decimal := input("Escribe un número decimal: ")) + "\nNúmero truncado (entero): " + str(int(float(numero_decimal))) + "\nNúmero como cadena: " + str(numero_decimal))  