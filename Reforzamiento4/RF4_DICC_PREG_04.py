

departamentos = {
    1: "Lima",
    2: "Arequipa",
    3: "Cusco",
    4: "Piura",
    5: "Lambayeque",
    6: "Puno"
}

# eliminamos key 3
del departamentos[3]
print("\nDiccionario después de eliminar:")
print(departamentos)

llave = len(departamentos.keys())
llave2 = list(departamentos.keys())
print(llave)
print(llave2)
print(llave2[-1])
print(llave2[1])
penultima = llave2[-2]
departamentos[penultima]="iquitos"
print(departamentos)
