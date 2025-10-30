""" Casting entre tipos de datos.
    Podemos convertir entre los distintos tipos de datos de momento trabajaremos la
    conversion entre enteros, cadenas y flotantes"""

# una cadena la podemos convertir en numero, si y solo si los valores
# contenidos dentro de la cadena correspondan a valores numericos
cadena = "1000"     
print(f"El tipo actual de dato de la variable cadena {cadena} es {type(cadena)}")

# convertimos el dato a entero
cadena = int(cadena)
print(f"El tipo actual de dato de la variable cadena {cadena} es {type(cadena)}")

# podemos conertir a flotante (note que le aumenta el punto y el cero al numero)
cadena = float(cadena)
print(f"El tipo actual de dato de la variable cadena {cadena} es {type(cadena)}")

# actualmente el valor de la variable cadena es flotante ahora lo vamos a convertir a cadena
cadena = str(cadena)
print(f"El tipo actual de dato de la variable cadena {cadena} es {type(cadena)}")


print("\n\nCONVERSION ENTRE SISTEMAS NUMERICOS\n")

numero_entero = 59                         # numero en base 10
numero_hexadecimal = hex(numero_entero)
numero_binario = bin(numero_entero)
numero_octal = oct(numero_entero)

print("EL RESULTADO DE LA CONVERSION DEL VALOR 59 ES:")
print(f"{numero_entero} convertido en hexadecimal es {numero_hexadecimal}")
print(f"{numero_entero} convertido a binario es {numero_binario}")
print(f"{numero_entero} convertido a octal es {numero_octal}")

