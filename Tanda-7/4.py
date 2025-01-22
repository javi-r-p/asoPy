# Simulación de inicio de sesión

usuarioValido = "usuario"
contraseniaValida = "contraseña"

intentos = 0
while intentos < 3:
    usuario = input("Usuario: ")
    contrasenia = input("Contraseña: ")
    if usuario == usuarioValido and contrasenia == contraseniaValida:
        print("Has iniciado sesión exitosamente.")
        break
    else:
        print("Credenciales incorrectas. Inténtalo de nuevo.")
        intentos += 1

if intentos == 3:
    print ("Has excedido el número de intentos.")