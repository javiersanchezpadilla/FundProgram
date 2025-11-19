"""Ejemplo de uso del ciclo while para imprimir una cadena y reducirla en cada iteración:
    En cada iteración se imprime la cadena completa y luego se elimina el primer carácter,
    hasta que la cadena quede vacía."""

cadena = "Python es un lenguaje de programación"
while len(cadena) > 0:
    print(cadena)
    cadena = cadena[1:]         # Actualizamos la cadena quitando el primer caracter
