# mensaje de bienvenida
print("**********************BIENVENIDO A NUESTRO CODIGO***********************")


# Definir una función para validar un número ingresado por el usuario
def validar_numero():
    while True:
        try:
            numero = int(input("\nIngrese un número: ")) # Solicitar al usuario que ingrese un número entero
            return numero # Devolver el número ingresado si es válido
        except ValueError:
            print("\nDebe ingresar un número entero. Intente nuevamente.") # Mostrar un mensaje de error si el número ingresado no es válido

# Definir una función para obtener un dato válido ingresado por el usuario
def obtener_dato_valido(mensaje):
    while True:
        dato = input(mensaje) # Solicitar al usuario que ingrese un dato
        if dato.isdigit():  # Verificar si el dato es un número entero
            return int(dato) # Devolver el número ingresado si es válido
        else:
            print("\nEl dato ingresado no es válido. Por favor, ingrese un número entero.") # Mostrar un mensaje de error si el dato ingresado no es válido

# Definir una función para contar la cantidad de números positivos, negativos y nulos ingresados por el usuario
def contar_numeros():
    cantidad_positivos = 0 
    cantidad_negativos = 0 
    cantidad_nulos = 0 
    n = obtener_dato_valido("\n¿Cuántos números desea ingresar? ") # Solicitar al usuario que ingrese la cantidad de números que desea ingresar y validar el dato ingresado

    for i in range(n): # Repetir el proceso de ingresar números la cantidad de veces indicada por el usuario
        numero = validar_numero() # Solicitar al usuario que ingrese un número y validar el dato ingresado
        if numero > 0:
            cantidad_positivos += 1 # Si el número ingresado es positivo, aumentar la cantidad de números positivos en 1
        elif numero < 0:
            cantidad_negativos += 1 # Si el número ingresado es negativo, aumentar la cantidad de números negativos en 1
        else:
            cantidad_nulos += 1 # Si el número ingresado es nulo, aumentar la cantidad de números nulos en 1
   
    print("\nEL RESULTADO ES EL SIGUIENTE")
    
    # Mostrar la cantidad de números positivos, negativos y nulos ingresados por el usuario
    print("\n esta es la cantidad de números positivos: ", cantidad_positivos)
    print("\n esta es la Cantidad de números negativos: ", cantidad_negativos)
    print("\n esta es la Cantidad de números nulos: ", cantidad_nulos)

# Llamar a la función contar_numeros() para iniciar el proceso de contar la cantidad de números positivos, negativos y nulos ingresados por el usuario
contar_numeros()

print("\nFIN DEL CODIGO GRACIAS POR TU TIEMPO\n")