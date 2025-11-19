""" En este ejemplo dada una lista de numeros ordenarlos

    Implementación:
    ---------------
    1) Crea una lista vacía, llamada, por ejemplo, lista_ordenada.
    2) Recorre la lista original elemento por elemento (usando un ciclo for).
    3) Para cada elemento, usa un ciclo anidado (while o for) para encontrar la posición correcta 
    dentro de lista_ordenada y luego insértalo allí.

    Sugerencia: Si el nuevo número es mayor que todos los de lista_ordenada, añádelo al final. Si no, 
    insértalo justo antes del primer número que sea mayor que él.

"""

# Lista de prueba
numeros_desordenados = [5, 3, 7, 2, 2, 10, 0, 2, 5, 7]
lista_ordenada = []

print(f"Lista original: {numeros_desordenados}")

# 1. Ciclo FOR: Recorre cada elemento de la lista desordenada
for elemento in numeros_desordenados:
    
    # Índice que usaremos para recorrer la lista_ordenada
    indice_insercion = 0
    
    # 2. Ciclo WHILE: Busca la posición correcta en la lista_ordenada
    # Se repite mientras no hayamos llegado al final de la lista_ordenada
    # Y mientras el elemento actual sea MAYOR que el elemento en esa posición
    while indice_insercion < len(lista_ordenada) and elemento > lista_ordenada[indice_insercion]:
        indice_insercion += 1
        
    # 3. Inserción: Usamos el método .insert(indice, valor)
    # Una vez que el ciclo while se detiene, 'indice_insercion' 
    # marca la posición antes de la cual se debe insertar el elemento.
    lista_ordenada.insert(indice_insercion, elemento)
    
    print(f"   Después de procesar {elemento}, la lista es: {lista_ordenada}")

print("\nRESULTADO FINAL:")
print(f"Lista ordenada manualmente: {lista_ordenada}")
