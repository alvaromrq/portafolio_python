#Sistema de costo de envios

print("*** Calculo de costos de envios ***")

#Declaramos las variables de costo de los envios nacional e internacional

NACIONAL = 10
INTERNACIONAL = 22

#Solicitamos saber los valores de peso del paquete y si es nacional o internacional

destino = input("por favor, indique tipo de envio (Nacional/Internacional): ").lower().strip()
peso = float(input("Por favor, introduzca el peso del paquete: "))
total = None

if destino == "nacional":
    total = peso * NACIONAL #Hacemos el caculo en funcion de si es nacional
    print (f"El precio total de un envio nacional para {peso}kg es: {total:.2f}€")

elif destino == "internacional":
    total = peso * INTERNACIONAL #Hacemos el caculo en funcion de si es nacional
    print(f"El precio total de un envio internacional para {peso}kg es: {total:.2f}€")

else:
    print("Valor desconocido")