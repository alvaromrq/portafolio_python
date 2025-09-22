#Ejercicio generador de ID único

#Introducimos los valores e inportamos randint

from random import randint

#Establecemos inputs para nombre, apellido y año de nacimiento

print ("*** Generador de ID unico ***")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
ano = input("Año: ")
valor_random = randint(1000, 9999) #Declaramos una variable para darnos un valor random del 1000 al 9999

sub_nombre = nombre[0:2] #Elegimos los dos primeros digitos del nombre introducido, no se cuenta lo que haya escrito dentro del input, solo lo que introducimos, por lo que contamos desde el 0
sub_nombreup = sub_nombre.upper() #Ponemos en mayusculas los digitos introducidos

sub_apellido = apellido[0:2]
sub_apellidoup = sub_apellido.upper()

sub_ano = ano[0:2]

#Imprimimos el valor final

print(f"Hola Álvaro, tu ID unico es: {sub_nombreup}{sub_apellidoup}{sub_ano}{valor_random}")