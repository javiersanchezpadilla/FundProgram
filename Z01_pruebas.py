""" Ejercicios de prueba para evaluar la funcion print()

    10 Ejercicios de Programación en Python (Solo con print())
    Ejercicios, ordenados de menor a mayor complejidad, que solo requieren el 
    uso de la función print() para resolverlos.

    Consejo para el Alumno
    Recuerde a su alumno que, aunque se sienta limitado al principio, dominar el output (print()) es crucial. 
    Todos los programas, sin importar lo complejos que sean, usan esta función para mostrar sus resultados o 
    para depurar errores. ¡Es la primera forma en que el programa "habla" con el mundo! 
"""
calificaciones = {
   "Ana": {"Matematicas": 85, "Historia": 90},
   "Beto": {"Matematicas": 78, "Historia": 88},
   "Carlos": {"Matematicas": 92, "Historia": 70} }

for nombre in calificaciones:
   print("Estudiante:", nombre)
   print("Calificación de Historia:", calificaciones[nombre]["Historia"])
   print()