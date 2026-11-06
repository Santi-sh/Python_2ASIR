# 📝 ACTIVIDAD FINAL BLOQUE 01 - b1_10_login.py

# Variables globales para almacenar el usuario registrado
identifer = ""
password = ""
usuario_registrado = False

# Bucle principal para mantener el menú activo hasta que se elija salir
opcion = ""
while opcion != "3":
    print("\n==============================")
    print("         MENÚ PRINCIPAL       ")
    print("==============================")
    print("[1]. Registrarse")
    print("[2]. Iniciar sesión")
    print("[3]. Salir")

    opcion = input("¿Qué quieres hacer? [1] Registrarse  [2] Iniciar sesión  [3] Salir: ")

    # ---------------------------------------------------------
    # OPCIÓN 1: REGISTRO DE USUARIO
    # ---------------------------------------------------------
    if opcion == "1":
        print("\n--- REGISTRO DE NUEVO USUARIO ---")

        # Validación paso a paso del correo (identifer)
        email_valido = False
        while not email_valido:
            nuevo_identifer = input("Introduce un nombre de usuario (email): ")

            # 1. Comprobar longitud mínima (al menos 3 caracteres)
            if len(nuevo_identifer) < 3:
                print("Error. El identificador debe tener al menos 3 caracteres.")
                continue

            # 2. Comprobar que contenga exactamente una arroba
            if nuevo_identifer.count("@") != 1:
                print("Error. El identificador debe contener exactamente un '@'.")
                continue

            # 3. Comprobar que termine en una extensión válida
            if not nuevo_identifer.endswith((".com", ".es", ".net")):
                print("Error. Debe terminar con .com, .es o .net.")
                continue

            # 4. Comprobar símbolos prohibidos (bucle tradicional fácil de leer)
            simbolos_prohibidos = ["!", "#", "$", "%", "&", "*", "?", ",", " "]
            tiene_simbolo_prohibido = False
            for simbolo in simbolos_prohibidos:
                if simbolo in nuevo_identifer:
                    tiene_simbolo_prohibido = True
                    break # Salimos del bucle en cuanto encontramos un símbolo prohibido

            if tiene_simbolo_prohibido:
                print("Error. El identificador no debe contener símbolos especiales.")
                continue

            # Si pasa todas las comprobaciones, el correo es válido
            email_valido = True
            print("Identificador válido")

        # Validación paso a paso de la contraseña
        password_valida = False
        while not password_valida:
            nueva_password = input("Introduce una contraseña: ")

            # 1. Comprobar longitud mínima (8 caracteres)
            if len(nueva_password) < 8:
                print("Contraseña insegura. Debe tener al menos 8 caracteres.")
                continue

            # 2. Comprobar si tiene al menos una mayúscula
            tiene_mayuscula = False
            for caracter in nueva_password:
                if caracter.isupper():
                    tiene_mayuscula = True
                    break

            if not tiene_mayuscula:
                print("Contraseña insegura. Debe contener al menos una letra mayúscula.")
                continue

            # 3. Comprobar si tiene al menos un número
            tiene_numero = False
            for caracter in nueva_password:
                if caracter.isdigit():
                    tiene_numero = True
                    break

            if not tiene_numero:
                print("Contraseña insegura. Debe contener al menos un número.")
                continue

            # 4. Comprobar si tiene al menos un símbolo especial
            simbolos_especiales = "._!@#$%&*?,"
            tiene_simbolo = False
            for caracter in nueva_password:
                if caracter in simbolos_especiales:
                    tiene_simbolo = True
                    break

            if not tiene_simbolo:
                print("Contraseña insegura. Debe contener al menos un símbolo especial.")
                continue

            # Si pasa todas las comprobaciones, la contraseña es válida
            password_valida = True
            print("Contraseña válida")

        # Guardar los datos en las variables del sistema
        identifer = nuevo_identifer
        password = nueva_password
        usuario_registrado = True
        print("¡Usuario registrado con éxito! 🎉")

    # ---------------------------------------------------------
    # OPCIÓN 2: INICIO DE SESIÓN
    # ---------------------------------------------------------
    elif opcion == "2":
        print("\n--- INICIO DE SESIÓN ---")

        # Comprobar si hay un usuario registrado previamente
        if not usuario_registrado:
            print("No hay ningún usuario registrado. Regístrate primero (opción 1).")
            continue

        usuario_ingresado = input("Introduce tu usuario: ")

        # Verificar si el usuario introducido coincide
        if usuario_ingresado != identifer:
            print("Acceso denegado. El usuario no existe.")
        else:
            # Control de intentos para la contraseña (máximo 3)
            intentos_maximos = 3
            intentos_actuales = 0
            acceso_concedido = False

            while intentos_actuales < intentos_maximos and not acceso_concedido:
                contrasena_ingresada = input("Introduce tu contraseña: ")

                if contrasena_ingresada == password:
                    # Extraer el nombre antes de la arroba para saludar
                    nombre_usuario = identifer.split("@")[0]
                    print(f"Acceso concedido. Bienvenida, {nombre_usuario}.")
                    acceso_concedido = True
                else:
                    intentos_actuales += 1
                    if intentos_actuales < intentos_maximos:
                        print(f"Acceso denegado. Intento {intentos_actuales}/3")
                    else:
                        print(f"Acceso denegado. Intento {intentos_actuales}/3")
                        print("Demasiados intentos fallidos 🚫. Regresando al menú principal.")

    # ---------------------------------------------------------
    # OPCIÓN 3: SALIR
    # ---------------------------------------------------------
    elif opcion == "3":
        print("\nSaliendo del programa. ¡Hasta pronto! 👋")

    # ---------------------------------------------------------
    # OPCIÓN NO VÁLIDA
    # ---------------------------------------------------------
    else:
        print("\nOpción no válida. Por favor, elige una opción entre 1 y 3.")