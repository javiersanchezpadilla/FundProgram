""" Promedio Flotante: Pide al usuario dos notas de examen (números). 
    Conviértelas a flotantes, calcula e imprime la suma de ambas notas."""

nota1 = input("Escribe la primera nota: ")
nota2 = input("Escribe la segunda nota: ")
suma_notas = float(nota1) + float(nota2)
print("La suma de las notas es " + str(suma_notas) + ".")

# Alternativa usando solo una línea de código
# print("La suma de las notas es " + str(float(input("Escribe la primera nota: ")) + float(input("Escribe la segunda nota: "))) + ".")  