#Segun el mes introducido nos dará la estación del año en la que estamos

print("*** Estación del año ***")

#Solicitamos saber el mes

estacion = int(input("Por favor, introduce el nº de mes en el que estamos: "))

#Dependiendo del mes introducido comprobamos con que valor de mes coincide

if estacion == 1 or estacion == 2 or estacion == 12:
    print ("Estamos en invierno")

elif estacion == 3 or estacion == 4 or estacion == 5:
    print ("Estamos en primavera")

elif estacion == 6 or estacion == 7 or estacion == 8:
    print ("Estamos en verano")

elif estacion == 9 or estacion == 10 or estacion == 11:
    print ("Estamos en otoño")

else:
    print ("Estacion desconocida")

