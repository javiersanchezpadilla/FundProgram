""" Binario a Decimal: Pide al usuario que ingrese una cadena de 8 bits 
    (ej. 10110011). Convierte esta cadena a su valor entero decimal usando 
    la función int() con el argumento base."""

bits = input("Escribe una cadena de 8 bits (ej. 10110011): ")
numero_decimal = int(bits, 2)
print(f"La cadena de bits {bits} en decimal es {numero_decimal}.")  
