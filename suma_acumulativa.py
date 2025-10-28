print ("*** Suma acumulativa ***")

#Declaramos variables

MAXIMO = 5 #Constante de maximo
numero = 1 #variable de comparativa
acumulador = 0 #variable de acumulación

while numero <= MAXIMO: #Mientras la variable numero sea igual o inferior a constante MAXIMO el ciclo se ejecuta
    print (f"(Acumulador suma + numero) -- {acumulador} + {numero}")

    acumulador += numero #Por cada ciclo, a la variable acumulador se le suma la variable numero
    numero += 1 #Por cada ciclo a la variable numero se le suma 1

    print (f"La acumulación hasta el momento es: {acumulador}\n")


print (f"\nResultado de la suma acumulada: {acumulador}") #Ejecutamos esta linea una vez se haya completado el ciclo while