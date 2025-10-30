""" En este ejercicio aprenderemos el uso de input()"""

# podemos capturar valores a traves de input
nombre = input('Dame tu nombre: ')
print(f'La varaiable nombre es del tipo {type(nombre)}')
print('Bienvenido {}'.format(nombre))

# Todos los valores capturados a traves de input son del tipo string <class int>
numero1 = input("Valor uno: ")
numero2 = input("Valor dos: ")
print(f"El tipo de dato de la variable numero1 es {type(numero1)}")
print(f"El tipo de dato de la variable numero2 es {type(numero2)}")

print("El resultado de la suma de cadenas nos da {} (lo cual es una concatenacion)".format(numero1 + numero2))

