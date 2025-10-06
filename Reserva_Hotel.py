#Sistema de reserva de hoteles

print ("*** Bienvenido a su reserva de hoteles ***")

#Declaramos variables de costos de cada tipo de habitacion en funcion de si tiene vistas

VISTA_MAR = 200
NO_VISTA_MAR = 150

#Solicitamos datos

nombre = input("¿Cual es su nombre? ")
dias = int(input("¿Cuantos días se quedará? "))
habitacion = input("¿Quiere una habitación con vistas al mar? ").lower().strip()

#Con operador ternario, calculamos el costo en funcion de si se eligió vistas al mar o no

costo = dias * VISTA_MAR if habitacion == "si" else dias * NO_VISTA_MAR

#Imprimimos detalles

print ("\n---- Detalles de la reserva ----")
print (f"Cliente: {nombre}")
print(f"Días de estancia: {dias}")
print(f"Costo total: {costo}")
print(f"¿Tendra vistas al mar? {habitacion}")