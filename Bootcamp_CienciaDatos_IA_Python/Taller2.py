#! =========================Taller n° 2 ====================================
# * Nombre: Arturo Parra
#? Fecha: 20/07/2025
# Bootcamp Ciencia de Datos + Inteligencia Artificial con Python
# Empresa: Codins Academy

#?==================glosario======================
#if = si caso es verdad, elif=sino siguiente caso, else = caso contrario o ninguna condicion
# for i in range (I, F, #saltos) para cada elemento i en un rango de (inicio del rando, final, saltos) hacer:
# el bucle for se itera,cuenta los elementos.
#while condicion : = mientras la condicion cumpla hacer:, si la condicion del bucle cumple, se repite.
#upper poner texto string en mayuscula
#break = terminar bucle
#en las condicionales, secuencias y bucles siempre ira dos puntos: final de la condicion, significa hacer:
#ejemplo: 
# if condicion : <-------->      si la condicion cumple, hacer:
# Métodos de strings:
# lower() - convierte texto a minúsculas
# upper() - convierte texto a mayúsculas
# strip() - elimina espacios en blanco al inicio/final
# split() - divide un string en una lista
# join() - une elementos de una lista en un string
# Métodos de listas:
# append() - añade un elemento al final
# remove() - elimina un elemento específico
# pop() - elimina y retorna un elemento por índice
# sort() - ordena la lista (modifica la original)
# sorted() - devuelve una nueva lista ordenada
# Métodos de diccionarios:
# keys() - devuelve todas las claves
# values() - devuelve todos los valores
# items() - devuelve pares clave-valor
# get() - obtiene valor de una clave
# Métodos de conjuntos:
# add() - añade un elemento
# update() - añade múltiples elementos
# discard()/remove() - elimina un elemento
# union() o | - operación de unión
# intersection() o & - operación de intersección
# Funciones útiles:
# len() - devuelve longitud/cantidad de elementos
# type() - muestra el tipo de dato
# range() - genera secuencia numérica
# input() - captura entrada del usuario
# print() - imprime en consola
# int()/float()/str() - conversión de tipos
# Estructuras de datos:
# [] - lista (ordenada, mutable, permite duplicados)
# () - tupla (ordenada, inmutable, permite duplicados)
# {} - diccionario (pares clave-valor) o conjunto (valores únicos)
# set() - constructor de conjuntos

#*==================ejercicios:=====================

"""EJERCICIO1
Elabora el ejercicios fizzbuzz
solicitar al usuario un numero para generar la secuencia
Si el numero es multiplo de 3, imprimir fizz
Si el numero es multiplo de 5, imprimir buzz
Si el numero es multiplo de 3 y 5, imprimir fizzbuzz
"""
print("--- Primer ejercicio --- \n")
#? pedimos al usuario que ingrese un numero
num= int(input("ingrese un numero: "))
#? para la secuencia ascendente que empezara en el rango del 1 hasta el numero ingresado por el usuario
for secuencia in range (1, num + 1): #! se pone + 1 ya que python el numero final discrimina
    #?si cumple la condicion que sea multiplo de 3 y multiplo de 5 al mismo tiempo imprimir Fizzbuzz
    #si los numero cumplen con la condicion se reemplaran con el mensaje impreso
    if  secuencia %3 == 0 and secuencia % 5 == 0: #! modulo % igual a cero, para los multiplos
        print("fizzbuzz") 
    elif secuencia % 5 == 0: #! multiplo de 5
        print("buzz")
    elif secuencia % 3 == 0: #!multiplo de 3
         print ("fizz")
    else : #caso contrario si no es multiplo de 3 o 5 imprimir el numero que toca de la secuencia
        print(secuencia)
        
    
"""EJERCICIO2
Generar un menu que el usuario pueda elegir una opcion
1. Saludar
2. Despedir
3. Salir
"""

print("--- Segundo ejercicio --- \n")

while True: #! el bucle siempre se repetira si cumple la condicion, se rompe si no cumple o ponemos break.
    print("Menu del sistema:")
    print("opcion 1 Saludar")
    print("opcion 2 Despedir ")
    print("opcion 3 salir")
    print()
    opcion = int(input("ingrese la opcion que desea: "))
    print()
    #*mientras el numero ingresado sea verdad hacer: 
    if opcion == 1: #si el numero es 1 saluda
      print("Saludos, ingresando al menu")
      print()
    elif opcion == 2: #si el numero es 2 regresa
        print("Adios, regresando al menu")
        print()
    elif opcion == 3: #si el numero es 3 cierra el bucle
        print("cerrando el menu")
        break #!rompemos el bucle
    else:
        print("opcion no encontrada intente de nuevo")
        print()

"""
EJERCICIO3 
Genera un programa el cual solicite al usuario 
ingresar su nombre su edad y sueldo
analice si es mayor de edad y el sueldo en mayor a 500 muestre un mensje con sus impuestos (0 %)
si es mayor de edad y el sueldo es menor  a 500 un mensaje que diga no paga impuestos
si es menor de edad igualmente no paga impuestos
"""
#en este ejercicio lo pondre al 5% de impuesto ya que es ilogico pensar no pagar impuesto o pagar 0 impuesto.
print("--- tercer ejercicio --- \n")

