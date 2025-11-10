""" Uso de continue en un ciclo for
    En este ejemplo se creará un ciclo del 1 al 100, pero saltara los valores entre 10 y 20, 40 y 70, y 90 y 95."""

print("Iterando sobre un rango de números del 1 al 100, saltando ciertos rangos:")
for numero in range(1, 101):
    if (10 <= numero <= 20) or (40 <= numero <= 70) or (90 <= numero <= 95):
        continue  # Saltar los números en los rangos especificados
    print(numero)
