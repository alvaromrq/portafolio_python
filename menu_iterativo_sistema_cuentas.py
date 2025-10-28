#Vamos a crear un menu iterativo donde se daran 3 opciones, cada una con un valor

print("*** Sistema de cuentas ***")

salir = False #Declaramos una variable booleana para que mientras sea falsa se ejecute el ciclo

while not salir: #Declaramos que el ciclo while funcionara mientras salir sea falso (negada)

    print("Menu:\n"
          "1.Crear cuenta\n"
          "2.Eliminar cuenta\n"
          "3.Salir\n")
    opcion = int(input("Escoje una opción: ")) #Imprimimos el menu y solicitamos la opción escogida

#Declaramos un if por cada opción dentro del ciclo while

    if opcion == 1:
        print("Creando cuenta...\n")

    elif opcion == 2:
        print("Eliminando cuenta...\n")

    elif opcion == 3:
        print("Saliendo del sistema.")
        salir = True #si se selecciona la opcion de salir, declaramos la variable salir como true y por tanto, se acaba el programa

    else:
        print("Valor desconocido\n")
        
else:
    print("Terminando sistema de cuentas")