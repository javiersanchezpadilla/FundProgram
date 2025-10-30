""" División y Residuo: Pide dos números enteros. Calcula e imprime el resultado de la 
    división entera (//) y el residuo (módulo %) de la división de ambos."""

num1 = int(input("Escribe el primer número entero: "))
num2 = int(input("Escribe el segundo número entero: "))
division_entera = num1 // num2
residuo = num1 % num2
print(f"La división entera de {num1} // {num2} es {division_entera}.")
print(f"El residuo de {num1} % {num2} es {residuo}.")

