#Sistema de login

#Establecemos constantes de usuario y contraseña

USUARIO = "user"
CONTRASENA = "pass"

#Solicitamos introducir usuario y contraseña

usuario = input("Usuario: ").lower().strip()
contrasena = input("Contraseña: ").lower().strip()

#Comparamos los valores de las variables con las constantes y segun que situación imprimimos una cosa u otra

if usuario == USUARIO and contrasena == CONTRASENA:
    print("Bienvenido a su perfil.")

elif usuario == USUARIO and not contrasena == CONTRASENA:
    print("Contraseña incorrecta.")

elif not usuario == USUARIO and contrasena == CONTRASENA:
    print("Usuario incorrecto.")

else:
    print("Usuario y contraseña incorrectos.")

