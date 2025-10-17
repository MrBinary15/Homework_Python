#! =========================Taller n° 5 ====================================
# * Nombre: Arturo Parra
#? Fecha: 15/09/2025
# Bootcamp Ciencia de Datos + Inteligencia Artificial con Python
# Empresa: Codins Academy

# GLOSARIO DE COMENTARIOS:
# #* Comentario importante o titulo
# #? Comentario de duda o descripción
# #! Comentario de advertencia o precaución

#*===================== Primer Ejercicio ======================

"""Ejercicio1
con el Archivo Gastos.txt realiza un porograma que lea el archivo
muestre por pantalla el total de los gastos.
escriba en el archivo Gastos.txt el total de los gastos.
"""

print("\nPrimer ejercicio: Manipulación de documentos", end="\n\n")

#!forma 1 larga
with open("Gastos.txt", "r+") as gastos: #? Abrimos el archivo en modo lectura y escritura
    doc_gastos1 = gastos.readlines() #? Leemos todas las líneas del archivo y la transformamos en lista
    print(doc_gastos1) #? Mostramos las líneas leídas por pantalla
    gastos1 = doc_gastos1[0].strip() #? Eliminamos espacios en la primera línea
    gastos2 = doc_gastos1[1].strip() #? Eliminamos espacios en la segunda línea
    gastos3 = doc_gastos1[2].strip() #? Eliminamos espacios en la tercera línea
    suma = int(gastos1) + int(gastos2) + int(gastos3) #? Sumamos los gastos convertidos a entero
    gastos.write("\n" + str(suma))         #? Escribimos el total de los gastos en el archivo con salto de línea
#!forma 2 corta
with open("Gastos.txt", "r+") as gastos: #? Abrimos el archivo en modo lectura y escritura
    doc_gastos1 = [int(line.strip()) for line in gastos.readlines()]#? Leemos cada línea, eliminamos espacios y convertimos a entero
    print(doc_gastos1) #? Mostramos la lista de gastos por pantalla
    suma = sum(doc_gastos1) #? Calculamos la suma total de los gastos
    gastos.write("\n" + str(suma)) #? Escribimos el total de los gastos en el archivo con salto de línea

#*===================== Segundo Ejercicio ======================

"""Ejercicio2
Realice un bucle que solicite a 3 usuario el usuario ingresas 
, su nombre completo y su edad cedula, y guarde estos datos en un archivo llamado Datos.csv
Luego, lea el archivo y muestre por pantalla los datos ingresados.
Ej.
Crear el archivo 
Nombre, Edad, Cedula
Juan Perez, 30, 123456789
Maria Lopez, 25, 987654321  
"""

#* Segundo ejercicio: Crear bucle y archivo csv
print("Segundo ejercicio: Crear bucle y archivo csv", end="\n\n") 

#* Función para registrar un usuario solicitando nombre, edad y cédula
def registro_usuario():
    while True:
        try:
            name = input("Ingrese su Nombre: ")
            if not name.replace(" ", "").isalpha():
                raise ValueError("El nombre debe contener solo letras.")
            age = input("Ingrese su edad: ")
            if not age.isdigit():
                raise ValueError("La edad debe ser un número.")
            cedula = input("Ingrese su n° cedula: ")
            if not cedula.isdigit():
                raise ValueError("La cédula debe ser un número.")
            return {
                "nombre": name,
                "edad": age,
                "cedula": cedula
            }
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")
            
def subir_archivo():
    with open("usuario.csv", "w") as user: #? Abre el archivo CSV
        user.write("nombre,edad,cedula\n") #? Escribe los titulos
        for usuario in usuarios_registrados: #? Escribe los datos de cada usuario
            user.write(f"{usuario['nombre']},{usuario['edad']},{usuario['cedula']}\n")
    print("Registro subido con exito", end="....\n\n")

usuarios_registrados = []  #* Lista para almacenar los usuarios

