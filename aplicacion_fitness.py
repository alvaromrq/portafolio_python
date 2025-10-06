#Aplicación fitness

print ("*** App fitness ***")

#Establecemos las constantes de minimo de pasos y caloria por paso

META_PASOS = 10000
CALORIA_PASO = 0.04

#Solicitamos saber nombre de la persona y cuantos pasos hizo

nombre = input("¿Cual es su nombre? ")
pasos = int(input("¿Cuantos pasos ha caminado hoy? "))

#Declaramos el valor de las calorias quemadas en funcion de los pasos hechos, tambien comparamos si se llegó al minimo de pasos

calorias = pasos * CALORIA_PASO
meta = pasos >= META_PASOS
meta_alcanzada = "Sigue asi!" if meta else "Hay que mejorar..."

#Si se llego al minimo, imprimimos una felicitación y las calorias quemadas, sino solo las calorias quemadas

if meta:
    print(f"\nEnhorabuena {nombre}, usted ha cumplido el minimo de pasos diario, ha quemado {calorias} cal.")
    print(meta_alcanzada)

else:
    print(f"\nHola {nombre}, Lamentablemente no ha llegado al minimo de pasos diario, no obstante ha quemado {calorias} cal.")
    print(meta_alcanzada)