print("hola mundo desde python")
#variables numericas
edad = 25 #entero
#variable de tipo flotante
altura = 1.75 #flotante
bandera = True #booleano
nombre = "bruno diaz" #string
print("\nprint tradicional")
print("-------------")
print ("MI NOMBRE ES:", nombre)
print("Mi edad es:", edad)
print("Mi altura es:", altura)
print("Mi bandera es:", bandera)


#entrada e datos
print("\nEntrada de datos")
print("-------------")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura: "))
bandera =input("estas vivo? (true/false): ")
#segunda forma de imprimir
print("\nprint moderno")
print("-------------")
print (f"mi nombre es: {nombre}")
print(f"mi edad es: {edad}")
print(f"mi altura es: {altura}")
print (f"estoy vivo: {bandera}")