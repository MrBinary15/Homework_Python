#* ========================= Proyecto 1: Calculadora básica con Python ====================================
# * Nombre: Arturo Parra
#? Fecha: 29/08/2024
# Bootcamp Ciencia de Datos + Inteligencia Artificial con Python
# Empresa: Codings Academy
#? Propuesta: Crear un sistema que permita realizar las cuatro operaciones
#? matemáticas básicas (Suma, Resta, Multiplicación y División).
#? Mediante un bucle while creará un menú de opciones que permita al usuario
#? seleccionar la operación deseada ej. (Ingrese la palabra ‘suma’ para sumar, la
#? palabra ‘resta’ para restar, etc.)
#? Los datos se deben capturar por teclado con la función de entrada input(), tanto las
#? opciones de menú como los números a operar.
#? Deberá utilizar estructuras de control como if y else en caso de la operación
#? seleccionada sea división y se intenté dividir algún número por cero, recordar que
#? esto no es posible por lo tanto debe mostrar un mensaje de error indicando que no
#? se puede dividir un número por cero.
#? Para salir del programa, el usuario puede ingresar "salir".

#* Especificaciones:
#* El proyecto estará dividido en dos criterios (fases):
#* En el primer criterio, deberás analizar el código del archivo calculadora.py y
#* deberás dar tu interpretación de cada línea de código.
#*  Comentarios: Asegúrate de incluir comentarios descriptivos en cada línea de
#* código para explicar tú interpretación.
#* En el segundo criterio, deberás implementar mejoras en el código del archivo
#* calculadora.py 
#* Las mejoras pueden ser algunas de las siguientes observaciones descritas a
#* continuación o las que tu consideres necesarias.
#*  En el menú de opciones en lugar de escribir ingrese “sumar” para
#* sumar o “restar” que se ingrese 1 para sumar, 2 para restar, 3 para multiplicar y 4
#* para dividir.
#* Puede hacer alguna mejora que ud considere necesaria, debe comentar
#* cada línea de código con su explicación.


#* ========================= Inicio del código ====================================
print("Calculadora Básica con Python", end="\n\n") #
print("Bienvenidos a la calculadora basica de Arturo Parra", end="\n")
print("primera version del codigo", end="\n")
def suma(x, y):
    return x + y  #? Retorna la suma de x , y
def resta(x, y):
    return x - y  #? Retorna la resta de x , y
def multiplicacion(x, y):
    return x * y  #? Retorna la multiplicación de x , y
def division(x, y):
    if y == 0:  #! Verifica si y es igual a 0 para evitar división por cero
        return "Error: No se puede dividir por cero."  #? Retorna un mensaje de error si y es 0
    return x / y  #? Retorna la división de x , y
while True:  #? Bucle para mostrar el menú al usuario
    print("\nSeleccione la operación:")  #? Muestra las opciones de operaciones
    print("1. Sumar")  #? Opción para sumar
    print("2. Restar")  #? Opción para restar
    print("3. Multiplicar")  #? Opción para multiplicar
    print("4. Dividir")  #? Opción para dividir
    print("5. Salir")  #? Opción para salir del programa
    opcion = input("Ingrese su opción (1 al 5): ")  #? Captura la opción del usuario

    if opcion == '5':  #? Verifica si el usuario desea salir
        print("Saliendo de la calculadora. ¡Hasta luego!")  #? Mensaje de despedida
        break  #? Sale del bucle y termina el programa
    if opcion not in {'1', '2', '3', '4'}:
        print("Opción no válida. Intente de nuevo.")
        continue  #? Regresa al menú
    try:
        x = float(input("Ingrese el primer número: "))
        y = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Entrada inválida. Debe ingresar números (ej. 10, 3.5).")
        continue
    
    #? Ejecutamos según la opción
    if opcion == '1':
        resultado = suma(x, y)
        print("El resultado de la suma es:", resultado)
    elif opcion == '2':
        resultado = resta(x, y)
        print("El resultado de la resta es:", resultado)
    elif opcion == '3':
        resultado = multiplicacion(x, y)
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == '4':
        resultado = division(x, y)
        print("El resultado de la división es:", resultado)  
#!=================fin del codigo=========================
#*=================siguiente codigo========================
lambda_calculadora = lambda x, y, op: {
    "1": x + y,
    "2": x - y,
    "3": x * y,
    "4": x / y if y != 0 else "Error: No se puede dividir para cero"
}.get(op, "Operación no válida")

def valores():
    numero = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))
    return numero, numero2

print("Bienvenidos a la calculadora encadenada")
print("Segunda version del codigo", end="\n")

while True:
    print("\nBienvenido al menu princial:")
    print("Seleccione la operación para continuar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    eleccion = input("Ingrese su opción (1 al 5): ")
    
    if eleccion == "5":
        print("Gracias por usar nuestro servicio", "Cerrando calculadora", sep="\n", end="....\n")
        break
    elif eleccion in ["1", "2", "3", "4"]:
        numero, numero2 = valores()
        resultado = lambda_calculadora(numero, numero2, eleccion)
        
        # Mostrar el resultado con el tipo de operación
        operaciones = {
            "1": "suma",
            "2": "resta", 
            "3": "multiplicación",
            "4": "división"
        }
        
        print(f"El resultado de la {operaciones[eleccion]} es: {resultado}")
        while True:
            print("desea seguir operando con el valor resultado")
            decision = input("digite si o no para continuar: ")
            if decision == "si":
                for key, value in operaciones.items():
                    print(f"{key}. {value}")
                op_siguiente = input("Seleccione la operación para continuar (1-4): ")
                if op_siguiente in ["1", "2", "3", "4"]:
                    siguiente_numero= float(input("ingrese el siguiente numero a operar: "))
                    resultado = lambda_calculadora(resultado, siguiente_numero, op_siguiente)
                    print(f"El nuevo resultado de la {operaciones[op_siguiente]} es: {resultado}")
                else:
                    print("Opción no válida. Regresando al menú.")
                    continue
                
            else:
                print("lo llevaremos al menu si desea salir o segui eligiendo operaciones con otros valores")
                break
        
    else:
        print("Opción no válida. Por favor, ingrese una opción del 1 al 5.")
    
                                