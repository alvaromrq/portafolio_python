#Se solicitara al usuario un valor y comprobaremos si el valor introducido, esta dentro de rango del 0 al 5

print("*** Comprobación de valor ***")

#Declaramos constantes de minimo y maximo

MINIMO = 0
MAXIMO = 5

valor = int(input("\nIntroduzca un valor: ")) #Solicitamos que se introduzca un valor

comparativa = MINIMO <= valor <= MAXIMO #Comparamos que el valor introducido este entre el minimo y maximo marcado por las constantes

print (f"¿El valor se encuentra dentro del rango? {comparativa}")