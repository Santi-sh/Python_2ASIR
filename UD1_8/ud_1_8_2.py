# 📝 ACTIVIDAD FINAL BLOQUE 01 - b1_10_login.py


# Variables globales para almacenar el usuario registrado (simulación básica)
identifer = ""
password = ""
usuario_registrado = False

# Bucle principal para mantener el menú activo hasta que el usuario decida salir
opcion = ""
while opcion != "3":
    print("\n--- MENÚ PRINCIPAL ---")
    print("[1]. Registrarse")
    print("[2]. Iniciar sesión")
    print("[3]. Salir")

    opcion = input("¿Qué quieres hacer? [1] Registrarse  [2] Iniciar sesión  [3] Salir: ")

    # ---------------------------------------------------------
    # OPCIÓN 1: REGISTRO DE USUARIO
    # ---------------------------------------------------------
    if opcion == "1":
        print("\n--- REGISTRO DE NUEVO USUARIO ---")

        # Validación del identificador (correo electrónico)
        email_valido = False
        while not email_valido:
            nuevo_identifer = input("Introduce un nombre de usuario (email): ")

            # Comprobar reglas del identificador:
            # - Mínimo 3 caracteres
            # - Contener '@'
            # - Contener extensiones .com, .es o .net
            # - No contener símbolos especiales prohibidos (!@#$%&*?, etc.)
            simbolos_prohibidos = ["!", "@", "#", "$", "%", "&", "*", "?", ",", " "]
            tiene_simbolo_prohibido = any(
                simbolo in nuevo_identifer for simbolo in simbolos_prohibidos if simbolo != "@")

            # Verificamos que contenga alguna de las extensiones requeridas
            tiene_extension = nuevo_identifer.endswith((".com", ".es", ".net"))

            if len(nuevo_identifer) < 3:
                print("Error ❌. El identificador debe tener al menos 3 caracteres.")
            elif nuevo_identifer.count("@") != 1:
                print("Error ❌. El identificador debe contener exactamente un '@'.")
            elif not tiene_extension:
                print("Error ❌. Debe contener alguna de las extensiones: .com, .es, .net.")
            elif tiene_simbolo_prohibido:
                print("Error ❌. El identificador no debe contener símbolos especiales.")
            else:
                email_valido = True
                print("Identificador válido ✅")

        # Validación de la contraseña segura
        password_valida = False
        while not password_valida:
            nueva_password = input("Introduce una contraseña: ")

            # Comprobar reglas de la contraseña:
            # - Mínimo 8 caracteres
            # - Al menos una mayúscula
            # - Al menos un número
            # - Al menos un símbolo especial (!@#$%&*?, etc.)
            tiene_ocho_caracteres = len(nueva_password) >= 8
            tiene_mayuscula = any(c.isupper() for c in nueva_password)
            tiene_numero = any(c.isdigit() for c in nueva_password)
            simbolos_especiales = "._!@#$%&*?,"
            tiene_simbolo = any(c in simbolos_especiales for c in nueva_password)

            if not (tiene_ocho_caracteres and tiene_mayuscula and tiene_numero and tiene_simbolo):
                print("Contraseña insegura ❌. Debe tener al menos 8 caracteres, una mayúscula, un número y un símbolo.")
            else:
                password_valida = True
                print("Contraseña válida ✅")

        # Almacenar los datos en las variables del sistema
        identifer = nuevo_identifer
        password = nueva_password
        usuario_registrado = True
        print("Usuario registrado con éxito ✅")

    # ---------------------------------------------------------
    # OPCIÓN 2: INICIO DE SESIÓN
    # ---------------------------------------------------------
    elif opcion == "2":
        print("\n--- INICIO DE SESIÓN ---")

        # Comprobar si hay algún usuario registrado previamente
        if not usuario_registrado:
            print("No hay ningún usuario registrado en el sistema. Regístrate primero (opción 1).")
            continue

        usuario_ingresado = input("Introduce tu usuario: ")

        # Verificar si el usuario (email) existe en el sistema
        if usuario_ingresado != identifer:
            print("Acceso denegado ⛔. El usuario no existe.")
        else:
            # Control de intentos para la contraseña (máximo 3)
            intentos_maximos = 3
            intentos_actuales = 0
            acceso_concedido = False

            while intentos_actuales < intentos_maximos and not acceso_concedido:
                contrasena_ingresada = input("Introduce tu contraseña: ")

                if contrasena_ingresada == password:
                    print(f"Acceso concedido ✅. Bienvenida, {identifer.split('@')[0]}.")
                    acceso_concedido = True
                else:
                    intentos_actuales += 1
                    if intentos_actuales < intentos_maximos:
                        print(f"Acceso denegado ⛔. Intento {intentos_actuales}/3")
                    else:
                        print(f"Acceso denegado ⛔. Intento {intentos_actuales}/3")
                        print("Demasiados intentos fallidos 🚫. Regresando al menú principal.")

    # ---------------------------------------------------------
    # OPCIÓN 3: SALIR
    # ---------------------------------------------------------
    elif opcion == "3":
        print("\nSaliendo del programa. ¡Hasta pronto!")

    # ---------------------------------------------------------
    # OPCIÓN NO VÁLIDA
    # ---------------------------------------------------------
    else:
        print("\nOpción no válida ❌. Por favor, elige una opción entre 1 y 3.")