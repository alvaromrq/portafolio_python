#Juego numero secreto

from random import randint #Importamos funcion randint

#Declaramos variables a utilizar
respuesta = None
conteo = 0

aleatorio = randint(1, 50) #Generamos un numero aleatorio entre 1 y 50

print("Bienvenido al juego de adivinar el numero!\n")


while respuesta != aleatorio and conteo < 10: #Mientras el numero respuesta sea distinto al generado y numero de intentos sea inferior a 10 se ejecuta el ciclo

   respuesta = int(input("Por favor introduce un número del 1 al 50: ")) #Solicitamos respuesta

   if respuesta > aleatorio: #Si el numero es mayor al generado, indicamos que es menor
       print("El numero no es correcto, es un numero menor a ese.\n")
       conteo += 1 #Sumamos conteo de fallos

   elif respuesta < aleatorio: #Si el numero es menor al generado, indicamos que es mayor
       print("El numero no es correcto, es un numero mayor a ese.\n")
       conteo += 1 #Sumamos conteo de fallos

   elif respuesta == aleatorio: #Si es correcto indicamos que ha ganado
       print("¡¡¡El numero es correcto, has ganado!!!\n")
       print(f"El numero de intentos ha sido de: {conteo}")

   else:
       print("Error: numero no valido.\n")

else:
    print("Has perdido...") #Si se acaban los intentos declaramos fallo





