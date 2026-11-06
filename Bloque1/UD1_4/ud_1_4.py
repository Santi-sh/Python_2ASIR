# 📝 Actividad evaluable - b1_5_1_calculadora_condicional

# Crea un script que:

#    Pida al usuario dos números (num1, num2).
#    Pida elegir una operación: suma, resta, multiplicación o división.
#    Use if...elif...else para realizar la operación seleccionada.
#    Si elige una opción inválida, mostrar "Operación no reconocida".

# 👉 Ejemplo de salida:

# Elige operación (suma, resta, multiplicacion, division): suma
# Resultado: 25

num1 = int(input("dime el primer número: "))
num2 = int(input("dime el segundo número: "))

operacion = input("Elige operación (suma, resta, multiplicacion, division): ")
if operacion == "suma":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")

elif operacion == "resta":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")

elif operacion == "multiplicacion":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")

elif operacion == "division":
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")

else:
    print("Operación no reconocida")

