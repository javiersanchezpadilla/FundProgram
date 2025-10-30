""" En este ejercicio practicaremos la indexacion y el slicing de cadenas de texto (strings) en Python."""

mi_cadena = "Python es un lenguaje de programación muy popular"

print(f"La cadena es: '{mi_cadena}'\n")
resultado = mi_cadena.index("lenguaje")
print(f"La palabra 'lenguaje' comienza en el índice: {resultado}")

resultado = mi_cadena.index("p")
print(f"La primera aparición de la letra 'p' está en el índice: {resultado}")

# PAra indicar el inicio de la busqueda, podemos pasar un segundo parametro
resultado = mi_cadena.index("p", resultado)
print(f"La segunda aparición de la letra 'p' está en el índice: {resultado}")

# Podemos usar un tercer parametro para indicar el final de la busqueda
resultado = mi_cadena.index("o", 10, 30)
print(f"La primera aparición de la letra 'o' entre los índices 10 y 30 está en el índice: {resultado}")
