# PREGUNTA N1
# ROGER VERA
# /07/2025


# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular IMC
imc = peso / (altura ** 2)

print("\n---------------------------------")
print("El Resultado para {}:".format(nombre))
print("El IMC calculado es: ", format(imc,".2f"))

