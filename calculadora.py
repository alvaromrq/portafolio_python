#Vamos a crear una calculadora con el ciclo while

salir = False

while not salir: #Mientras salir sea Falso, se ejecuta el ciclo
    print("Escoja una opción:\n"
          "1. Suma\n"
          "2. Resta\n"
          "3. Multiplicación\n"
          "4. División\n"
          "5. Salir\n")

    opc = int(input("¿Que opción escoje? ")) #Pedimos una opcion de las ofrecidas

    if opc == 1: #Realizamos una operacion por cada opcion elegida
        valor1 = float(input("Valor 1: "))
        valor2 = float(input("Valor 2: "))
        resultado = valor1 + valor2
        print (f"Resultado: {resultado}")

    elif opc == 2:
        valor1 = float(input("Valor 1: "))
        valor2 = float(input("Valor 2: "))
        resultado = valor1 - valor2
        print (f"Resultado: {resultado}")

    elif opc == 3:
        valor1 = float(input("Valor 1: "))
        valor2 = float(input("Valor 2: "))
        resultado = valor1 * valor2
        print (f"Resultado: {resultado}")

    elif opc == 4:
        valor1 = float(input("Valor 1: "))
        valor2 = float(input("Valor 2: "))
        resultado = valor1 / valor2
        print (f"Resultado: {resultado}")

    elif opc == 5: #Si elegimos salir, salir lo ponemos como True y termina el ciclo
        salir = True
        print("Hasta pronto!")

    else:
        print("Error, selecciona otra opción.")