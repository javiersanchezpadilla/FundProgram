""" Podemos convertir una tupla en una lista y una lista en una tupla"""

miTupla = (1,2,(10,20),4)
print(miTupla)
miTupla = list(miTupla)
print(type(miTupla))
print(miTupla)

miTupla = tuple(miTupla)
print(type(miTupla))
print(miTupla)
