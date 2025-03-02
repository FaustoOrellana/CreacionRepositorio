# Matriz 3x3
matriz = [
    [4, 7, 1],
    [8, 3, 6],
    [2, 9, 5]
]

# Valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar: "))

# Función
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return None

# Llamar a la función de búsqueda
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar el resultado
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_buscado} no está en la matriz.")
