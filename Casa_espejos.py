#Queremos entrar a la casa de los espejos, pero para ello se debe cumplir: tener mas de 10 años y no darte miedo la oscuridad

print("*** Bienvenido a la casa de los espejos ***")

edad = int(input("¿Cuantos años tienes? ")) #Solicitamos saber la edad
miedo = input("¿Te da miedo la oscuridad? (Si/No): ") #Solicitamos saber si le da miedo la oscuridad
confirmacion = miedo.lower().strip() == "si" #Guardamos el valor booleano de miedo en otra variable


if edad >= 10 and not confirmacion: #Si la edad es superior a 10 y NO le da miedo la oscuridad (para saberlo negamos la variable confirmacion) puede pasar
    print("Puedes acceder")

else: #Si no se cumple lo anterior no puede pasar
    print("No puedes acceder")