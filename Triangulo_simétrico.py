#Este código dibujará un triángulo simétrico de las filas que deseemos

print ("*** Dibujar triángulo simétrico ***")

numero_filas = int(input("Proporciona el numero de filas: ")) #Solicitamos saber el numero de filas

for fila in range (1, numero_filas + 1): #Declaramos la variable fila como indice y declaramos que desde 1 hasta el numero de filas + 1

    espacios_blanco = " " * (numero_filas - fila) #Los espacios en blanco los asignamos con esta operacion
    asteriscos = "*" * (2 * fila - 1) #Los asteriscos los declaramos con esta otra operación
    print (f"{espacios_blanco}{asteriscos}") #Por ultimo imprimimos los espacios seguido de los asteriscos