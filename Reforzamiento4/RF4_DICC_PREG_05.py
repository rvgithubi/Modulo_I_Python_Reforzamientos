datos_personales = {
    "nombre": "Juan Pérez",
    "edad": 25,
    "ciudad": "Lima",
    "profesion": "Ingeniero"
}

# 1. Agregar la carrera al diccionario
datos_personales["carrera"] = "Ingeniería de Sistemas"

# 2. Crear variables para los valores específicos
nombre = datos_personales["nombre"]
carrera = datos_personales["carrera"]

# 3. Mostrar los valores en consola
print("Valores importantes:")
print(f"Nombre: {nombre}")
print(f"Carrera: {carrera}")

# 4. Opcional: Mostrar el diccionario completo actualizado
print("\nDiccionario completo actualizado:")
print(datos_personales)