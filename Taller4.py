#! =========================Taller n° 4 ====================================
# * Nombre: Arturo Parra
#? Fecha: 15/09/2025
# Bootcamp Ciencia de Datos + Inteligencia Artificial con Python
# Empresa: Codins Academy

# GLOSARIO DE COMENTARIOS:
# #* Comentario importante o titulo
# #? Comentario de duda o descripción
# #! Comentario de advertencia o precaución

"""
Tienes un arreglo (llamado myArray) con 5 elementos (enteros en el rango de 1 a 100).
 Escribe un programa en Python que imprima el número más alto del arreglo (Si se repite, 
 solo imprimir una vez). El programa solo debe imprimir el número, sin ningún texto.
"""
#*===================== Primer Ejercicio ======================
print("Primer ejercicio: Número más alto en un arreglo", end="\n\n")
def ejercicio1():
    myArray = [23, 89, 67, 89, 12] # Arreglo
    max_num = max(myArray) # ?Encontrar el número más alto
    return max_num #? Retornar el número más alto
print(ejercicio1()) #! Imprimir el resultado del primer ejercicio
print() #* Salto de línea para separar los ejercicios


#*===================== Segundo Ejercicio ======================
"""
Escribir un programa en Python que recorra un arreglo y genere un histograma en
base a los números de este. El arreglo se llama myArray y contiene 10 elementos que
corresponden a números enteros del 1 al 5. Un histograma representa que tanto un elemento
aparece en un conjunto de datos (Debe mostrar la frecuencia para todos los números del 1 al 5,
incluso si no están presentes en el arreglo). 
Por ejemplo, para el arreglo: myArray:=(1,2,1,3,3,1,2,1,5,1) el histograma se vería así:
1: *****
2: **
3: **
4:
5: *
"""
print("Segundo ejercicio: Histograma de Frecuencia", end="\n\n") 
def ejercicio2():
    myArray = [1, 2, 3, 3, 3, 4, 5, 5, 5, 5]
    histograma = {elemento: 0 for elemento in range(1, 6)} #? Inicializar el histograma con claves del 1 al 5
    #? Contar la frecuencia de cada número en el arreglo
    for num in myArray:
        histograma[num] +=1 #? Contar la frecuencia de cada número en el arreglo
    for key, value in histograma.items():
        print(f"{key}: {'*' * value }") #? Imprimir el histograma
    return "" #! Retornar una cadena vacía para evitar retorno None o imprimir el histograma dos veces
print(ejercicio2()) #! Llamar a la función del segundo ejercicio
print() #* Salto de línea para separar los ejercicios

