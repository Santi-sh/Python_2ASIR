# 📝 Reto a entregar — contador.py

# Crea un script que:

#    Defina una variable global contador = 0.

#    Implemente tres funciones:
#        incrementar() → suma 1 al contador.
#        decrementar() → resta 1 al contador.
#        mostrar_contador() → imprime el valor actual.

#    Use la palabra clave global para modificar el contador dentro de las funciones.

#    Desde el programa principal, llama a las funciones en este orden:
#        incrementar() dos veces.
#        decrementar() una vez.
#        mostrar_contador().

#    Añade un docstring en cada función explicando lo que hace.

# Definición de la variable global

contador = 0

def incrementar():
    # Incrementa en 1 el valor de la variable global contador.
    global contador
    contador += 1

def decrementar():
    # Resta 1 al valor de la variable global contador.
    global contador
    contador -= 1

def mostrar_contador():
    global contador
    # Imprime en la consola el valor actual de la variable global contador.
    print(f"El valor actual del contador es: {contador}")

# Programa principal (Orden de ejecución solicitado)
for i in range(10):
    incrementar() # Llama a incrementar por primera vez (contador = 1)
    mostrar_contador()
decrementar()       # Llama a decrementar una vez (contador = 1)
mostrar_contador()   # Muestra el resultado final

