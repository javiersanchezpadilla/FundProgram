""" Nivel Medio (Múltiples if Independientes)
    Aquí se requiere usar varios if independientes o el uso de operadores lógicos (and, or) 
    para ejecutar diferentes acciones basadas en una misma entrada.
    
    Ejercicio 6: Días de Fin de Semana
    Pide al usuario el día de la semana (como una cadena de texto, ej. "sábado").
    Usa un if con el operador or para imprimir: "¡Relájate, es fin de semana!" solo si el día es "sábado" O "domingo".
"""

dia_semana = input("Dame el día de la semana en letras: ").lower()

# validamos si el usuario escribio sábado con acento lo quitamos para hacer solo una comparación
dia_semana = dia_semana.replace('á', 'a')

# como vemos solo se está validando la palabra sabado y domingo (sábado con acento se reemplaza por sabado sin acento)
if dia_semana == 'sabado' or dia_semana == 'domingo':
    print("¡Relájate, es fin de semana!")
