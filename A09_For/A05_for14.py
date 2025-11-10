""" Ejemplo de uso del ciclo for para iterar sobre diferentes tipos de colecciones en Python.
    Se muestran ejemplos de iteración sobre diccionarios.
    Los diccionarios son estructuras de datos que almacenan pares clave-valor."""


print("\nIterando sobre los elementos de un diccionario:")
print( "Usando solo las claves del diccionario:" )

mi_diccionario = {'nombre': 'juan', 'calificaciones': [100, 90, 80, 95], 'carrera': 'Ingenieria en Ciencia de Datos', 'Matricula': '25322660'}

for clave in mi_diccionario:
    print(f'El valor de la llave es: {clave}, >>> El valor en el diccionario es: {mi_diccionario[clave]}') 
