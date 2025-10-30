""" Podemos extrar los elementos de una tupla y asignarlos a variables """

mi_tupla = (1, 10, 14, 20)

# Podemos de forma tradicional extraer cada uno de los valores a cada una de 
# las variables

valor1 = mi_tupla[0]
valor2 = mi_tupla[1]
valor3 = mi_tupla[2]
valor4 = mi_tupla[3]

# Como los valores ya no son parte de la tupla ahora podemos usarlos de forma normal 
# porque ya pertenecen a las variables
print(valor1)
print(valor1 + 10)
print(valor2)
print(valor2 + 20)
print(valor3)
print(valor3 + 30)
print(valor4)
print(valor4 + 40)

# Otra forma de extrer los valores es mediante el concepto de desempaquetar los valores 
# solo que el número de variables debe ser equivalente al número de elementos en la tupla
a, b, c, d = mi_tupla
print('Los valores de las variables son', a, b, c, d)

# En caso de requerir menos valores podemos ignorar el resto de las variables, por ejemplo
# en la siguiente tupla solo requerimos extraer el primer valor, el resto no nos interesa
mi_otra_tupla = ( 1, 2, 3, 4, 10, 22, 5, 60, 7, 3, 4, 55, 12, 4432, 0, 2)


# podemos usar la variable de descarte "_", tambien conocida como variable temporal
# tenemos que usar el mismo numero de variables temporales como elementos en la tupla
primer_valor, _,_, _, _, _, _, _, _, _, _, _, _, _, _, _ = mi_otra_tupla
print(primer_valor)

# Lo anterior no se ve nada practico, por lo que podemos usarlo tambien de la siguiente forma
# con la variable de descarte "_" y el asterisco "*", le estamos diciendo a Python
# *_ descarta (_) el resto (*) de los valores (hacia adelante).
primer_valor, *_ = mi_otra_tupla
print(primer_valor)
