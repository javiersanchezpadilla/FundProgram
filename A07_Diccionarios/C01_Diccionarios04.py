""" Acceder a los elementos de un diccionario.
    En este ejemplo accederemos a traves de la llave del diccionario
    y donde sea el caso por medio del elemento índice (valor numerico de referencia)
"""

mi_diccionario = {'c1':55, 'c2':[1,2,3,4,5], 'c3':{'v1':'Valor 1','v2':'Valor 2'}}

print(mi_diccionario)
print(mi_diccionario['c1'])

print(mi_diccionario['c2'])
print(mi_diccionario['c2'][0])
print(mi_diccionario['c2'][1])
print(mi_diccionario['c2'][2])
print(mi_diccionario['c2'][3])
print(mi_diccionario['c2'][4])
print(mi_diccionario['c2'][2:])
print(mi_diccionario['c2'][:4])
print(mi_diccionario['c3'])
print(mi_diccionario['c3']['v1'])
print(mi_diccionario['c3']['v2'])