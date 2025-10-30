""" Uso de los operadores lógicos

    Operador        Descripción                                   Uso
    -----------------------------------------------------------------
      and       Devielve True si ambos valores son True         a and b
      or        Devuelve True si algunos de los coponentes      a or b
                es True.
      not       Devuelve True si el componente es False         not a
"""

a = True
b = True
c = False
res = a and b
print(f'La comparación de {a} AND {b} es {res}')    # La comparación de True AND True es True
res = a and c
print(f'La comparación de {a} AND {c} es {res}')    # La comparación de True AND False es False
res = a or b
print(f'La comparación de {a} OR {b} es {res}')     # La comparación de True OR True es True
res = a or c
print(f'La comparación de {a} OR {c} es {res}')     # La comparación de True OR False es True
res= not a
print(f'La comparación de NOT {a} es {res}')        # La comparación de NOT True es False
