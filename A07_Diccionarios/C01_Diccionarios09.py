""" Eliminar elementos de un diccinario
    1. Eliminar un Par Específico: 
    
        del()

    La palabra clave del se utiliza para eliminar permanentemente un par de llave-valor 
    del diccionario. Si la llave no existe, causará un error (KeyError).

"""

perfil = {
    "nombre": "Elena",
    "edad": 28,
    "ciudad": "Madrid"
}

                            # 1. Eliminar la llave "edad"
del perfil["edad"] 

print(perfil)               # Salida: {'nombre': 'Elena', 'ciudad': 'Madrid'}