print("Bienvenidos al servicio de rentas internas (SRI) \n")
print("Para continuar, ingrese los siguientes datos:", end="\n")
edad = int(input("ingrese su edad: ")) #pedimos al usuario que ingrese la edad
if edad >= 18: #? si es mayor de edad hacer:
    sueldo = int(input("ingrese su sueldo: ")) #pedimos al usuario que ingrese su sueldo
    if sueldo >= 500: #? si sueldo es mayor o igual a 500
        print("Usted paga impuesto del 5%")
        print(f"El valor de su impuesto a pagar es: ${int(sueldo * 0.05)}")
    else: #caso contrario: su sueldo es menor no paga.
        print("Su sueldo es menor, no paga impuesto.")
else:  #! caso contrario: al ser menor se imprime el mensaje, no se pide sueldo, no labora.
    print("usted es menor de edad, no paga impuesto.")
print()

"""EJERCICIO4
Solicitar al usuario ingresarar 3 notas y el nombre del alumno
calcular el promedio y mostrar un mensaje si el alumno aprueba o no
"""

print("--- cuarto ejercicio --- \n")
#pedimos al usuario que ingrese su nombre.
nombre = (input("ingrese su nombre: ").upper()) #! upper metodo para poner todo en mayuscula
#pedimos al usuario sus notas de sus 3 calificacione
print("se calificara del 0 al 10")
calificacion1 = float(input("ingrese su primera nota: "))
calificacion2 = float(input("ingrese su segunda nota: "))
calificacion3 = float(input("ingrese su tercera nota: "))
# lo transformo en una vector
calificaciones = (calificacion1, calificacion2, calificacion3)
#sacamos el promedio de las notas de los 3 valores ingresado dividido para el numero de sus elemento
promedio = round(sum(calificaciones) / len(calificaciones),2) #! se redondea a 2 decimales
if 10>= promedio >= 8:
    print(f" Estimad@ {nombre}, ha aprobado con excelentes resultado con: {promedio}")
elif 8 > promedio >= 6:
    print(f"Estimad@ {nombre}, ha aprobado con: {promedio}")
elif 6> promedio >0 :
    print(f"Estimad@ {nombre}, lo sentimos no ha aprobado")
else:
    print("error los valores no estan definido dentro de la regla, solo valores del 0 al 10")
#hacemos un salto de linea    
print()

"""EJERCICIO5
Escriba 2 conjuntos por favor y realice las operaciones de conjuntos 
"""
print("--- quinto ejercicio --- \n")

#pondremos 2 conjuntos 
conjunto1 = {"caballos", "gallinas", "vacas", "cerdos", "patos"} 
conjunto2 = {"pavos", "gallinas", "cordonices", "patos", "palomas"} 
conjunto3 = {0, 1, 2, 3, 4, 5}
conjunto4 = {9, 8, 7, 6, 5, 4}
print(f" el conjunto 1 es: \n{conjunto1}")
print(f" el conjunto 2 es: \n{conjunto2}")
print(f" el conjunto 3 es: \n{conjunto3}")
print(f" el conjunto 4 es: \n{conjunto4}")
print()

#? operacion de conjuntos

#* union 
#crea un conjunto nuevo con todo los elementos del conjunto1 y conjunto2
union1 = conjunto1.union(conjunto2, conjunto3, conjunto4)  #manera 1
union2 = (conjunto3 | conjunto4 | conjunto2 | conjunto1)  #manera 2
print("\n Unión")
print(union1) 
print(union2)

#* intersección
#crea un conjunto nuevo con los elementos que tienen en comun el conjunto 1 y 2
interseccion1 = conjunto1.intersection(conjunto2) #manera 1
interseccion2 = (conjunto3 & conjunto4) #manera 2
print("\n Interseccion:")
print(interseccion1)
print(interseccion2)

#* diferencia
#crea un conjunto nuevo  con solo los elementos del conjunto que se pone primero
#solo toma elementos del conjunto que se pone primero ignorando al otro conjunto y su elementos comunes.
diferencia1 = conjunto1.difference(conjunto2) #manera 1
diferencia2 = (conjunto3 - conjunto4) #manera 2
print("\n Diferencia")
print(diferencia1)
print(diferencia2)

#? bonus
#* diferencia simetrica
#crea un conjunto nuevo uniendo los conjuntos pero ignorando los valores que tienen en comun.
simetrica1 = conjunto1.symmetric_difference(conjunto2) #manera 1
simetrica2 = (conjunto3 ^ conjunto4) #manera 2
print("\n Diferencia simetrica:")
print(simetrica1)
print(simetrica2)

"""
EJERCICIO 6:
Genera una lista de compras con 3 frutas, muéstrala en consola,
luego añade una fruta más al final (ingresada por teclado).
Si la fruta ya existe, muestra un mensaje de error.
"""

