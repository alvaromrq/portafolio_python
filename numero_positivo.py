#Revisamos si un numero es positivo

print ("*** Revisión de numero ***")

numero = int(input("Por favor intruduzca un numero: "))

if numero > 0: #Primera condición, revisamos si es mayor a 0
    print (f"El numero {numero} es positivo")

elif numero < 0: #segunda condición, revisamos si es menor a 0
    print (f"El numero {numero} es negativo")

else: #Si no es ninguna de ellas, el numero es 0
    print(f"El numero es 0")