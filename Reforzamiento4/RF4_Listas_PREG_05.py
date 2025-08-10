"""Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de
TI) y harás una copia donde adrede agregarás nombres que estarán
repetidos (mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también te mostrará la lista
inicial """

lista = []
tamano = int(input("ingresa el  tamaño de la lista: "))
for i in range(tamano):
    compania = input("Ingrese el número de compañías a registrar {}: " .format(i+1))
    lista.append(compania)
copialista = lista.copy()

repetidos = int(input("¿Cuántas compañías adicionales se agregan?: "))
for i in range(repetidos):
    compania = input(f"Ingrese compañía adicional {i+1}: ")
    copialista.append(compania)

lista_unica = list(set(copialista))

print("\nLista sin duplicados ({len(lista_unica)} compañías):")
for i, comp in enumerate(sorted(lista_unica), 1):
    print(f"{i}. {comp}")
