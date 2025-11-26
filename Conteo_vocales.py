#Contar vocales en un ciclo FOR

cadena = "Hola Mundo" #Declaramos la variable cadena con Hola Mundo
vocales = "aeiouAEIOU" #Declaramos las vocales que hay, tanto minus como mayus
contador = 0 #Declaramos un contador

for letra in cadena: #Declaramos un ciclo for para la cadena
    if letra in vocales: #Indicamos que cada letra pase se compare con lo que hay en vocales
        contador += 1 #Si la letra esta en vocales, añade +1 a contador
print (contador) #imprimimos contador tras el conteo