# Mostramos un encabezado para identificar el ejercicio
print("--- sexto ejercicio --- \n")

# Inicializamos la lista con 3 frutas predefinidas
inventario_Frutas = ["bananas", "manzanas", "sandias"]

# Mostramos el inventario actual al usuario
print("Inventario actual:", inventario_Frutas)

# Bucle infinito para asegurar que se ingrese una fruta válida
while True:
    # Solicitamos al usuario que ingrese una nueva fruta
    # Convertimos a minúsculas para evitar problemas de mayúsculas/minúsculas
    agregar_Frutas = input("Ingrese el nuevo producto: ").lower()
    
    # Verificamos si la fruta ya existe en el inventario
    if agregar_Frutas in inventario_Frutas:
        # Si existe, mostramos un mensaje de error
        print(f" -({agregar_Frutas})- ya está registrado. Intente con otra fruta.")
    else:
        # Si no existe, la agregamos al final de la lista
        inventario_Frutas.append(agregar_Frutas)
        # Mostramos confirmación y el inventario actualizado
        print(f"Se agregó el producto al inventario. \n {inventario_Frutas}")
        # Salimos del bucle while
        break


"""
EJERCICIO7
en un grupo de numero [1,2,2,3,4,5,1,8,9] 
ordene los numeros
muestre los numero sin ningun valor repetido
indica cual es el maximo y minimo
"""
print("--- septimo ejercicio --- \n")
num=[1,2,2,3,4,5,1,8,9]
ordenar= sorted(num)
print(f"su lista sin ordenar es: \n {num}")
print(f"su lista ordenada es: \n {ordenar}")
#?eliminación de numeros repetidos
# para eliminar los numeros repetidos tranformamos la lista a conjunto
# con la estructura de datos set() <--> (conjuntos)
conjuntos = set(ordenar) #!transformamos list a conjuntos / se eliminan los elementos repetido
lista = list(conjuntos) #! transformamos de nuevo a list
print(f"Eliminamos los elementos repetidos: \n {lista}")
print(f"El maximo es: {max(lista)}")#! enseñamos el maximo numero con la funcion max()
print(f"El minimo es: {min(lista)}")#! enseñamos el minimo numero con la funcion min()

"""EJERCICIO8
Genere un diccionario con los siguientes datos 
nombre, apellido, edad, puesto
luego muestre los datos en consola
"""
print("--- octavo ejercicio --- \n")
# Creamos un diccionario con información de una persona
# Los diccionarios usan pares clave-valor entre llaves {}
diccionario = {
    "nombre": "Arturo",      #* Clave "nombre" con valor "Arturo"
    "apellido": "Parra",    #* Clave "apellido" con valor "Parra"
    "edad": 28,             #* Clave "edad" con valor numérico 28
    "puesto": "Desarrollador"  #* Clave "puesto" con valor "Desarrollador"
}

print("Los datos del usuario son: ")

#! Iteramos a través del diccionario usando .items()
#! Esto nos da acceso a cada par clave-valor
for clave, valor in diccionario.items():
    # Por cada iteración, mostramos la clave y su valor correspondiente
    # Usamos f-strings para formatear la salida
    print(f"{clave} : {valor}")
    
    
"""
EJERCICIO9
En base a la estructura anterior 
genere un lista de 2 diccionario solicitando el ingreso de los datos
"""

print("--- noveno ejercicio --- \n")
# Creamos una lista vacía para almacenar los diccionarios de cada persona
lista_personas = []

# !Bucle para pedir datos de 2 personas (range(2) -> 0 y 1)
for i in range(2):
    #? Mostramos un mensaje para indicar qué persona se está ingresando
    print(f"\nIngrese los datos de la persona {i + 1}:")
    
    #? Solicitamos los datos al usuario
    nombre = input("Nombre: ")          #* Guarda el nombre como string
    apellido = input("Apellido: ")      #* Guarda el apellido como string
    edad = int(input("Edad: "))         #* Guarda la edad a entero
    puesto = input("Puesto: ")          #* Guarda el puesto como string
    
    #? Creamos un diccionario con los datos ingresados
    persona = {
        "nombre": nombre,       #* Clave "nombre" con valor ingresado
        "apellido": apellido,   #* Clave "apellido" con valor ingresado
        "edad": edad,           #* Clave "edad" con valor convertido a int
        "puesto": puesto        #* Clave "puesto" con valor ingresado
    }
    
    #? Agregamos el diccionario de la persona a la lista
    lista_personas.append(persona)

#? Mostramos todos los datos ingresados
print("\nLista de personas ingresadas:")

#? Recorremos cada persona (diccionario) en la lista
for persona in lista_personas:
    print("\nDatos:")
    #? Recorremos cada clave-valor en el diccionario de la persona
    for clave, valor in persona.items():
        #? Mostramos la clave y su valor 
        print(f"{clave}: {valor}")
