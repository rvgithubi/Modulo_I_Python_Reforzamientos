"""Crear un programa en Python donde tendrás una lista con 6 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista. """


lista  = ["lima","huancayo","arequipa","cusco","tacna","iquitos"]

tamano = len(lista)
print("Ingrese los departamentos\n")
print(tamano)
i=1
while i<=2:
    provincia = input("ingrese el departamento {}: ".format(i))
    if (i == 2):
            lista [1] = provincia
    else:
        lista.append(provincia)
    i+=1
print(lista)
