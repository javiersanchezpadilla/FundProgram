""" Programa que simula un relog con el ciclo for anidado.
    El ciclo externo itera sobre las horas del día (0 a 23) y el ciclo interno itera sobre los minutos (0 a 59).
    Ademas se contará con los segundos para cada minuto (0 a 59).

    En cada iteración del ciclo interno, se imprime la hora y los minutos en formato "HH:MM:SS".
"""

for hora in range(24):  # Itera sobre las horas del día (0 a 23)
    for minuto in range(60):  # Itera sobre los minutos (0 a 59)
        for segundo in range(60):  # Itera sobre los segundos (0 a 59)
            print(f"{hora:02}:{minuto:02}:{segundo:02}")  # Imprime la hora en formato HH:MM:SS

    # Nota: El formato :02 en f-strings asegura que los números se impriman con al menos dos dígitos, agregando 
    # un cero a la izquierda si es necesario, Por ejemplo, la hora 5 se imprimirá como 05.
