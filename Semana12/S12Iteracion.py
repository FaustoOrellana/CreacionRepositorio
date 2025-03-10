# Nombres de las ciudades
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Datos de temperaturas (matriz 3D)
temperaturas = [
    [  # Ciudad 1
        [{"day": "Lunes", "temp": 78}, {"day": "Martes", "temp": 80}, {"day": "Miércoles", "temp": 82},
         {"day": "Jueves", "temp": 79}, {"day": "Viernes", "temp": 85}, {"day": "Sábado", "temp": 88},
         {"day": "Domingo", "temp": 92}],

        [{"day": "Lunes", "temp": 76}, {"day": "Martes", "temp": 79}, {"day": "Miércoles", "temp": 83},
         {"day": "Jueves", "temp": 81}, {"day": "Viernes", "temp": 87}, {"day": "Sábado", "temp": 89},
         {"day": "Domingo", "temp": 93}],

        [{"day": "Lunes", "temp": 77}, {"day": "Martes", "temp": 81}, {"day": "Miércoles", "temp": 85},
         {"day": "Jueves", "temp": 82}, {"day": "Viernes", "temp": 88}, {"day": "Sábado", "temp": 91},
         {"day": "Domingo", "temp": 95}],

        [{"day": "Lunes", "temp": 75}, {"day": "Martes", "temp": 78}, {"day": "Miércoles", "temp": 80},
         {"day": "Jueves", "temp": 79}, {"day": "Viernes", "temp": 84}, {"day": "Sábado", "temp": 87},
         {"day": "Domingo", "temp": 91}]
    ],
    [  # Ciudad 2
        [{"day": "Lunes", "temp": 62}, {"day": "Martes", "temp": 64}, {"day": "Miércoles", "temp": 68},
         {"day": "Jueves", "temp": 70}, {"day": "Viernes", "temp": 73}, {"day": "Sábado", "temp": 75},
         {"day": "Domingo", "temp": 79}],

        [{"day": "Lunes", "temp": 63}, {"day": "Martes", "temp": 66}, {"day": "Miércoles", "temp": 70},
         {"day": "Jueves", "temp": 72}, {"day": "Viernes", "temp": 75}, {"day": "Sábado", "temp": 77},
         {"day": "Domingo", "temp": 81}],

        [{"day": "Lunes", "temp": 61}, {"day": "Martes", "temp": 65}, {"day": "Miércoles", "temp": 68},
         {"day": "Jueves", "temp": 70}, {"day": "Viernes", "temp": 72}, {"day": "Sábado", "temp": 76},
         {"day": "Domingo", "temp": 80}],

        [{"day": "Lunes", "temp": 64}, {"day": "Martes", "temp": 67}, {"day": "Miércoles", "temp": 69},
         {"day": "Jueves", "temp": 71}, {"day": "Viernes", "temp": 74}, {"day": "Sábado", "temp": 77},
         {"day": "Domingo", "temp": 80}]
    ],
    [  # Ciudad 3
        [{"day": "Lunes", "temp": 90}, {"day": "Martes", "temp": 92}, {"day": "Miércoles", "temp": 94},
         {"day": "Jueves", "temp": 91}, {"day": "Viernes", "temp": 88}, {"day": "Sábado", "temp": 85},
         {"day": "Domingo", "temp": 82}],

        [{"day": "Lunes", "temp": 89}, {"day": "Martes", "temp": 91}, {"day": "Miércoles", "temp": 93},
         {"day": "Jueves", "temp": 90}, {"day": "Viernes", "temp": 87}, {"day": "Sábado", "temp": 84},
         {"day": "Domingo", "temp": 81}],

        [{"day": "Lunes", "temp": 91}, {"day": "Martes", "temp": 93}, {"day": "Miércoles", "temp": 95},
         {"day": "Jueves", "temp": 92}, {"day": "Viernes", "temp": 89}, {"day": "Sábado", "temp": 86},
         {"day": "Domingo", "temp": 83}],

        [{"day": "Lunes", "temp": 88}, {"day": "Martes", "temp": 90}, {"day": "Miércoles", "temp": 92},
         {"day": "Jueves", "temp": 89}, {"day": "Viernes", "temp": 86}, {"day": "Sábado", "temp": 83},
         {"day": "Domingo", "temp": 80}]
    ]
]

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for ciudad_idx, ciudad in enumerate(temperaturas):
    print(f"\n {ciudades[ciudad_idx]}:")
    for semana_idx, semana in enumerate(ciudad):
        # Sumar las temperaturas de la semana
        suma = sum(dia['temp'] for dia in semana)
        promedio = suma / len(semana)
        print(f"  - Semana {semana_idx + 1}: Promedio = {promedio:.2f}°C")


