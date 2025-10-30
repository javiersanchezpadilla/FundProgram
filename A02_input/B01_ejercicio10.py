""" Booleano de un Número: Pide al usuario un número. 
    Conviértelo a booleano y explica si el resultado fue True o False. 
    (Ejemplo: "El número [X] se considera [Y]")."""

numero = input("Escribe un número: ")
booleano = bool(float(numero))  # Convertir a float primero para manejar números decimales
print(f"El número {numero} se considera {booleano}.")

