# 📝 Actividad evaluable b1_4_login
# Crea un script que:

#    Guarde en variables:

#    usuario_correcto = "admin"
#    contrasena_correcta = "1234"

#    Pida al usuario con input() un nombre y contraseña.

#    Use operadores de comparación y lógicos para verificar:
#        Si ambos coinciden → mostrar "Acceso concedido".
#        Si no → mostrar "Acceso denegado"

usuario_correcto = "admin"
contrasena_correcta = 1234

usuario = input("Usuario: ")
contrasena = input("Contraseña:")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Correcto")
else:
    print("Incorrecto")


