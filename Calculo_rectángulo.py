#Solicitamos al usuario que introduzca los valores de base y altura de un rectangulo para poder calcular su área y perímetro

print ("*** Calculo de área y perímetro de rectángulo ***")

#Solicitamos los valores de base y altura y los declaramos en float, para que puedan ser decimales

base = float(input("Introduzca el valor de la base en cm: "))
altura =float(input("Introduzca el valor de la altura en cm: "))

#Realizamos el calculo de base y perimetro con las formulas pertinentes

area = base * altura
perimetro = 2 * base + altura

print (f"\nEl valor de área es: {area} cm2 \nEl valor del perímetro es: {perimetro} cm") #Imprimos resultado