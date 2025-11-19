""" Dibujar un Triángulo con while Anidado
Objetivo: Pedir al usuario la altura del triángulo (ej. 5). Usar un ciclo while externo 
para controlar las filas y un ciclo while anidado para controlar la impresión de * en cada columna.
Mecanismo: Dos while anidados. El externo avanza las filas, el interno imprime los caracteres de la fila actual."""

altura = int(input("Ingresa la altura del triángulo: "))  # Solicita la altura del triángulo al usuario
fila = 1                        # Inicializa la variable para controlar las filas
while fila <= altura:           # Ciclo externo para cada fila
    columna = 1                 # Inicializa la variable para controlar las columnas
    while columna <= fila:      # Ciclo interno para imprimir los '*' en la fila actual
        print("*", end="")      # Imprime un '*' sin salto de línea
        columna += 1            # Avanza a la siguiente columna
    print()                     # Salto de línea después de completar una fila
    fila += 1                   # Avanza a la siguiente fila

