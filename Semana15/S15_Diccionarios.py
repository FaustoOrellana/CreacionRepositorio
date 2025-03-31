print("\n=== DICCIONARIOS ===")
# Crear el diccionario con información ficticia
info_personal = {
    "nombre": "Andres Orellana",
    "edad": 30,
    "ciudad": "Machala",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
info_personal["ciudad"] = "Pasaje"
print("Después de modificar 'ciudad':", info_personal)

# Agregar una nueva clave-valor "profesion"
info_personal["profesion"] = "Desarrollador de Software"
print("Después de agregar 'profesion':", info_personal)

# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in info_personal:
    info_personal["telefono"] = "0999672440"
    print("Después de verificar si existe 'telefono':", info_personal)

# Eliminar la clave "edad"
del info_personal["edad"]
print("Después de eliminar 'edad':", info_personal)

# Imprimir el diccionario final
print("Resultado final:", info_personal)