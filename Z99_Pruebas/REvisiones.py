texto = input("Escribe un texto (una frase, poema o párrafo): ")

letra1 = input("Escribe la primera letra: ").lower()
letra2 = input("Escribe la segunda letra: ").lower()
letra3 = input("Escribe la tercera letra: ").lower()
texto_minus = texto.lower()

print("RESULTADOS")
print("Cantidad de veces que aparecen las letras:")
print(f"La letra '{letra1}' aparece {texto_minus.count(letra1)} veces.")
print(f"La letra '{letra2}' aparece {texto_minus.count(letra2)} veces.")
print(f"La letra '{letra3}' aparece {texto_minus.count(letra3)} veces.")


palabras = texto.split() 
cantidad_palabras = len(palabras)
print(f" El texto tiene {cantidad_palabras} palabras en total.")

primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra del texto es: '{primera_letra}'")
print(f"La última letra del texto es: '{ultima_letra}'")


palabras_invertidas = palabras[::-1]
texto_invertido = " ".join(palabras_invertidas)
print(f"Texto con el orden de las palabras invertido:")
print(texto_invertido)


print("La palabra 'Python' está en el texto")
python = "python" in texto_minus
print(python)