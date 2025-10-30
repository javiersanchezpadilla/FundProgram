""" Definición de Tupla

    Una tupla es un contenedor ordenado que se utiliza para agrupar una colección de elementos. 
    Se define encerrando los elementos entre paréntesis (), separados por comas. 
    
    Características Clave: La Inmutabilidad
    La característica que define a una tupla y la diferencia de la lista es la inmutabilidad:
    
    Característica          Tupla                                               Lista
    --------------------------------------------------------------------------------------------------
    Ordenada                Sí (el orden se mantiene).                          Sí.
    Mutable                 No (una vez creada, no se puede modificar,          Sí (se puede modificar 
                            añadir o eliminar elementos).                       libremente).
    Sintaxis                Paréntesis ()                                       Corchetes []

    Esto significa que, si bien puedes acceder a cualquier elemento de una tupla, no puedes cambiar 
    su valor, ni suprimirlo, ni añadir nuevos elementos a esa misma tupla.
                            
"""

# Tupla de coordenadas (las coordenadas de un punto no cambian)
punto_fijo = (10, 25)
print(type(punto_fijo))
print(punto_fijo)

# Tupla con diferentes tipos de datos
configuracion = ("servidor_a", 8080, True)
print(type(configuracion))
print(configuracion)

# Tupla de un solo elemento (¡la coma es crucial!)
elemento_unico = (5,)
print(type(elemento_unico))
print(elemento_unico)
