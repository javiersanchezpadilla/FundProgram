""" 3. G - Global
    Una variable es global si está definida en el nivel principal del módulo (el archivo .py que estás ejecutando) 
    o si ha sido explícitamente declarada como global usando la palabra clave global.

    Accesibilidad: Accesible desde cualquier lugar del módulo (dentro y fuera de las funciones).
"""

z = 30                      # Z es global

def otra_funcion():
    print(z)                # Puede acceder a Z

otra_funcion()              # Imprime 30