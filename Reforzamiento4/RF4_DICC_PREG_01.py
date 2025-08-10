""" Crea correctamente un diccionario con los campos de: nombre, edad, salario
y edad. Convierte tu diccionario finalmente a una lista y muestra el resultado en la
terminal."""


empleado = {"nombre": "Juan Pérez","edad": 35,"salario": 4500.50, "departamento": "TI"}

lista = list(empleado.values())
lista1 = list(empleado.keys())
lista2 = list(empleado.items())

print(empleado)
print(lista)
print(lista1)
print(lista2)
