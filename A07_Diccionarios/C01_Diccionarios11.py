""" Eliminar elementos en un diccionario
    Eliminar y Obtener el Valor: 
    
    pop()

    El método pop() elimina un par de llave-valor y, a diferencia de del, devuelve el valor 
    del elemento que fue eliminado. Esto es útil si necesitas usar ese valor antes de desecharlo.

    Pero, ¿qué sucede si el elemento a eliminar no existe?
    Respuesta: se obtiene un error.
    Alternativa: para evitar el error podermos especificar que valor retornar en caso de no 
    encontrar el valor a borrar.

"""
inventario = {
    "manzana": 150,
    "pera": 200,
    "kiwi": 50
}

print(inventario) 
                                                    # Intenta eliminar "uva", que no existe
cantidad = inventario.pop("uva", 0)                 # El 0 es el valor por defecto si no se encuentra la llave

print(f"Cantidad de uva: {cantidad}")               # Salida: Cantidad de uva: 0 (No hay error)
                                                    # De esta forma evitamos el error