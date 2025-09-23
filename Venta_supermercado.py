#La pagina del supermercado nos pregunta los valores que debemos introducir para generar un ticket final de compra con impuestos y descuento

print("*** Bienvenido al sistema online de su supermercado ***")

#Nos preguntara el valor de los productos que llevamos en la cesta

natillas = float(input("\nPor favor introduzca el valor de las natillas: "))
camiseta = float(input("Por favor introduzca el valor de la camiseta: "))
leche = float(input("Por favor introduzca el valor de la leche: "))
queso = float(input("Por favor introduzca el valor del queso: "))
descuento_porcentaje = int(input("¿Desea aplicar algun descuento? indique %: ")) #Solicitamos el descuento que se debe aplicar

subtotal = natillas + camiseta + leche + queso #Sumamos los valores introducidos

descuento = subtotal * (descuento_porcentaje / 100) #Aplicamos el descuento al total sin impuestos

total_sin_impuestos = subtotal - descuento #Restamos impuestos

impuestos = (total_sin_impuestos / 100 * 21) #Calculamos los impuestos, obviando que son un 21%

total_con_impuestos = total_sin_impuestos + impuestos #Sumamos los impuestos al total

#Imprimimos el valor final de compra

print (f"Impuestos (21%): {impuestos}")


print (f"El total sin impuestos asciende a: {total_sin_impuestos} \nSe añade un 21% de impuestos, precio final: {total_con_impuestos}")