#*===================== Tercer Ejercicio ======================
"""
Gestor de Tareas Pendientes
Crea una función que permita:
Agregar tareas a una lista.
Marcar tareas como completadas (eliminándolas de la lista).
Mostrar todas las tareas pendientes.
Utilizar un diccionario para guardar el estado de las tareas (ej: {"descripción": "comprar pan", "completada": False}).
"""
print("Tercer ejercicio: Gestor de Tareas Pendientes", end="\n\n") 
def gestor_tareas():
    tareas = []

    def marcar_completada():
        #presentamos las tareas pendientes
        pendientes = [tarea for tarea in tareas if not tarea["completada"]]
        if not pendientes:
            print("No hay tareas pendientes.")
        else:
            for indice, tarea in enumerate(pendientes, start=1):
                print(f"{indice}. {tarea['descripción']}")
            tarea_indice = int(input("Seleccione el número de la tarea que ha completado: ")) - 1
            if 0 <= tarea_indice < len(pendientes):
                tarea_completada = pendientes[tarea_indice]
                tarea_completada["completada"] = True
                print("Tarea marcada como completada.")
            else:
                print("No hay tarea con ese número.")

    while True:
        print("1. Agregar tarea")
        print("2. Marcar tarea realizada")
        print("3. Mostrar tareas pendientes")
        print("4. Mostrar las tareas completadas")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == '1':
            descripcion = input("Ingrese la descripción de la tarea: ")
            if descripcion not in [tarea["descripción"] for tarea in tareas]:
                tareas.append({"descripción": descripcion, "completada": False})
                print("Tarea agregada.")
                #si desea ingresar otra tarea
                otra = input("¿Desea agregar otra tarea? (si/no): ").lower()
                while otra == 'si':
                    descripcion = input("Ingrese la descripción de la tarea: ")
                    if descripcion not in [tarea["descripción"] for tarea in tareas]:
                        tareas.append({"descripción": descripcion, "completada": False})
                        print("Tarea agregada.")
                        otra = input("¿Desea agregar otra tarea? (si/no): ").lower()
                    else:
                        continue
            else:
                print("La tarea ya existe.")
            print("volviendo al menú principal...")
        elif opcion == '2': #marcar tarea como completada
            marcar_completada()
            print("volviendo al menú principal...")
        elif opcion == '3': #mostrar tareas pendientes
            pendientes = [tarea for tarea in tareas if not tarea["completada"]]
            if not pendientes:
                print("No hay tareas pendientes.")
            else:
                print("Tareas pendientes:")
                for tarea in pendientes:
                    print(f"- {tarea['descripción']}")
                
                #desea marcar alguna como completada?
                marcar = input("¿Desea marcar alguna tarea como completada? (si/no): ").lower()
                if marcar == 'si':
                    #ir a la opción 2
                    marcar_completada()
                elif marcar == 'no':
                    continue
                else:
                    print("Opción no válida.")
            print("volviendo al menú principal...")
        elif opcion == '4': #mostrar tareas completadas
            completadas = [tarea for tarea in tareas if tarea["completada"]]
            if not completadas:
                print("No hay tareas completadas.")
            else:
                print("Tareas completadas:")
                for tarea in completadas:
                    print(f"- {tarea['descripción']}")
            print("volviendo al menú principal...")
        elif opcion == '5': #salir
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
gestor_tareas() #! Llamar a la función tareas
print()
#*==================== cuarto ejercicio =======================
"""
 Filtro de Números
Crea una función que reciba una lista de números y devuelva:
Una lista con los números pares.
Un diccionario con el conteo de números mayores que 10.

ej. numeros = [5, 12, 3, 8, 15, 12, 6]
"""
print("cuarto ejercicio: Filtro de Números", end="\n\n") 
def filtro_numeros(numeros):
    #? Lista de números pares
    pares = [num for num in numeros if num % 2 == 0] # comprensión de listas para obtener números pares
    #? Diccionario con el conteo de números mayores que 10
    mayores_que_10 = sum(1 for num in numeros if num > 10)
    conteo_mayores = {"mayores_que_10": mayores_que_10}
    return pares, conteo_mayores
print(filtro_numeros([5, 12, 3, 8, 15, 12, 6])) #! Llamar a la función filtro_numeros
print() #* Salto de línea para separar los ejercicios

#*==================== quinto ejercicio =======================
"""
Búsqueda en Diccionario de Contactos
Crea un diccionario de contactos (nombre: teléfono) y una función que:
Busque un contacto por nombre (usando condicionales).
Permita añadir nuevos contactos (validando que el teléfono sea numérico).
"""
print("quinto ejercicio: Búsqueda en Diccionario de Contactos", end="\n\n")
def gestor_contactos():
    contactos = {}

    def buscar_contacto():
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        if nombre in contactos:
            print(f"El teléfono de {nombre} es {contactos[nombre]}.")
        else:
            print(f"No se encontró el contacto {nombre}.")

    def agregar_contacto():
        nombre = input("Ingrese el nombre del nuevo contacto: ")
        telefono = input("Ingrese el teléfono del nuevo contacto: ")
        if telefono.isdigit(): #? Validar que el teléfono sea numérico
            contactos[nombre] = telefono
            print(f"Contacto {nombre} agregado con éxito.")
        else:
            print("El teléfono debe ser numérico. Contacto no agregado.")

    while True:
        print("1. Buscar contacto")
        print("2. Agregar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")
        if opcion == '1':
            buscar_contacto()
            print("volviendo al menú principal...")
        elif opcion == '2':
            agregar_contacto()
            print("volviendo al menú principal...")
        elif opcion == '3':
            if not contactos:
                print("No hay contactos en la agenda.")
            else:
                print("Contactos en la agenda:")
                for nombre, telefono in contactos.items():
                    print(f"- {nombre}: {telefono}")
            print("volviendo al menú principal...")
        elif opcion == '4':
            print("Saliendo del gestor de contactos.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
gestor_contactos() #! Llamar a la función gestor_contactos
#*==================== Fin Taller 4 =======================