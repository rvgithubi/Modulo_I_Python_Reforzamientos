"""Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tienes. """


empleado = {"nombre": "Roger Vera","edad": 28,"salario": 3800.50,"departamento": "Informatica"}

lista = list(empleado.items())

print(type(lista))
print(lista)

for elemento in lista:
    print(type(elemento), elemento)
