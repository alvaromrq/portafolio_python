#Tienda en línea

print ("*** Bienvenido a la tienda online ***")

#Solicitamos las entradas del importe de compra y si es miembro

importe = float(input("\nPor favor introduzca el importe de compra: "))
miembro = input("¿Es usted miembro? ").lower().strip()

#Declaramos variables de descuento

descuento_10 = importe / 100 * 10
descuento_5 = importe / 100 * 5

#Si es miembro y ha gastado 100€ o mas, se le hace un 10% de descuento

if importe >= 100 and miembro == "si":
    print("\nEnhorabuena tiene un descuento del 10%")
    print(f"Total sin descuento: {importe:.2f}€" #Añadimos 2f, para que solo salgan 2 cifras decimales
          f"\nTotal descontado: {importe - descuento_10:.2f}€")

#Si es miembro y pero no ha llegado a gastar 100€, se le hace un 5% de descuento

elif importe < 100 and miembro == "si":
    print("\nEnhorabuena tiene un descuento del 5%")
    print(f"Total sin descuento: {importe:.2f}€"
          f"\nTotal descontado: {importe - descuento_5:.2f}€")

#Si no es ninguno de los dos casos anteriores, no le descontamos nada

else:
    print("\nLamentablemente no dispone de descuento")
    print(f"El total asciende a: {importe:.2f}€")