""" Generador de Secuencia Fibonacci
    Objetivo: Generar los números de la secuencia de Fibonacci (donde cada número es 
    la suma de los dos anteriores) hasta que el número generado supere un límite establecido por el usuario (ej. 1000).
    Mecanismo: Un while que se repite mientras el número actual de la secuencia sea menor o igual al límite."""

limite = int(input("Ingresa el límite superior para la secuencia de Fibonacci: "))
a, b = 0, 1             # Inicializa los dos primeros números de la secuencia
print("Secuencia de Fibonacci hasta", limite, ":")

while a <= limite:
    print(a, end=' ')
    a, b = b, a + b     # Actualiza los valores de a y b para la siguiente iteración

print()                 # Imprime una nueva línea al final de la secuencia
