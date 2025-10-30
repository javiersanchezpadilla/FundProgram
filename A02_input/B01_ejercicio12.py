""" Cálculo de Área: Pide la base y la altura de un triángulo. Calcula e imprime el área 
    ( base x altura/2), asegurándote de que el resultado sea un número decimal (float)."""

base = input("Escribe la base del triángulo: ")
altura = input("Escribe la altura del triángulo: ")
area = (float(base) * float(altura)) / 2
print("El área del triángulo es " + str(area) + ".")

