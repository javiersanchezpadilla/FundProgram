""" Ejemplo de uso del ciclo for para iterar sobre diferentes tipos de colecciones en Python.
    Se muestran ejemplos de iteración sobre diccionarios.
    Los diccionarios son estructuras de datos que almacenan pares llave-valor."""


print("\nIterando sobre los elementos de un diccionario:")
print( "Extraer llave y valor mediante el metodo items()" )

mi_diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for llave, valor in mi_diccionario.items():
    print('El valor de la llave es:', llave, 'El valor en el diccionario es:', valor) 
