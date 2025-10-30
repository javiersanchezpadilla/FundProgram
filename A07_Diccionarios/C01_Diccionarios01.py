""" Diccionarios en Python:
    Un diccionario en Python es una colección de datos no ordenada, mutable y que se organiza 
    mediante un sistema de llave (o clave)-valor. Es la estructura de datos ideal para almacenar 
    información relacionada de forma lógica.

    Características Clave de los Diccionarios
    Un diccionario es similar a un diccionario real o a una agenda telefónica, donde buscas algo 
    (la llave) para encontrar su significado o dato asociado (el valor).
    
    Característica          Descripción
    ---------------------------------------------------------------------------------------------
    No Ordenado         A partir de Python 3.7 (y de forma implementada en 3.6+), los diccionarios 
                        mantienen el orden de inserción. Sin embargo, a diferencia de las listas 
                        y tuplas, no se accede a sus elementos por un índice numérico de posición.

    Mutable             Se pueden añadir, modificar o eliminar pares de llave-valor después de que 
                        el diccionario ha sido creado.

    Indexado            Los elementos se acceden utilizando una llave única (que debe ser inmutable, 
    por Llave           como una cadena o un número), no por su posición numérica.

    Par                 Cada elemento es un par donde la llave es el identificador (p. ej., "nombre") 
    Llave-Valor         y el valor es el dato (p. ej., "Ana").


    * Se manejan en pares.
    * Cada par tiene una clave y una definición separada por dos puntos (:)
    * Las definiciones de claves no deben repetirse, las definiciones si.
    * No existe orden alguno por lo que no se busca por el índice sino por su valor llave.
    * Podemos acceder sin necesidad de conocer su ubicación exacta.
"""

usuario = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "México",
    "activo": True 
}

edad_carlos = usuario["edad"]
print(f"La edad es: {edad_carlos}") 
# Salida: La edad es: 30