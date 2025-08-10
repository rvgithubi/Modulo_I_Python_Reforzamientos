"""
Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado
insertados en la terminal
"""

numeros = []

print("ingresando los valores")
for i in range(10):
    numeros.append(int(input("ingrese el nombre {}: ".format(i+1))))

suma = sum(numeros)
media = suma/len(numeros)

print("la suma de los valores", suma)
print("la media de los valores", media)

for numero in range(len(numeros)):
    print(numeros[numero])
