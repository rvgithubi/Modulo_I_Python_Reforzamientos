"""
1. Escribir un programa donde ingresarás el tamaño de la lista mediante
consola, este tamaño servirá para ingresar una cantidad X de nombres de
alumnos. Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de
la lista que fueron ingresados.  """
#RF4_Listas_PREG_01

tamano = input("ingresa la cantidad de nombres de la lista: ")
lista = []
for i in range(int(tamano)):
    nombre = input("ingrese nombres de la lista: ")
    lista.append(nombre)
    print(i)

for nombre1 in lista:
    print(nombre1)

print("lista actualizada : {}".format(lista))
print("tamaño de la lista :", len(lista))

