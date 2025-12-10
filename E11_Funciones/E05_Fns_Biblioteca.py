""" Programa para la gestión de una biblioteca
    Usando funciones y manejo de variables globales y locales.
    
    #,Nombre de la Función      Parámetros      Tarea Específica                        Concepto Clave
    --------------------------------------------------------------------------------------------------------
    1,mostrar_menu()            Ninguno         Imprime todas las opciones              Función sin return.
                                                disponibles en la consola

    2,obtener_libros()          Ninguno         Inicializa y devuelve la lista          Función de inicialización.
                                                principal de libros

    3,agregar_libro(libros)     Lista libros    Pide al usuario el Título y Autor       Modificar un argumento (lista).
                                                y lo añade a la lista

    4,mostrar_libros(libros)    Lista libros    Recorre la lista y muestra todos        Uso de ciclo for.
                                                los libros de forma ordenada.

    5,buscar_por_titulo,        Lista libros    Busca un libro por una palabra          Uso de ciclo for y if con cadenas.
      (libros, titulo)          Cadena titulo   clave en el título y lo imprime

    6,eliminar_libro            Lista libros    Recibe el índice del libro y lo         Uso de pop() o del.
      (libros, indice)          Entero indice   elimina usando .pop() o del
    
    """

def obtener_libros():
    """ Inicializa y devuelve la lista principal de libros."""

    return [
        {"titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez"},
        {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes"},
        {"titulo": "La Sombra del Viento", "autor": "Carlos Ruiz Zafón"},
        {"titulo": "El Amor en los Tiempos del Cólera", "autor": "Gabriel García Márquez"},
        {"titulo": "1984", "autor": "George Orwell"},
        {"titulo": "Ficciones", "autor": "Jorge Luis Borges"},
        {"titulo": "La Casa de los Espíritus", "autor": "Isabel Allende"},
        {"titulo": "Rayuela", "autor": "Julio Cortázar"},
        {"titulo": "El Aleph", "autor": "Jorge Luis Borges"},
        {"titulo": "Pedro Páramo", "autor": "Juan Rulfo"} 
    ]


def mostrar_libros(libros):
    """ Recorre la lista y muestra todos los libros de forma ordenada."""

    print("Libros en la Biblioteca:")
    for idx, libro in enumerate(libros, start=1):
        print(f"{idx}. {libro['titulo']} por {libro['autor']}")



def agregar_libro(libros):
    """ Pide al usuario el Título y Autor y lo añade a la lista."""

    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    libros.append({"titulo": titulo, "autor": autor})
    print(f"Libro '{titulo}' agregado a la biblioteca.")



def buscar_por_titulo(libros, titulo):
    """ Busca un libro por una palabra clave en el título y lo imprime."""

    encontrados = [libro for libro in libros if titulo.lower() in libro["titulo"].lower()]
    
    if encontrados:
        print(f"Libros encontrados con '{titulo}':")
        for libro in encontrados:
            print(f"- {libro['titulo']} por {libro['autor']}")
    else:
        print(f"No se encontraron libros con '{titulo}' en el título.")



def eliminar_libro(libros, indice):
    """ Recibe el índice del libro y lo elimina usando .pop()."""

    if 0 <= indice < len(libros):
        eliminado = libros.pop(indice)
        print(f"Libro '{eliminado['titulo']}' eliminado de la biblioteca.")
    else:
        print("Índice inválido. No se pudo eliminar el libro.")



def mostrar_menu():
    """ Imprime todas las opciones disponibles en consola."""

    print("\nMenú de la Biblioteca:")
    print("1. Mostrar Libros")
    print("2. Agregar Libro")
    print("3. Buscar por Título")
    print("4. Eliminar Libro")
    print("5. Salir")



def ejecutar_sistema():
    """ Funcion principal para ejecutar el sistema de gestión de biblioteca."""

    biblioteca = obtener_libros()                           # Inicializa la lista de libros
    
    while True:
        mostrar_menu()                                      # Despliega las opciones del menu
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            mostrar_libros(biblioteca)

        elif opcion == '2':
            agregar_libro(biblioteca)

        elif opcion == '3':
            titulo_buscado = input("Título a buscar: ")
            buscar_por_titulo(biblioteca, titulo_buscado)

        elif opcion == '4':
            eliminar_libro(biblioteca, int(input("Índice del libro a eliminar: ")) - 1)

        elif opcion == '5':
            print("Saliendo del sistema.")
            break
            

                                            # Llamada de inicio al programa
if __name__ == "__main__":
    ejecutar_sistema()