#Ejercicio descuento de supermercado, si el numero de articulos es mayor o igual a 10 y tiene membresia vip, se ofrece descuento

print ("*** Bienvenido a su área de cliente ***")

articulos = int(input("Por favor, ingrese el numero de articulos que ha comprado: ")) #Preguntamos numero de articulos precedido de INT para que el valor introducido sea numero entero
vip = input("¿Cuenta con membresía VIP? (SI/NO) ") #Preguntamos si se dispone de membresía
vip_ = vip.lower().strip() #Hacemos que el input se ponga en minusculas y sin espacios


articulos_ok = articulos >= 10 #Comparamos si los articulos comprados son iguales o mayores que 10
vip_ok = vip_ == "si" #Comparamos si la cadena introducida es igual a "si"

descuento = articulos_ok and vip_ok #Indicamos con AND que se tienen que cumplir ambas condiciones
print(f"¿Tiene usted descento? {descuento}")
