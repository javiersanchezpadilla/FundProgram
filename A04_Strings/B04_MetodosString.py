""" En este ejercicio entenderemos y practicaremos algunos de los metodos mas comunes de las cadenas 
    de texto (strings) en Python."""

mi_cadena = "   Python es un lenguaje de programación muy popular   "
print(f"La cadena original es: '{mi_cadena}'\n")

# Metodo upper(): convierte todos los caracteres a mayusculas
cadena_mayusculas = mi_cadena.upper()
print(f"Cadena en mayusculas: '{cadena_mayusculas}'")

# Metodo lower(): convierte todos los caracteres a minusculas
cadena_minusculas = mi_cadena.lower()
print(f"Cadena en minusculas: '{cadena_minusculas}'")

# Metodo strip(): elimina los espacios en blanco al inicio y al final de la cadena
cadena_sin_espacios = mi_cadena.strip()
print(f"Cadena sin espacios al inicio y al final: '{cadena_sin_espacios}'")

# Metodo replace(): reemplaza una subcadena por otra
cadena_reemplazada = mi_cadena.replace("popular", "famoso")
print(f"Cadena con reemplazo: '{cadena_reemplazada}'")

# Metodo split(): divide la cadena en una lista de subcadenas basadas en un separador
lista_palabras = mi_cadena.split()
print(f"Cadena dividida en palabras: {lista_palabras}")

# split() con un separador especifico
lista_palabras_o = mi_cadena.split("o")
print(f"Cadena dividida por la letra 'o': {lista_palabras_o}")

# Metodo find(): busca una subcadena y devuelve el indice de su primera aparicion, o -1 si no se encuentra
indice_programacion = mi_cadena.find("programación")
print(f"Indice de la palabra 'programación': {indice_programacion}")

# Metodo count(): cuenta cuantas veces aparece una subcadena en la cadena
conteo_de_a = mi_cadena.count("a")
print(f"Número de veces que aparece la letra 'a': {conteo_de_a}")

# Metodo join(): une una lista de cadenas en una sola cadena, usando un separador especifico
lista_palabras = ["Python", "es", "genial"]
cadena_unida = " ".join(lista_palabras)     # unimos con espacios
print(f"Cadena unida con espacios: '{cadena_unida}'")

# Metodo join(): une una lista de cadenas en una sola cadena, usando un separador especifico
lista_palabras = ["Python", "es", "genial"]
cadena_unida = "-".join(lista_palabras)     # unimos con guiones
print(f"Cadena unida con espacios: '{cadena_unida}'")

