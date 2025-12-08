""" Crea una función “lanzar_dados” que arroje dos datos al azar y devuelva sus resultados 
    (la función debe retornar dos valores resultado. que se encuentren entre 1 y 6)
    proporciona el resultado de estos dos dados a una función que se llame “evaluar_jugada” 
    (es decir, esta segunda función debe recibir dos argumentos) y que retorne 
    -sin imprimirlo - un mensaje según la suma de estos valores.

    SI LA SUMA ES MENOR O IGUAL A 6:
    “La suma de tus dados es {suma_dados}, lamentable”
    SI LA SUMA ES MAYOR A 6 Y MENOR A 10:
    “La suma de tus dados es {suma_dados}. tienes buenas oportunidades”.
    SI LA SUMA ES MAYORAO IGUAL A 10:
    “La suma de tus datos es {suma_dados}. Parece una jugada ganadora”


"""

from random import randint

dados = []

def lanzar_dados():
    return (randint(1,6), randint(1,6))

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    resultado = ''
    if suma_dados <= 6:
        return f'La suma de tus dados es {suma_dados}. Lamentable'
    elif suma_dados > 6 and suma_dados < 10:
        return f'La suma de tus dados es {suma_dados}. Tienes buenas oportunidades'
    else:
        return f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'

dados = list(lanzar_dados())
print(dados)
print(evaluar_jugada(dados[0],dados[1]))
