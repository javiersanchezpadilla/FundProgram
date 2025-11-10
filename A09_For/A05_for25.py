""" Ejemplo de uso del ciclo for con la instrucción break.
    En este ejemplo se itera sobre una cadena de texto y se detiene el ciclo al encontrar una letra específica."""

print("\nIterando sobre una cadena de texto, deteniéndose al encontrar la letra 'e':")

texto = "Fundamentos de Programación"

for letra in texto:
    if letra == 'e':
        break  # Salir del ciclo cuando se encuentra la letra 'e'
    print(letra)    
