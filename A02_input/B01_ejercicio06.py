""" Edad en 5 Años: Pide al usuario su edad actual (como texto). 
    Conviértela a número entero y calcula e imprime la edad que tendrá en 5 años."""

edad_actual = input("¿Cuál es tu edad actual? ")
edad_en_5_anios = int(edad_actual) + 5
print("En 5 años tendrás " + str(edad_en_5_anios) + " años.")

# Alternativa usando solo una línea de código
# print("En 5 años tendrás " + str(int(input("¿Cuál es tu edad actual? ")) + 5) + " años.")

# Alternativa usando f-strings (Python 3.6+)
# print(f"En 5 años tendrás {int(input('¿Cuál es tu edad actual? ')) + 5} años.")

# Alternativa usando format()
# print("En 5 años tendrás {} años.".format(int(input("¿Cuál es tu edad actual? ")) + 5))