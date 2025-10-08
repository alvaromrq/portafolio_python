#Vamos a convertir una calificación numerica en una letra

print("*** calificaciones ***")

nota = float(input("Por favor, introduce tu nota: ")) #Solicitamos saber la nota
letra = None #Declaramos la variable como none, para poder asiganarle un valor variable segun que situacion

#Declaramos los escenarios para cada letra y hacemos que la variable "letra" cambie su valor en cada sitiuación

if nota >= 9 and nota <= 10:
    letra = "A"
    print (f"El equivalente a un {nota} es una {letra}")

elif nota >= 8 and nota < 9:
    letra = "B"
    print (f"El equivalente a un {nota} es una {letra}")

elif nota >= 7 and nota < 8:
    letra = "C"
    print(f"El equivalente a un {nota} es una {letra}")

elif nota >= 6 and nota < 7:
    letra = "D"
    print(f"El equivalente a un {nota} es una {letra}")

elif nota >= 0 and nota < 6:
    letra = "F"
    print(f"El equivalente a un {nota} es una {letra}")

else:
    print("Valor desconocido")