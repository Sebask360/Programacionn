# 1. El programa debe solicitar al usuario que ingrese su nombre.
nombre = input("Ingresa tu nombre: ")

# 2. El programa debe solicitar al usuario que ingrese su edad.
edad_str = input("Ingresa tu edad: ")

# 3. El programa debe mostrar un mensaje de bienvenida utilizando el nombre y la edad proporcionados por el usuario.

try:
    edad = int(edad_str)
    print(f"Bienvenido, {nombre}! Tienes {edad} años.")

    # 4. El programa debe solicitar al usuario que ingrese un número.
    numero_str = input("Ingresa un número: ")

    # 5. El programa debe convertir el número ingresado a un tipo de dato entero.
    numero_entero = int(numero_str)

    # 6. El programa debe mostrar el doble del número ingresado.
    doble_numero = numero_entero * 2
    #print(doble_numero)
    print(f"El doble de {numero_entero} es {doble_numero}")
    
except ValueError:
    print("Error: Ingresa datos numéricos válidos para la edad y el número.")