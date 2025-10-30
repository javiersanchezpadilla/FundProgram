""" Cadena a Lista: Pide al usuario que ingrese una serie de elementos separados 
    por comas (ej. "rojo,verde,azul"). Imprime el resultado de convertir esa cadena a una lista."""

elementos = input("Escribe una serie de elementos separados por comas (ej. 'rojo,verde,azul'): ")
lista_elementos = elementos.split(",")
print("La lista de elementos es:", lista_elementos)
