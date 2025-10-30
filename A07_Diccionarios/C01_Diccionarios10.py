""" Eliminar elementos en un diccionario
    Eliminar y Obtener el Valor: 
    
    pop()

    El método pop() elimina un par de llave-valor y, a diferencia de del, devuelve el valor 
    del elemento que fue eliminado. Esto es útil si necesitas usar ese valor antes de desecharlo.
"""
inventario = {
    "manzana": 150,
    "pera": 200,
    "kiwi": 50
}

                                                    # Eliminar "kiwi" y guardar su cantidad
cantidad_eliminada = inventario.pop("kiwi")         # recordar que "kiwi" es la llave y el valor 50

                                                    # Salida: Kiwi eliminado. Cantidad: 50
print(f"Kiwi eliminado. Cantidad: {cantidad_eliminada}")

print(inventario)                                   # Salida: {'manzana': 150, 'pera': 200}
