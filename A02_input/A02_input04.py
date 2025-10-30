""" En este ejercicio se solicitara información para
    rellenar un formulario y desplegar sus resultados"""


nombre = input("Proporcione su nombre: ")
apellido = input("Proporcione su apellido: ")
edad = int(input("Proporcione su edad: "))
semestre = int(input("Proporcione el semestre actual: "))

# Solucion para mostrar los datos formateando la cadena de salida
print("\n\nBienvenido {} {}".format(nombre, apellido))
print("Tu edad es {} años y en diez años tendras {} años".format(edad, edad + 10))

# Solucion para mostrar los datos mediante el uso de "F" string
print(f"\nBienvenido {nombre} {apellido}")
print(f"Tu edad es {edad} años y en diez años tendras {edad + 10} años")
