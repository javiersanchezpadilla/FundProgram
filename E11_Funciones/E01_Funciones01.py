def suma_dos(a, b):
    return a + b

def suma_tres(a, b, c):
    return a + b + c

def suma_cuatro(a=0, b=0, c=0, d=0):
    return a + b + c + d

def suma_muchos(*perro):
    total_suma = 0
    for x in perro:
        total_suma += x
    return total_suma



# a = suma_dos(10, 5)
# print(a)

# a = suma_tres(5, 10, 20)
# print(a)

# a = suma_cuatro(1, 9, 10, 20)
# print(a)

# a = suma_muchos(1, 2, 3, 4, 5, 10, 40, 50)
# print(a)

a = suma_cuatro(1, 1, 8, 10, 30)
print('El valor de la suma es:', a)




