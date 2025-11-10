#Validador de passwords

print("Para cambiar las credenciales de su cuenta:\n"
      "El password introducido debe tener al menos 6 caracteres.\n") #Informamos de las condiciones del password

password = input("Por favor, intruzca su password: ") #Solicitamos password

while len (password) < 6: #Mientras el valor del password sea inferior a 6, el ciclo se repite (con "len" vemos la longitud de la variable)

        print("Error, password no valido") #Si es menor a 6, devolvemos error y solicitamos nuevo pass
        password = input("Por favor, intruzca nuevamente su password: ")

else:
        print("Su password se ha cambiado con éxito") #Si es igual o mayor a 6, devolvemos mensaje de exito