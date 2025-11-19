""" La Definición "Estándar" de Python: La ListaEn el uso diario de Python, la estructura fundamental y más 
    flexible que funciona como un arreglo es la Lista (list).

    +-------------------+------------------------------------------+--------------------------------------------+
    |   Característica  |           Listas (list)                  |    Arreglos Típicos (en otros lenguajes)   |
    --------------------+------------------------------------------+--------------------------------------------+
    | Tipo de Elementos | Heterogéneas (Pueden contener            | Homogéneos (Solo pueden contener un        |
    |                   | cualquier tipo de dato: números,         | tipo de dato, ej. solo números enteros).   |
    |                   | cadenas, diccionarios, etc., a la vez).  |                                            |
    |                   |                                          |                                            |
    | Tamaño            | Dinámico (Pueden crecer o encogerse      | Fjo (Su tamaño se define al crearse y      |
    |                   | fácilmente con append(), remove(), etc.).| es difícil o imposible de cambiar).        |
    |                   |                                          |                                            |  
    | Velocidad         | Flexible, pero menos eficiente para      | Muy rápido para cálculos numéricos y       |
    |                   | cálculos numéricos masivos.              | procesamiento de datos.                    |    
    +--------------------+-----------------------------------------+--------------------------------------------+
                        
    En resumen, para el 90% de las tareas de programación general en Python, la lista es tu arreglo.   

    PRINCIPALES DIFERENCIAS ENTRE LOS ARREGLOS Y LAS LISTAS

    +-------------------+----------------------------------------+-------------------------------------+
    | Característica    |      Listas (list)                     |      Arreglos (numpy.array)         |
    +-------------------+----------------------------------------+-------------------------------------+
    | Tipo de datos     | Heterogéneos (cualquier tipo)          | Homogéneos (Sólo un tipo)           |
    |                   |                                        |                                     |
    | Flexibilidad      | Muy alta                               | Media                               |
    |                   |                                        |                                     |
    | Uso de memoria    | Mayor (almacena referencias a objetos) | Menor (almacena datos directamente) |
    |                   |                                        |                                     |
    | Velocidad         | Lenta en cálculos numéricos            | Muy rápida                          |
    |                   |                                        |                                     |
    | Funcionalidades   | Limitadas                              | Muy amplias                         |
    | matemáticas       |                                        |                                     |
    +-------------------+----------------------------------------+-------------------------------------+

""" 

# Las listas son heterogeneas
mi_lista = [1, 2, 'a', 'casa', True, None, ['a', 'b', 'c'], 3.15]

print(mi_lista)

# Son dinamicas, esto quiere decir que pueden crecer o encogerse facilmente
# Agregamos elementos a nuestra lista medinte append()
mi_lista.append(1)
mi_lista.append('a')
mi_lista.append("otro valor")
mi_lista.append(100)
mi_lista.append(False)

print(mi_lista)

# podemos eliminar elementos de nuestra lista
mi_lista.pop()      # con Pop() eliminamos siempre el último elemento de la lista
print(mi_lista)

mi_lista.pop() 
print(mi_lista)

mi_lista.pop()      # eliminamos los últimos tres elementos de la lista
mi_lista.pop()
mi_lista.pop()
print(mi_lista)

# insertamos nuevos elementos en la posicion que deseemos
# en este caso en la posición cero insertamos el valor 'El nuevo valor'
mi_lista.insert(0, 'El nuevo valor')
print(mi_lista)

mi_lista.insert(3,333)
print(mi_lista)

# elimina el valor 2 dentro de la lista (solo el primer valor si existe)
mi_lista.remove(2)
print(mi_lista)

# elimina de la lista el valor 'casa'
mi_lista.remove('casa')
print(mi_lista)

# Podemos borrar con base al índice dentro de la lista
# por ejemplo si quiero borrar el elemento 0 de la lista
del mi_lista[0]
print(mi_lista)

# por ejemplo si quiero borrar el elemento 5 de la lista
del mi_lista[5]
print(mi_lista)

