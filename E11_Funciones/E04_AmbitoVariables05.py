""" Modificación de Variables Globales (Palabras Clave)
    Por defecto, si intentas modificar (asignar un nuevo valor) a una variable dentro de una función, 
    Python asume que estás creando una nueva variable local con ese nombre, incluso si ya existe una 
    variable global con el mismo nombre.
    Para modificar una variable que existe en un ámbito superior, debes usar palabras clave:
    
    Palabra                 Uso                                 Ambito que Modifica
    Clave
    --------------------------------------------------------------------------------
    global      Se usa dentro de una función para indicar           Global (G)
                que quieres modificar una variable global.
                
    nonlocal    Se usa dentro de una función anidada para           Encerrado (E)
                indicar que quieres modificar una variable 
                del ámbito encerrado (enclosing)."""

contador = 10            # Variable Global

                        # Hacer la prueba de comentar la linea global contador
def incrementar():
    global contador     # Indica que queremos modificar la variable global
    contador = 100       # Modifica la variable global

incrementar()
print(contador)         # Imprime 10 comentando la linea global contador
                        # Si descomentamos la linea global contador, imprimirá 100  

