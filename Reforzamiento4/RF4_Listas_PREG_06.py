"""Tiene una lista de invitados que llegaron a una boda de acuerdo a su orden
de llegada:
guests = [“Ana”, “Katherine”, “Pedro”, “Luis”, “Raúl”, “Fiorella”, “Miguel”]
Se requiere reorganizar esta lista.
Primero los que tienen número impar y en el orden que fueron llegando
Segundo las personas que tienen número par de letras
Input: [“Ana”, “Pedro”, “Raúl”, “Fiorella”, “Katherine”, “Miguel”, “Luis”]
Output: [“Ana”, “Pedro”, ”Katherine”, “Raúl”, “Fiorella”, “Miguel”, “Luis”]"""

lista = ["Ana","Katherine","Pedro","Luis","Raúl","Fiorella","Miguel"]

lista_par = []
lista_impar = []

for i in lista:
    if len(i) % 2 != 0:
        lista_impar.append(i)
        print("Impar " ,lista_impar)
    else:
        lista_par.append(i)

lista_actual= lista_impar + lista_par

print(lista_actual)
