#📝 Actividad guiada — operaciones.py

#    Define una función sumar(a, b) que imprima la suma de dos números.
#    Define una función saludo_personal(nombre, saludo="Hola") que muestre un saludo personalizado.
#    Llama a ambas funciones con distintos parámetros desde el programa principal.

#👉 Objetivo: practicar parámetros posicionales y valores por defecto.
#💡 Reto a entregar — registro_usuario.py

#    Crea una función registrar_usuario(nombre, edad, ciudad="Madrid").
#    La función debe mostrar en pantalla: "Usuario: [nombre], Edad: [edad], Ciudad: [ciudad]".
#    Debe poder llamarse con:
#        Todos los argumentos posicionales.
#        Algún argumento omitido, usando el valor por defecto.
#        Argumentos nombrados en distinto orden.
#    Incluye un docstring en la función.
#    Desde el programa principal, llama a la función al menos 3 veces con diferentes combinaciones de argumentos.


def registrar_usuario(nombre, edad, ciudad="Madrid"):
    print (f"usuario: {nombre}, Edad: {edad}, Ciudad: {ciudad}")
# En esta llamada hemos puesto todos los argumentos posicionales.
registrar_usuario("Pepe", 20, "Huelva")
# En este ejemplo hacemos que haya un argumento omitido, en mi caso, la ciudad.
registrar_usuario("Juan", 30)
# En esta ultima llamada a la función he puesto un ejemplo donde ponemos los argumentos en distinto orden.
registrar_usuario(ciudad="Sevilla", nombre="José", edad=18)




