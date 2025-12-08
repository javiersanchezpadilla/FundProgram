""" Para entender este tema se va a presentar el juego de los palitos, 
    se toman un palito por cada participante y el que saca el palito más corto 
    es el que pierde.

    La secuencia de ejecución será la siguiente:
    --------------------------------------------
    Lista inicial
    Mezclar palitos
    pedirle intento al usuario
    Comprobar intento
"""

from random import shuffle

                        # Definicion de la lista inicial
palitos = ['-', '--', '---','----']

                        # Mezclar los palitos
def mezclar(lista):
    shuffle(lista)
    return lista

                        # pedirle al jugados que intente
def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')
    return int(intento)

                        # comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('Perdiste!!! a lavar los platos')
    else:
        print('Esta vez te has salvado')

    print(f'Te ha tocado {lista[intento - 1]}')


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)

