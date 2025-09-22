#Ejercicio generador de mails

#Declaramos las variables de entrada de texto
print("*** Generador de Email ***")

nombre = input("Nombre: ")
apellido = input("Apellidos: ")
nombre_empresa = input("Empresa: ")
dominio = input("Dominio: ")

#Retiramos espacios, ponemos en minuscula y sustituimos espacios por puntos

nombre_2 = nombre.strip().lower().replace(" ", ".")
apellido_2 = apellido.strip().lower().replace(" ", ".")
nombre_empresa2 = nombre_empresa.strip().lower().replace(" ", "") #En este caso reemplazamos el espacio por cadena vacia
dominio_2 = dominio.strip().lower().replace(" ", ".")

#Resultado final

email = f"Enhorabuena, tu nueva dirección Email es: {nombre_2}.{apellido_2}@{nombre_empresa2}{dominio_2}"
print(email)