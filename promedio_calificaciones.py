#Vamos a realizar un programa que realice un promedio de las calificaciones obtenidas mediante una lista

print ("*** promedio de calificaciones ***")

calificaciones = [] #Declaramos una lista vacia

numero_calificaciones = int(input("¿Cuantas calificaciones vamos a evaluar? ")) #Solicitamos saber el total de calificaciones

for indice in range(numero_calificaciones): #Iteramos las calificaciones de la lista
    calificacion = float(input(f"Introduce la calificación {indice + 1} obtenida: ")) #Solicitamos cada calificacion por separado
    calificaciones.append(calificacion) #Añadimos cada calificacion a la lista

print (f"\nLas calificaciones obtenidas son: {calificaciones}") #Imprimimos lista de calificaciones


promedio = sum(calificaciones) / numero_calificaciones #Realizamos el promedio, con SUM sumamos todos los valores de la lista y los dividimos por el numero de calificaciones a promediar
print (f"\nEl promedio de calificaciones es: {promedio}") #Imprimimos el promedio