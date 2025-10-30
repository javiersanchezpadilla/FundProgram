""" Datos de Inventario: Pide el nombre de un producto y su precio. 
    Imprime un mensaje que concatene ambos datos, asegurándote de que el 
    precio se muestre con exactamente dos decimales (usa una f-string o métodos de formateo)."""

nombre_producto = input("Escribe el nombre del producto: ")
precio_producto = input("Escribe el precio del producto: ")
precio_formateado = "{:.2f}".format(float(precio_producto))
print(f"El producto '{nombre_producto}' tiene un precio de ${precio_formateado}.")

# Alternativa usando solo una línea de código
# print(f"El producto '{(nombre_producto := input('Escribe el nombre del producto: '))}' tiene un precio de ${'{:.2f}'.format(float(input('Escribe el precio del producto: ')))}.") 
