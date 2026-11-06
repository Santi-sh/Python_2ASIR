#📝 Actividad evaluable - b1_9_analizador_notas.py

#Crea un script que:

#    Pida al usuario tres notas.
#    Calcule el promedio.
#    Introduzca un error lógico en el cálculo (como en el ejemplo anterior).
#    Usa IntelliJ en modo depuración para encontrar y corregir el error.
#    Añade un docstring al inicio explicando qué hacía mal el programa y cómo se corrigió.


# 1. Pide al usuario tres notas por teclado y las convierte a decimal (float)
nota_1 = float(input("Introduce la primera nota: "))
nota_2 = float(input("Introduce la segunda nota: "))
nota_3 = float(input("Introduce la tercera nota: "))

# 3. Error lógico intencionado (para mostrar qué fallaba):
# promedio = nota_1 + nota_2 + nota_3 / 3

# 2 y 4. Cálculo correcto del promedio tras corregir el error lógico con el depurador
promedio = (nota_1 + nota_2 + nota_3) / 3

# Mostrar el resultado final formateado a dos decimales
print(f"El promedio de las tres notas es: {promedio:.2f}")
