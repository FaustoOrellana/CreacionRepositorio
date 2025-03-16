def temperatura_promedio(ciudades_temperaturas):
    """
    Calcula la temperatura promedio de varias ciudades durante un período de tiempo.

    Args:
        ciudades_temperaturas (dict): Diccionario que contiene nombres de ciudades como claves
                                      y listas de temperaturas (por semana) como valores.
    Returns:
        dict: Diccionario con las ciudades y sus temperaturas promedio.
    """
    temperaturas_promedio = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio

# Datos de temperaturas para varias ciudades (4 semanas)
ciudades_temperaturas = {
    "Pasaje": [78, 80, 82, 79, 85, 88, 92, 76, 79, 83, 81, 87, 89, 93, 77, 81, 85, 82, 88, 91, 95, 75, 78, 80, 79, 84, 87, 91],
    "Machala": [62, 64, 68, 70, 73, 75, 79, 63, 66, 70, 72, 75, 77, 81, 61, 65, 68, 70, 72, 76, 80, 64, 67, 69, 71, 74, 77, 80],
    "Guabo": [90, 92, 94, 91, 88, 85, 82, 89, 91, 93, 90, 87, 84, 81, 91, 93, 95, 92, 89, 86, 83, 88, 90, 92, 89, 86, 83, 80]
}

# Llamar a la función para calcular los promedios
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostrar los resultados
print("Temperaturas Promedio por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio:.2f}°C")
