#📝 Actividad evaluable - b1_7_filtrar_lista.py

#Crea un script que:

#    Defina una lista con al menos 6 nombres.
#    Recorra la lista con un bucle for.
#    Use continue para saltar los nombres que empiezan por la letra "A" (mayúscula o minúscula).
#    Muestre en pantalla solo los nombres que no empiecen por "A".
#    Añada un docstring explicando el propósito del programa y comentarios en las partes importantes del código.

#📌 Ejemplo de entrada/salida:

#lista = ["Ana", "Pedro", "Alba", "Lucía"]

#➡️ Resultado:

#Pedro
#Lucía

# definimos la lista con 6 nombres
lista = ["Ana", "Pedro", "Alba", "Lucía", "Carlos", "David"]

# hacemo el bucle for y añadimos el nombre.starswitch para añadir el filtro para los nombres que empiecen por A y a 
for nombre in lista:
    if nombre.startswith(("A", "a")):
        continue
    else:
        print(nombre)


