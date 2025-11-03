#Ejercicio cajero automatico

#Vamos a crear un programa de cajero automatico que nos permita saber el saldo disponible, introducir o extraer dinero a voluntad

#Declaramos variables

salir = False
saldo = 1000
ingreso = None
extracto = None

while not salir: #Mientras la variable salir sea False, el ciclo se repite

    print ("Elige una opción:\n"
           "1. Consultar saldo.\n"
           "2. Ingresar dinero.\n"
           "3. Sacar dinero.\n"
           "4. Salir.\n")

    opcion = int(input("¿Que opción desea? ")) #Imprimimos menu y solicitamos saber la opcion

    if opcion == 1: #Con la opcion 1 solo imprimimos el saldo
        print(f"Tu saldo actual es de {saldo}€\n")

    elif opcion == 2: #Con la opcion 2 solicitamos saber el monto a ingresa y se lo sumamos al saldo incial
        ingreso = int(input("¿Cuanto dinero desea introducir?"))
        saldo += ingreso
        print(f"Tu saldo actual es de {saldo}€\n")

    elif opcion == 3: #Con la opcion 3 solicitamos saber el monto a extraer y solo permitimos si es menor al saldo disponible
        extracto = int(input("¿Cuanto desea extraer?"))
        if extracto > saldo:
            print("Error: No dispone de tanta cantidad\n")
        else:
            saldo -= ingreso
            print(f"Tu saldo actual es de {saldo}€\n")

    elif opcion == 4: #Con la opcion 4 declaramos la variable salir como True y rompemos el ciclo, terminando el programa
        salir = True
        print("Hasta pronto.\n")

