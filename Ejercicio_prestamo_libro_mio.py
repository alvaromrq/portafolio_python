#Ejercicio de préstamo de libros, solo se prestara si la persona reside a 3km o menos o tiene credencial de estudiante

credencial = input("¿Tiene credencial de estudiante? (SI/NO) ") #Preguntamos si tiene credencial
credencial_ = credencial.strip().lower() #Retiramos espacios y colocamos la cadena en minuscula
distancia = int(input("¿A que distancia reside en KM? ")) #Solicitamos saber la distancia como numero entero con INT

credencial_ok = credencial_ == "si" #Comparamos con "si" para  obtener un valor booleano de la respuesta
distancia_ok = distancia <= 3 #Comprobamos si la distancia es menor o igual a 3km

resultado = credencial_ok or distancia_ok #Comparamos variables con OR
print(f"¿Apto para préstamo? {resultado}")