""" Programa para solicitar una contraseña al usuario hasta que ingrese la correcta.
    Se utiliza un ciclo while que continúa pidiendo la contraseña hasta que el usuario ingrese """

contraseña_correcta = "segura123"                               # Definimos la contraseña correcta
contraseña_ingresada = ""                                       # Inicializamos la variable para almacenar la contraseña ingresada

while contraseña_ingresada != contraseña_correcta:
    contraseña_ingresada = input("Ingrese la contraseña: ")     # Solicitamos la contraseña al usuario
    if contraseña_ingresada != contraseña_correcta:
        print("Contraseña incorrecta. Intente de nuevo.")       # Mensaje de error si la contraseña es incorrecta
print("Contraseña correcta. Acceso concedido.")                 # Mensaje de éxito al ingresar la contraseña correcta
