""" MODIFICAR ELEMENTOS DE UN DICCIONARIO.
    Como condición el elemento debe existir dentro del diccionario. en el ejemplo se va a
    carmbiar el elemento 2 por la letra “B”, esto es de “b” → “B”
""" 

dic = {1:'a', 2:'b'}
print(dic)          # {1: 'a', 2: 'b'}

dic[3]='c'          #                  vvvvvvv SE agrego este nuevo elemento al diccionario
print(dic)          # {1: 'a', 2: 'b', 3: 'c'}

dic[2]='B'          #          vvvvv Se modifico este elemento
print(dic)          # {1: 'a', 2: 'B', 3: 'c'}
