"""Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado. """


empleado = {"nombre": "Roger Vera","edad": 28,"salario": 3800.50,"departamento": "Informatica"}

empleado["dni"] = "41356521"

print(empleado["salario"])
print(empleado["dni"])

del empleado["edad"]
print("Diccionario Actualizado")
print(empleado)