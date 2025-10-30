""" En este ejercicio practicaremos el uso de cadenas de texto (strings) en Python.
    Veremos como definirlas, concatenarlas, repetirlas y algunas de sus funciones mas comunes"""

cadena = "Hola Mundo"
print(f"El tipo actual de dato de la variable cadena {cadena} es {type(cadena)}")

# podemos concatenar cadenas con el operador +
cadena2 = " - Adios Mundo"
cadena3 = cadena + cadena2
print(f"El tipo actual de dato de la variable cadena3 {cadena3} es {type(cadena3)}")    

# podemos referenciar caracteres individuales de la cadena
print("\n\nREFERENCIACION DE CARACTERES EN UNA CADENA\n")
print(f"El primer caracter de la cadena3 {cadena3} es {cadena3[0]}")    
print(f"El segundo caracter de la cadena3 {cadena3} es {cadena3[1]}")    
print(f"El tercer caracter de la cadena3 {cadena3} es {cadena3[2]}")    
print(f"El cuarto caracter de la cadena3 {cadena3} es {cadena3[3]}")    
print(f"El ultimo caracter de la cadena3 {cadena3} es {cadena3[-1]}")    
print(f"El penultimo caracter de la cadena3 {cadena3} es {cadena3[-2]}")    
print(f"El antepenultimo caracter de la cadena3 {cadena3} es {cadena3[-3]}")

# podemos obtener subcadenas (slicing)
print("\n\nOBTENCION DE SUBCADENAS (SLICING)\n")
print(f"Los caracteres del 0 al 3 de la cadena3 {cadena3} son {cadena3[0:4]}")    
print(f"Los caracteres del 5 al 10 de la cadena3 {cadena3} son {cadena3[5:11]}")    
print(f"Los caracteres del 11 al 16 de la cadena3 {cadena3} son {cadena3[11:17]}")    
print(f"Los caracteres del 17 al 22 de la cadena3 {cadena3} son {cadena3[17:23]}")    
print(f"Los caracteres del 0 al 22 de la cadena3 {cadena3} son {cadena3[0:23]}")    
print(f"Los caracteres del 0 al 22 de la cadena3 {cadena3} son {cadena3[:23]}")    
print(f"Los caracteres del 5 al final de la cadena3 {cadena3} son {cadena3[5:]}")    
print(f"Los caracteres del inicio al 10 de la cadena3 {cadena3} son {cadena3[:11]}")    
print(f"Los caracteres del inicio al final de la cadena3 {cadena3} son {cadena3[:]}")

