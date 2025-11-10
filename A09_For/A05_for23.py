""" break dentro de los ciclos en Python se define como una salida inmediata y completa del ciclo donde se encuentra.

    A diferencia de continue (que salta a la siguiente repetición), el break detiene totalmente el ciclo (for o while) 
    y el programa continúa ejecutándose con el código que viene después de que el ciclo ha terminado.

    Uso de break
    La función principal de break es:

    1. Terminar la ejecución del ciclo actual de forma abrupta.
    2. Saltar todo el código restante dentro del ciclo (incluyendo el código que venía después del break y las 
       repeticiones futuras).
    3. Continuar con la ejecución normal del programa fuera del ciclo.

    El break se usa comúnmente cuando has encontrado lo que buscabas y no tiene sentido seguir revisando el resto de los elementos."""

print("\nIterando sobre un rango de números del 1 al 10, deteniéndose al encontrar el número 6:")

for numero in range(1, 11):
    if numero == 6:
        break  # Salir del ciclo cuando el número es 6
    print(numero)   

