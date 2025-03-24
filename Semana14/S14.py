# Definición de la función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función con solo el monto total (usa el valor predeterminado del 10%)
monto1 = 1000
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1
print(f"Monto total: ${monto1:.2f}")
print(f"Descuento aplicado (10%): ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}\n")

# Llamada a la función proporcionando el monto total y un porcentaje de descuento específico
monto2 = 1500
porcentaje2 = 15
descuento2 = calcular_descuento(monto2, porcentaje2)
monto_final2 = monto2 - descuento2
print(f"Monto total: ${monto2:.2f}")
print(f"Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")