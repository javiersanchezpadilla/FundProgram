# Plantear el siguiente problema
# Declara una variable del tipo lista llamada mochila
mochila = []
print(mochila)

# Introducir en mochila un libro de matematica, otro de fisica, un cuaderno rojo y un cuaderno amarillo
print('\nSE INRODUJERON LOS SIGUIENTES ELEMENTOS EN LA MOCHILA\n')
mochila.append('Libro matematicas')
mochila.append('Libro fisica')
mochila.append('Cuaderno rojo')
mochila.append('Cuaderno amarillo')

print(mochila)

# Sacamos de la mochila el cuaderno rojo
# primero ubicamos la posicion del indice donde se encuentra el cuaderno rojo
# ya que contamos con la posicion (indice),procedemos a borrarlo
mochila.pop(mochila.index('Cuaderno rojo'))

# la opcion mas sencilla es:
# mochila.pop('Cuaderno rojo')  
print(mochila)

# Introucimos en la mochila un bote de agua y un borrador
mochila.append('Bote agua')
mochila.append('Borrador')

# Contamos con una lapicera que contiene un lapiz, una pluma y pegamento
lapicera = ['lapiz', 'pluma', 'pegamento']
print('\nEl contenido de la lapicera es', lapicera)

# introducimos la lapicera dentro de la mochila
print('El contenido de la mochila antes de la lapicera', mochila)
mochila.append(lapicera)

print('El contenido de la mochila despues de introducir la la picera es', mochila)
print('¿Qué contiene la lapicera que esta dentro de la mochila?')
print(mochila[mochila.index(lapicera)])
print(mochila[mochila.index(lapicera)][0])
print(mochila[mochila.index(lapicera)][1])
print(mochila[mochila.index(lapicera)][2])
