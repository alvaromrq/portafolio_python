#Vamos a crear una lista de suscriptores dinámica

print("*** Lista de suscriptores ***")

#suscriptores = {} #Definimos un diccionario vacio, asi no podemos definir un set vacio
suscriptores = set() #Para crear un set vacio, debemos poner la funcion set y establecer dos paréntesis, creamos el set suscriptores

numero_suscriptores = int(input("¿Cuantos suscriptores desea agregar? ")) #Generamos una variable para saber que numero de suscriptores queremos añadir

for _ in range(numero_suscriptores): #Utilizamos la funcion range para agregar suscrptores desde 0 al numero que hayamos puesto -1, utilizamos _ para omitir el indice
    suscriptores.add(input("Nuevo suscriptor: ")) #Con .add, añadimos valores al set suscriptores


#Vamos a verificar si el suscriptor esta en la lista y añadirlo

nuevo_suscriptor = input("Proporciona el nuevo suscriptor: ") #Declaramos una variable con un suscriptor a añadir

if nuevo_suscriptor in suscriptores: #Con if comparamos si el nuevo mail esta dentro (in) del set suscriptores
    print(f"\nEl suscriptor {nuevo_suscriptor} ya se encuentra suscrito.") #Si ya existe, indicamos que ya esta suscrito
else:
    suscriptores.add(nuevo_suscriptor) #Si no está, lo añadimos al set suscriptores con .add
    print(f"\nEl nuevo suscriptor se agregó a la lista: {suscriptores}") #Imprimimos la nueva lista


#Vamos a eliminar el suscriptor que queramos del set

suscriptor_a_eliminar = input("Proporciona el suscriptor a borrar: ") #Declaramos una variable con un suscriptor a borrar

if nuevo_suscriptor not in suscriptores: #Con if comparamos si el mail no esta dentro (in) del set suscriptores
    print(f"\nEl suscriptor {suscriptor_a_eliminar} no se encuentra suscrito.") #Si no existe, indicamos que no esta suscrito
else:
    suscriptores.remove(suscriptor_a_eliminar) #Si está, lo eliminamos del set lista con .remove
    print(f"\nEl suscriptor {suscriptor_a_eliminar}  se eliminó de la lista: {suscriptores}") #Imprimimos la nueva lista


#Verificamos la cantidad de suscriptores

print(f"\nLa cantidad total de suscriptores es: {len(suscriptores)}") #Con len, podemos ver el numero de componentes del set


#Mostramos todos los suscriptores iterándolos

print("\nSuscriptores de la lista:")
for suscriptor in suscriptores: #Iteramos los componentes de la lista con for
    print(f"- {suscriptor}")