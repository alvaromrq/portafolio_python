#La pagina del supermercado nos pregunta los valores que debemos introducir para generar un ticket final de compra con impuestos

print("*** Bienvenido al sistema online de su supermercado ***")

#Nos preguntara el valor de los productos que llevamos en la cesta

natillas = float(input("\nPor favor introduzca el valor de las natillas: "))
camiseta = float(input("Por favor introduzca el valor de la camiseta: "))
leche = float(input("Por favor introduzca el valor de la leche: "))
queso = float(input("Por favor introduzca el valor del queso: "))

total_sin_impuestos = natillas + camiseta + leche + queso #Sumamos los valores introducidos

impuestos = (total_sin_impuestos / 100 * 21) #Calculamos los impuestos, obviando que son un 21%

total_con_impuestos = total_sin_impuestos + impuestos #Sumamos los impuestos al total del valor de los productos

#Imprimimos el valor final de compra

print (f"Impuestos (21%): {impuestos}")

print (f"El total sin impuestos asciende a: {total_sin_impuestos}, sumando un 21% de impuestos, se queda en: {total_con_impuestos}")