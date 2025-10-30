""" En este ejercicio practicaremos la indexacion y el slicing de cadenas de texto (strings) en Python."""

texto = "Aprendiendo Python es divertido"
print(f"La cadena es: '{texto}'\n")

# Slicing para obtener subcadenas
subcadena1 = texto[0:12]
print(f"Subcadena desde el índice 0 hasta el 11: '{subcadena1}'")

subcadena2 = texto[13:19]
print(f"Subcadena desde el índice 13 hasta el 18: '{subcadena2}'")

subcadena3 = texto[20:]
print(f"Subcadena desde el índice 20 hasta el final: '{subcadena3}'")

subcadena4 = texto[:12]
print(f"Subcadena desde el inicio hasta el índice 11: '{subcadena4}'")

subcadena5 = texto[:]
print(f"Subcadena completa: '{subcadena5}'")    

# Slicing con paso
subcadena6 = texto[::2]
print(f"Subcadena con paso 2: '{subcadena6}'")

subcadena7 = texto[1::2]
print(f"Subcadena desde el índice 1 con paso 2: '{subcadena7}'")

subcadena8 = texto[::-1]
print(f"Subcadena invertida: '{subcadena8}'")

subcadena9 = texto[10:0:-1]
print(f"Subcadena desde el índice 10 hasta el 1 invertida: '{subcadena9}'") 

subcadena10 = texto[20:13:-1]
print(f"Subcadena desde el índice 20 hasta el 14 invertida: '{subcadena10}'")



