""" Nivel Muy Sencillo (Solo if Básico)
    En este nivel, un simple if es suficiente para validar y mostrar un resultado.

    Ejercicio 3: Descuento Fijo
    Pide al usuario el precio de un artículo. Usa un if para calcular e imprimir un 
    descuento de $50 pesos y el precio final solo si el precio original es mayor a 
    $200. Si el precio no cumple la condición, el programa simplemente no debe imprimir nada.
"""

# Capturamos el precio y lo covertimos a numero flotante
precio = float(input('Precio del articulo: '))

if precio > 200:
    precio = precio - 50
    print("\nSe aplico un descuento de $50 pesos")
    print(f"El precio a pagar es {precio}")
