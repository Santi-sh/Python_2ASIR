# 📝 Actividad evaluable - b1_5_2_calculadora_switch.py

# Crea un script que:

#    Pida al usuario dos números (num1, num2).
#    Pida elegir una operación: suma, resta, multiplicación o división.
#    Use match-case para realizar la operación seleccionada.
#    Si elige una opción inválida, mostrar "Operación no reconocida".

# 👉 Ejemplo de salida:

# Elige operación (suma, resta, multiplicacion, division): multiplicacion
# Resultado: 50

num1 = int(input("dime el primer número: "))
num2 = int(input("dime el segundo número: "))

operacion = input("Elige operación (suma, resta, multiplicacion, division): ")

match operacion :
    case "suma" :
        print(num1 + num2)
    case "resta" :
        print(num1 - num2)
    case "multiplicacion" :
        print(num1 * num2)
    case "division" :
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            print(num1 / num2)
    case _:
        print("Operación no reconocida")
