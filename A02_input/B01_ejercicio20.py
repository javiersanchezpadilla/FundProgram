""" Recolección de Datos: Pide el nombre de un amigo y su edad. Luego, pide tu nombre y tu edad. 
    Imprime los cuatro datos usando la función print() con el argumento `sep='"""

nombre_amigo = input("¿Cuál es el nombre de tu amigo? ")
edad_amigo = input("¿Cuál es la edad de tu amigo? ")
tu_nombre = input("¿Cuál es tu nombre? ")
tu_edad = input("¿Cuál es tu edad? ")
print(nombre_amigo, edad_amigo, tu_nombre, tu_edad, sep=" - ")
