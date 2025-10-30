""" Potencia: Pide un número base y un exponente (entero). 
    Calcula e imprime el resultado de elevar la base al exponente (operador **)."""

base = input("Escribe la base (número): ")
exponente = input("Escribe el exponente (entero): ")
potencia = float(base) ** int(exponente)
print(f"{base} elevado a la {exponente} es {potencia}.")    

