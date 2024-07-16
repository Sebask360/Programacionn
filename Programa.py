#Desarrollar un programa en Python que solicite al usuario su nombre, edad y un número, y luego realice operaciones básicas con estos datos.
#Requisitos:
#1. El programa debe solicitar al usuario que ingrese su nombre.
nombre = input("Ingrese su nombre: ")
apellido = input("ingrese su apellido: ")

#2. El programa debe solicitar al usuario que ingrese su edad.
edad = input("ingrese su edad: ")
#3. El programa debe mostrar un mensaje de bienvenida utilizando el nombre y la edad proporcionados por el usuario.

nombrecompleto = ((nombre)+ " " +str(apellido))
print("Bienvenido ", (nombrecompleto) + "! Tienes " + (edad), " años \n")


#4. El programa debe solicitar al usuario que ingrese un número.
num_uno = input("Ingrese un numero: ")
print(type(num_uno))

#5. El programa debe convertir el número ingresado a un tipo de dato entero.

num_int = int(num_uno)
print(type(num_int))

#6. El programa debe mostrar el doble del número ingresado.
doble_numero = num_int * 2
print(doble_numero)
print(type(doble_numero))
    
print(f"El doble de {num_int} es {doble_numero}")