#Sistema que comparará el valor de usuario y pass si son iguales con los introducidos por el usuario

print("*** Sistema de autenticación ***")

#Declaramos el valor del usuario y contraseña en dos constantes

USUARIO = "User"
PASSWORD = "1234"

#Solicitamos que se introduzca usuario y contraseña, retiramos espacios que pueda haber con strip

usuario = input("Introduce tu usuario: ").strip()
password = input("Introduce tu contraseña: ").strip()

comparativa = USUARIO == usuario and password == PASSWORD #Hacemos la comparación de los datos introducidos, respecto a las constarntes y declaramos AND, ya que ambos deben ser correctos

print(f"¿Son correctas las credenciales? {comparativa}")