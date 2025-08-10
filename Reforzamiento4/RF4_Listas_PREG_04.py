""" Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y luego esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola. """


lista = ["roger","luis","miguel","barto","julio"]

nombre = input("ingresa el nombre del estudiante: ").lower()

if nombre in lista:
 #   while nombre not in lista:
    lista.remove(nombre)
    print("el estudiante ", nombre.capitalize(), "ya existe")
    print("el nombre eliminado", nombre)

else:
    lista.append(nombre)
    print("el nombre AGREGADO", nombre)
#while nombre in lista:


print("Lista de Actualizada de estudiante", lista)