#* Menu principal del sistema
while True:
    print("Bienvenidos al sistema querido usuario", end="\n")
    print("1. registrarse", "2. usuarios registrados", "3. guardar usuarios en un archivo csv", "4. salir", sep="\n", end="\n")
    try:
        opcion = int(input("Digite la opcion que desea: "))  #? Solicita la opción al usuario
    except ValueError:
        print("Por favor digite números enteros")  #? Valida que la opción sea un número
        continue

    if opcion == 4:
        print("Gracias por preferir nuestro sistema, Adios", end="...\n\n")  #? Mensaje de despedida
        break
    if opcion == 1:
        cantidad = input("¿Cuántos usuarios desea registrar? ")
        if not cantidad.isdigit() or int(cantidad) < 1:
            print("Por favor ingrese un número válido mayor a 0.")
        else:
            for _ in range(int(cantidad)):
                usuario = registro_usuario()           #? Llama a la función para registrar usuario
                usuarios_registrados.append(usuario)   #? Agrega el usuario a la lista
            print(f"Felicidades, se registraron {cantidad} usuario(s) exitosamente", sep="\n")
            print("regresando al menu", end="....\n\n")
        
    elif opcion == 2:
        print("lista de usuarios registrados:")
        for usuario in usuarios_registrados:   #? Muestra los usuarios registrados
            print(usuario)
        seleccion = input("Seleccione una opción:\n1. regresar al menu\n2. subir datos al archivo\n3. salir\n")
        if seleccion == "1":
            print("Regresando al menu", end="....\n\n")
            continue
        elif seleccion == "2":
            print("dirigiendo a la seccion subir archivo")
            subir_archivo()
        elif seleccion == "3":
            print("Gracias por preferir nuestro sistema, Adios", end="...\n\n") 
            break
      
    elif opcion == 3:
        subir_archivo()
#*===================== Tercer Ejercicio ======================
"""Ejercicio3
 lista de correos electrónicos, realice un programa que lea el archivo Correos.txt
muestre por pantalla los correos electrónicos que son válidos.
Un correo electrónico es válido si :

@hotmail.com
@gmail.com
@yahoo.com

Luego cree el archivo solo con los correos Validos
"""
print("Tercer ejercicio: Correos validos", end="\n\n")

def emails_valido():
    dominios_validos = ["hotmail.com","hotmail.es", "outlook.es", "outlook.com", "gmail.com", "yahoo.com", "yahoo,es"]
    correos_validos = []
    try:
        with open("Correos.txt", 'r') as emails:
            for email in emails:
                correo = email.strip()
                #?si algun dominio esta contenido en correo para cada dominio que estan en los dominios validos, hacer:
                if any(dominio in correo for dominio in dominios_validos):
                    correos_validos.append(correo)
                    print(correo)
    except Exception as e:
        print(e)
emails_valido()

