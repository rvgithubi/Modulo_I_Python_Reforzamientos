# PREGUNTA N3
# ROGER VERA
# 25/07/2025


print("Verificador de múltiplos\n")
# Solicitar datos al usuario
num1 = float(input("Ingrese el primer número (flotante): "))
num2 = float(input("Ingrese el segundo número (flotante): "))

# Convertir a enteros
entero1 = int(num1)
entero2 = int(num2)

# Validacion Divisor mayor a Cero
if entero2 == 0:
    print("\nError: No se puede dividir por cero")
else:
    if entero1 % entero2 == 0:
        print("El numero {} es multiplo de {}".format(entero1, entero2))
    else:
        print("El numero {} no es multiplo de {}".format(entero1, entero2))

    # DETALLE De la Operacion

print("Se verificó la operacion realizada: {} % {} = {}". format(entero1,entero2,entero1 % entero2))
