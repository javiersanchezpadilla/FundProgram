""" Validación de Entrada Obligatoria
Objetivo: Pedir al usuario que ingrese su nombre de usuario. Usar un ciclo while para 
asegurar que el nombre no esté vacío y que no contenga espacios.
Mecanismo: Un while que repite el input si se cumplen las condiciones de error (cadena vacía o espacio)."""

nombre_usuario = ""                                                             # Inicializa la variable para almacenar el nombre de usuario
while not nombre_usuario or ' ' in nombre_usuario:                              # Continúa el ciclo mientras el nombre esté vacío o contenga espacios
    nombre_usuario = input("Ingresa tu nombre de usuario (sin espacios): ")     # Solicita el nombre de usuario
    if not nombre_usuario:
        print("El nombre de usuario no puede estar vacío. Intenta de nuevo.")   # Mensaje de error si está vacío
    elif ' ' in nombre_usuario:
        print("El nombre de usuario no puede contener espacios. Intenta de nuevo.")  # Mensaje de error si contiene espacios

print(f"Nombre de usuario '{nombre_usuario}' registrado correctamente.")        # Mensaje de éxito al ingresar un nombre válido