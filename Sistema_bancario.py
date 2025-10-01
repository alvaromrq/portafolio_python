#Sistema bancario, solicitud de cierre de sesión

print("*** Bienvenido a su sistema bancario ***")

solicitud = input("Detectado intento de cierre ¿Desea salir del sistema? (Si/No): ").strip().lower() #Preguntamos si deseamos seguir dentro

confirmacion = solicitud == "si" #Comparamos con si, para obtener un valor booleano


if not confirmacion: #Negamos con not, para que si decimos que si y coincide, haga lo opuesto, es decir salga del sistema
    print ("Continuamos dentro del sistema...")

else: #Si no es si, continuamos dentro
    print ("Saliendo del sistema...")