""" Uso del for mediante el uso de rangos numéricos.
    La función range() genera una secuencia de números enteros,
    que puede ser utilizada para iterar en un ciclo for.

    Cuando usamos range(n), se genera una secuencia desde 0 hasta n-1.
    También podemos especificar un inicio y un fin usando range(inicio, fin),
    que genera una secuencia desde 'inicio' hasta 'fin-1'.
    
    RECORDEMOS QUE EL VALOR FINAL NO SE INCLUYE EN LA SECUENCIA.
    """

print("Iterando sobre un rango de números del 0 al 4:")
for numero in range(5):
    print(numero)   


print("\nIterando sobre un rango de números del 3 al 15:")
for numero in range(3, 16):
    print(numero)

