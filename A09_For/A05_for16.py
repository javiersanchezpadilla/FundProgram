""" Ejemplo de uso del ciclo for para iterar sobre diferentes tipos de colecciones en Python.
    Se muestran ejemplos de iteración sobre diccionarios.
    Los diccionarios son estructuras de datos que almacenan pares clave-valor."""


print("\nIterando sobre los elementos de un diccionario:")
print( "Extraer la llave y el valor:" )

mi_diccionario = {'nombre': 'juan', 'calificaciones': [100, 90, 80, 95], 'carrera': 'Ingenieria en Ciencia de Datos', 'Matricula': '25322660'}

for llave, valor in mi_diccionario.items():
    print(f'El valor de la llave es: {llave}, >>> El valor en el diccionario es: {valor}') 
