#Compararemos cual de los numeros introducidos es mayor

print("*** Comparador de numeros ***")

#Solicitamos numero a y numero b

numero_a = int(input("Numero a: "))
numero_b = int(input("Numero b: "))

#Comparamos ambos valores y mandamos imprimir el mayor de ellos

comparador = f"Es mayor el a: {numero_a}" if numero_a >= numero_b else f"Es mayor el b: {numero_b}"

print(comparador)