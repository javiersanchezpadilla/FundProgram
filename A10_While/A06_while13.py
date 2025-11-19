""" Cálculo de Intereses Compuestos
    Objetivo: Calcular cuántos años tomará a una inversión inicial alcanzar una meta de dinero 
    específica (ej. duplicar el monto), dado un porcentaje de interés anual.
    Mecanismo: Un while que se ejecuta mientras el saldo actual sea menor que el saldo meta, 
    incrementando la cuenta de años en cada iteración."""


inversion_inicial = float(input("Ingresa el monto de la inversión inicial: "))
tasa_interes = float(input("Ingresa la tasa de interés anual (en %): ")) / 100
saldo_meta = float(input("Ingresa el monto meta que deseas alcanzar: "))

saldo_actual = inversion_inicial
años = 0
while saldo_actual < saldo_meta:
    saldo_actual += saldo_actual * tasa_interes     # Calcula el interés y lo añade al saldo actual
    años += 1                                       # Incrementa el contador de años

print(f"Tomará {años} años alcanzar o superar el monto meta de {saldo_meta:.2f}.")