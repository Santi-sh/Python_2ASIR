#📝 Actividad evaluable - b1_8_tabla_multiplicar.py

#En esta actividad deberás crear un programa en Python que:

#    Pida un número por teclado.
#    Muestre por pantalla su tabla de multiplicar (del 1 al 10).

#Requisitos

#Asegúrate de aplicar las siguientes buenas prácticas:

#    Incluir un docstring al inicio del programa que describa su propósito.
#    Añadir comentarios explicativos en las partes más importantes del código.
#   Utilizar nombres de variables siguiendo la guía PEP 8 (en minúsculas, descriptivos y con guiones bajos).

#Ejemplo de salida esperada

#Introduce un número: 5

#Tabla de multiplicar del 5:
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#...
#5 x 10 = 50


"""
Programa que solicita un número por teclado y
muestra por pantalla su tabla de multiplicar del 1 al 10.

"""

# Pedir un número entero por teclado al usuario y convertirlo a entero
numero_introducido = int(input("Introduce un número: "))

# Mostrar el título de la tabla correspondiente
print(f"Tabla de multiplicar del {numero_introducido}:")

# Bucle para recorrer los números del 1 al 10 y mostrar el resultado
for i in range(1, 11):
    resultado = numero_introducido * i
    print(f"{numero_introducido} x {i} = {resultado}")

