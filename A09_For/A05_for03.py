""" Ejemplo del uso de un bucle for sobre una cadena de texto.
    En este ejemplo la cadena es una secuencia numérica representada como texto.
    """

print("\nIterando sobre otra cadena de texto:")

cadena = "123456789"
for digito in cadena:       # Recordar que en este momento digito es una cadena de texto
    digito = int(digito)    # Convertimos la cadena a numero entero
    print(digito + 10)


