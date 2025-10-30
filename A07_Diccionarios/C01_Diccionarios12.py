""" Eliminar todos los elementos del diccinario y dejarlo vacio

    clear()

    El método clear() elimina todos los elementos del diccionario, dejándolo vacío, 
    pero la estructura del diccionario sigue existiendo.
"""

configuracion = {"tema": "oscuro", "fuente": 12, "notificaciones": True}

# 1. Eliminar todo el contenido
configuracion.clear()

print(configuracion)            # Salida: {}

