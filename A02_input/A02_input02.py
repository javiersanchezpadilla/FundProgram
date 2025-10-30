""" El siguiente ejercicio muestra como convertir entre el tipo de dato
    cadena a un valor entero.
    Recordar que lo que queremos es que en lugar de concatenar dos cadenas
    nos devuelva la operacion aritmetica
    """

# FORMA 1 de convertir los valores

numero1 = input("Valor uno: ")  # capturamos el primer valor
print(type(numero1))            # Podemos verificar que la variable es una cadena
numero1 = int(numero1)          # Hacemos la conversion de cadena a entero
print(type(numero1))            # verficamos la coversion del tipo de dato

numero2 = input("Valor dos: ")  # Capturamos el segundo valor
print(type(numero2))            # verificamos que la variable es una cadena
numero2 = int(numero2)          # Convertimos la variable de cadena a entero
print(type(numero2))            # verificamos la conversion del tipo de dato


print(f"El tipo de dato de la variable numero1 es {type(numero1)}")
print(f"El tipo de dato de la variable numero2 es {type(numero2)}")

print("El resultado de la suma de cadenas nos da {} (lo cual ya es una suma)".format(numero1 + numero2))
