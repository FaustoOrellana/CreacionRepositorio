# Ejemplo completo de Escritura y Lectura de Archivos en Python

# Nombre del archivo
file_name = "my_notes.txt"

# ----------------------------
# Escritura en el archivo
# ----------------------------

# Modo de apertura: "w" para escritura (write)
archivo_escritura = open(file_name, "w")

# Metodo write(): escribir líneas individuales
archivo_escritura.write("Nota 1: Terminar la práctica de programación.\n")
archivo_escritura.write("Nota 2: Revisar apuntes de la clase de redes.\n")

# Metodo writelines(): escribir una lista de líneas
notas_adicionales = [
    "Nota 3: Estudiar para el examen de Python.\n",
    "Nota 4: Subir tarea a GitHub antes del viernes.\n"
]
archivo_escritura.writelines(notas_adicionales)

# Cerramos el archivo de escritura
archivo_escritura.close()

# ----------------------------
# Lectura del archivo
# ----------------------------

# Modo de apertura: "r" para lectura (read)
archivo_lectura = open(file_name, "r")

# Mostrar contenido completo usando read()
contenido_completo = archivo_lectura.read()
print("Contenido completo del archivo my_notes.txt:")
print(contenido_completo)

# Reiniciamos el cursor al principio del archivo
archivo_lectura.seek(0)

# Leer línea por línea usando readline()
print("Leyendo línea por línea con readline():")
linea = archivo_lectura.readline()
while linea:
    print(linea.strip())  # Elimina saltos de línea al final
    linea = archivo_lectura.readline()

# Cerramos el archivo de lectura
archivo_lectura.close()
