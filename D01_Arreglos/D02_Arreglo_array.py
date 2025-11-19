""" Manejo de arreglos

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

    Uso de la Librería Estándar array

    La librería array es nativa de Python y te permite crear arreglos unidimensionales que solo contienen un tipo de 
    dato homogéneo (todo enteros, todo floats, etc.). Son más eficientes en memoria que las listas normales.
"""
import array

# Creamos un arreglo de enteros sin signo ('I' es el código para unsigned int)
# Tipo de dato 'I' significa que solo aceptará números enteros positivos
mi_array_estandar = array.array('I', [10, 20, 30, 40, 50])
mi_array_alfanumerico = array.array('s')

print(f"Tipo de objeto: {type(mi_array_estandar)}")
print(f"Arreglo inicial: {mi_array_estandar}")

# Operaciones básicas

# 1. Acceder a un elemento por índice (como en una lista)
primer_elemento = mi_array_estandar[0]
print(f"Primer  elemento: {primer_elemento}")
print(f"Segundo elemento: {mi_array_estandar[1]}")
print(f"Tercer  elemento: {mi_array_estandar[2]}")
print(f"Cuarto  elemento: {mi_array_estandar[3]}")
print(f"Quinto  elemento: {mi_array_estandar[4]}")


# 2. Añadir elementos al arreglo (append)
mi_array_estandar.append(60)
mi_array_estandar.append(70)
mi_array_estandar.append(80)
print(f"Después de añadir: {mi_array_estandar}")

