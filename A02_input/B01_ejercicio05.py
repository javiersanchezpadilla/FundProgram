""" Identificador: Pide al usuario su nombre y su edad. Imprime la frase 
    "ID: [Nombre] - [Edad]", donde el nombre esté en mayúsculas."""

nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuál es tu edad? ")
print("ID: " + nombre.upper() + " - " + edad)

# Alternativa usando solo una línea de código
# print("ID: " + input("¿Cuál es tu nombre? ").upper() + " - " + input("¿Cuál es tu edad? "))   

# Alternativa usando f-strings (Python 3.6+)
# print(f"ID: {input('¿Cuál es tu nombre? ').upper()} - {input('¿Cuál es tu edad? ')}")

# Alternativa usando format()
# print("ID: {} - {}".format(input("¿Cuál es tu nombre? ").upper(), input("¿Cuál es tu edad? ")))