#*==================== cuarto ejercicio =======================
"""Ejercicio4
Con el archivo Personal.csv, realice un programa que lea el archivo y muestre por pantalla
los datos de los empleados que tienen un salario mayor a 200.
Luego, guarde en un nuevo archivo llamado EmpleadosAltosSalarios.csv
muestre por pantalla Los datos de los empleados que tengan una edad menor a 25 años.
guarde en un nuevo archivo llamado EmpleadosJovenes.csv
los datos de los empleados que cumplen con esta condición.
El archivo Personal.csv tiene el siguiente formato:
Nombre, Edad, Cedula, rol, salario  
Agregue un usuario mas al archivo Personal.csv
Carlos Medina, 30, 1234567890, Developer, 1200
"""
print("cuarto ejercicio: Empleados", end="\n\n")
def procesar_empleados():  
    #* Lista inicial de empleados
    empleados = []  #? Lista vacía (no se usa, pero está declarada)
    list_empleados = []  #? Lista donde se guardarán los empleados como diccionarios

    def list_empleado():
        #* Leer archivo CSV y cargar datos
        try:
            with open("Personal.csv", 'r') as documento:  #? Abrimos el archivo en modo lectura
                personas = [linea.strip() for linea in documento]  #? Guardamos cada línea sin saltos de línea
                personas.pop(0)  #? Quitamos la cabecera
                for persona in personas:  #? Recorremos cada línea (empleado)
                    #* Separar datos por comas
                    nombre, edad, cedula, rol, salario = persona.split(",")
                    #* Agregar empleado como diccionario
                    list_empleados.append({
                        "nombre": nombre,         #? Guardamos el nombre
                        "edad": int(edad),        #? Convertimos la edad a número
                        "cedula": int(cedula),    #? Convertimos la cédula a número
                        "rol": rol,               #? Guardamos el rol
                        "salario": float(salario) #? Convertimos el salario a número decimal
                    })
        except Exception as e:
            #! Si ocurre un error al leer el archivo, lo mostramos
            print(e)

    list_empleado()  #* Llamamos a la función para llenar la lista de empleados

    #* FILTRO: empleados con salario mayor a 200
    print("Empleados con salario mayor a 200:")
    for trabajador in list_empleados:  #? Recorremos todos los empleados
        if trabajador["salario"] > 200:  #? Condición: salario > 200
            print(trabajador)  #? Mostramos el empleado en pantalla

    #* Guardar empleados con salario mayor a 200 en un nuevo archivo
    with open("EmpleadosAltosSalarios.csv", "w") as archivo:
        archivo.write("Nombre,Edad,Cedula,Rol,Salario\n")  #? Escribimos cabecera en CSV
        for trabajador in list_empleados:
            if trabajador["salario"] > 200:  #? Condición: salario > 200
                archivo.write(f'{trabajador["nombre"]},{trabajador["edad"]},{trabajador["cedula"]},{trabajador["rol"]},{trabajador["salario"]}\n')

    #* FILTRO: empleados con edad menor a 25
    print("\nEmpleados con edad menor a 25:")
    for trabajador in list_empleados:  #? Recorremos todos los empleados
        if trabajador["edad"] < 25:  #? Condición: edad < 25
            print(trabajador)  #? Mostramos empleado en pantalla

    #* Guardar empleados con edad menor a 25 en un nuevo archivo
    with open("EmpleadosJovenes.csv", "w") as archivo:
        archivo.write("Nombre,Edad,Cedula,Rol,Salario\n")  #? Escribimos cabecera en CSV
        for trabajador in list_empleados:
            if trabajador["edad"] < 25:  #? Condición: edad < 25
                archivo.write(f'{trabajador["nombre"]},{trabajador["edad"]},{trabajador["cedula"]},{trabajador["rol"]},{trabajador["salario"]}\n')


procesar_empleados()  #* Ejecutamos la función principal

#*==================== quinto ejercicio =======================
"""
Ejercicio5
Elaborar un menu.
donde se puede mostrar, agregar y eliminar items.
los items de la base de datos estan en Productos.txt
la estrucuta es la siguiente:
Nombre, Precio, Cantidad
Ejemplo:
Arroz, 1.50, 100
"""
print("quinto ejercicio: Productos", end="\n\n")



# Cargar productos desde el archivo antes del menú
def Menu_productos():
    items = []
    with open("Productos.csv", "r") as productos:
        for linea in productos:
            if linea.strip():
                items.append(linea.strip().split(','))

    while True:
        print("Bienvenidos al sistema")
        print("1. mostrar items", "2. agregar items", "3. eliminar items", "4. salir", sep="...\n", end="...\n")
        try:
            opcion=int(input("Digite del 1 al 4 la opcion que desea realizar: "))
        except Exception as e:
            print(e)
            continue
        if opcion == 4:
            print("Gracias por visitar nuestro sistema", "saliendo del sistema", sep='\n', end='...\n\n')
            break
        elif opcion == 1:
            print("la lista de productos es:")
            for item in items:
                print(','.join(item))
        elif opcion == 2:
            print("agregar productos:")
            nombre = input("digite el nombre del producto: ")
            precio = input("digite el precio del producto: ")
            cantidad = input("digite la cantidad del producto: ")
            items.append([nombre, precio, cantidad])
            print("Producto agregado exitosamente")
        elif opcion == 3:
            print("eliminar productos:")
            nombre = input("digite el nombre del producto a eliminar: ")
            encontrado = False
            try:
                for item in items:
                    if item[0].lower() == nombre.lower():
                        items.remove(item)
                        print(f"Producto '{nombre}' eliminado exitosamente")
                        encontrado = True
                        break
                if not encontrado:
                    print(f"Producto '{nombre}' no encontrado en la lista.")
            except (ValueError, IndexError) as e:
                print(f"Error al eliminar el producto: {e}")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
    return (Menu_productos)
Menu_productos()
#*==================== Fin Taller 4 =======================