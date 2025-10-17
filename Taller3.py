#! =========================Taller n° 3 ====================================
# * Nombre: Arturo Parra
#? Fecha: 25/07/2025
# Bootcamp Ciencia de Datos + Inteligencia Artificial con Python
# Empresa: Codins Academy

    
"""Escribir un programa que permita  al usuario ingresar 5 números enteros,
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
La variable debe empezar vacia: elementos = []
Utilice (Input, print, int, str, sort, y la sintaxis para añadir elementos a la lista,
se permite ser creativo).

"""
#*===================== Primer Ejercicio ======================
#? Inicializamos una lista vacía para almacenar los números
elementos = []

print("Bienvenidos estimado usuario")
print("Por favor, ingrese 5 números enteros")

#? Creamos una lista con los textos ordinales para mostrar mensajes más descriptivos
lista = ["primero", "segundo", "tercero", "cuarto", "quinto"]

#! Bucle para solicitar los 5 números al usuario
for i in range(5):
    #? Solicitamos cada número convirtiendo directamente el input a entero
    num = int(input(f"Ingrese el {lista[i]} número: "))
    
    #? Añadimos el número a la lista
    elementos.append(num)
    
    #? Ordenamos la lista después de cada inserción
    elementos.sort()

#? Mostramos la lista ya ordenada
print("\nLista ordenada de menor a mayor:", elementos)
    
"""Escribir un programa que solicite el nombre del alumno y almacene las notas 
de historia, fisica, quimica y matemáticas en un diccionario.
luego  muestre un mensaje diga 
nombre del alumno y promedio general
"""
#*===================== Segundo Ejercicio \n ======================
#? Solicitamos el nombre del alumno
nombre = input("Ingrese el nombre del alumno: ")

#? Solicitamos las notas de cada materia
notas = {
    'Historia': float(input("Ingrese la nota de Historia: ")),
    'Física': float(input("Ingrese la nota de Física: ")),
    'Química': float(input("Ingrese la nota de Química: ")),
    'Matemáticas': float(input("Ingrese la nota de Matemáticas: "))
}

#? Calculamos el promedio general
promedio = sum(notas.values()) / len(notas)

#? Mostramos el resultado
print(f"\nEl alumno {nombre} tiene un promedio general de: {promedio:.2f}")