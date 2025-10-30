""" Valor Booleano de una Cadena: Pide al usuario que ingrese una frase. 
    Imprime su representación booleana (True o False). 
    Luego, pide una frase vacía y muestra su valor booleano."""

frase = input("Escribe una frase: ")
valor_booleano = bool(frase)
print(f"La frase '{frase}' tiene un valor booleano de {valor_booleano}.")

frase_vacia = input("Escribe una frase vacía (simplemente presiona Enter): ")
valor_booleano_vacio = bool(frase_vacia)
print(f"La frase vacía tiene un valor booleano de {valor_booleano_vacio}.")

