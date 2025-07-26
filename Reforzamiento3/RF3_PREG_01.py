# PREGUNTA N1
# ROGER VERA
# /07/2025

#Variables

tipo_cambio=3.52
# TIPO DE CAMBIO

print("Convierte SOLES en Dolares")
print("Tipo de Cambio :", tipo_cambio)
# Solicitar datos al usuario
soles1 = input("Ingrese monto 1 en soles: ")
soles2 = input("Ingrese monto 2 en soles: ")
soles3 = input("Ingrese monto 3 en soles: ")

#Calculo de Float
dolares1 = float(soles1) / float(tipo_cambio)
dolares2 = float(soles2) / float(tipo_cambio)
dolares3 = float(soles3) / float(tipo_cambio)

print("Resultado 1: por S/.{} soles recibes $/ {} dolares".format(soles1, dolares1))
print("Resultado 2: por S/.{} soles recibes $/ {} dolares".format(soles2, dolares2))
print("Resultado 3: por S/.{} soles recibes $/ {} dolares".format(soles3, dolares3))
