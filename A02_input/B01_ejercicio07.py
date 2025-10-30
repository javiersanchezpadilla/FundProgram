""" Doble de Puntos: Pide al usuario su puntuación en un juego (como texto). 
    Conviértela a número y calcula e imprime el doble de esa puntuación."""

puntuacion = input("¿Cuál es tu puntuación en el juego? ")
doble_puntuacion = float(puntuacion) * 2
print("El doble de tu puntuación es " + str(doble_puntuacion) + ".")

# Alternativa usando solo una línea de código
# print("El doble de tu puntuación es " + str(float(input("¿Cuál es tu puntuación en el juego? ")) * 2) + ".")