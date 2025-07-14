
#! =========================Taller n° 1 ====================================
# * Nombre: Arturo Parra
#? Fecha: 13/07/2025
# Bootcamp Ciencia de Datos + Inteligencia Artificial con Python
# Empresa: Codins Academy

 
""" 1. Hola Mundo con Variables: Imprime el mensaje "¡Bienvenidos al curso de programación en Python!", 
  pero usando una variable para almacenar el mensaje antes de imprimirlo. """

#almaceno una variable tipo string y hago dos saltos de linea,
mensaje = "¡Bienvenidos al curso de programación en Python! \n" 
print("==========Taller #1 de Python.==============")
print("--- Primer ejercicio --- \n")
input("Para ingresar cualquier letra y pulse enter para empezar: ")
print() #hacemos un salto de linea
print(mensaje) #presentamos el mensaje de bienvenida

""" 2.	Operaciones Matemáticas Mejoradas: Declara dos variables con números aleatorios 
 realiza las operaciones de suma, resta, multiplicación, división y módulo.
 Muestra el resultado de cada operación en una línea separada."""
 
print("--- Este es el segundo ejercicio, por favor ingrese solo numeros. --- \n")
#Solicito 2 variables:
numero1 = float(input("digite el primer numero: "))
numero2 = float(input("digite el segundo numero: "))
#presento y relizo el resultado:
print() #presento un print() en blanco para hacer un salto de linea y hacer mas entendible el mensaje
print(f"El resultadao de la suma es: {numero1 + numero2}")
print(f"El resultadao de la resta es: {numero1 - numero2}")
print(f"El resultadao de la multiplicación es: {numero1 * numero2}")
print(f"El resultadao de la división es: {numero1 / numero2}")
print((f"El resultadao de la módulo es: {int(numero1 % numero2)}"))
print()#hacemos un salto de linea

"""3.	Concatenación y Formato de Texto: Crea dos variables con cadenas de texto y une ambas
 utilizando el método format() para imprimir la frase resultante."""
 
print("--- Este es el tercer ejercicio.  --- \n")
 #asignamos valores tipo string a las 2 variables
text1= "Crea dos variables con cadenas de texto"
text2= "y une ambas utilizando el método format()"
#unimos los valores y los presento en pantalla
print(f"{text1} {text2} ")
print()#hacemos un salto de linea

"""4.	Cambio de Tipos: Declara una variable con el valor "100", conviértela a tipo float, 
 luego multiplícalo por 1.5 y redondea el resultado a dos decimales. Imprime el resultado."""
variable = "100" #se declara la variable en formato string.
#? se crea una nueva variable para multiplicar y redondear,
#? la primera variable se transforma de string a float para cambiar de texto a numero.
mult= round(float(variable) * 1.5,2) #!se redondeo a 2 decimales.
print(f"su resultado es: {mult} ")
print()#hacemos un salto de linea
 
"""#5.	Impresión con Parámetros Personalizados: Imprime tres frases con diferentes separadores 
# usando sep y diferentes finales utilizando end. Asegúrate de que el texto impreso se vea ordenado y con variabilidad."""

print("------Quinto ejercicio------\n")
#se asigna texto (string) a 3 variables.
frase1 = "Imprime tres frases"
frase2 = "con diferentes separadores"
frase3= "y diferentes finales" 
#!se imprime en pantalla pero a cada variable se los separara con coma y terminara con 3 puntos.
print(frase1, frase2, frase3, sep=",", end="..." )
print()#hacemos un salto de linea

""" 6.	Multiplicación con Inputs: Solicita al usuario dos números y multiplica ambos."""

print("-----sexto ejercicio------\n")
#se solicita al usuario 2 numeros enteros
valor1=int(input("ingrese el primer numero entero: "))
valor2=int(input("ingrese el segundo numero entero: "))
print()#hacemos un salto de linea
#se realiza la multiplicacón de los valores ingresado
print(f"su resultado multiplicado es: {(valor1*valor2)}")
print()#hacemos un salto de linea

"""7.	Averiguar el Tipo de un Valor: Pide al usuario que ingrese un valor (puede ser un número o texto).
 Usa type() para determinar el tipo de datos del valor ingresado y muestra el resultado."""
 
print("-----sextimo ejercicio------\n")
#solicitamos un valor al usuario.
tipo = input("ingrese un valor: ")
#usamos el metodo type para identificar el tipo del valor ingresado: str, int, float, boolean.
print(type(tipo))
print()#hacemos un salto de linea

"""8.	Promedio con Validación: Pide al usuario que ingrese tres calificaciones. 
 Si alguna de las calificaciones  calcula y muestra el promedio."""
 
print("-----octavo ejercicio------\n")
#pedimos al usuario sus notas de sus 3 calificacione
print("se calificara del 0 al 10")
calificacion1 = float(input("ingrese su primera nota: "))
calificacion2 = float(input("ingrese su segunda nota: "))
calificacion3 = float(input("ingrese su tercera nota: "))
# lo transformo en una lista o vector
calificaciones = (calificacion1, calificacion2, calificacion3)
#sacamos el promedio de las notas de los 3 valores ingresado dividido para el numero de sus elemento
promedio = round(sum(calificaciones) / len(calificaciones),2) #! se redondea a 2 decimales
#imprimimos en pantalla el promedio
print(f"su promedio es: {promedio}")
#bonus, con esto el usuario sabra si paso
if 10>= promedio >= 8:
    print(f"usted ha aprobado con excelentes resultado con: {promedio}")
elif 8 > promedio >= 6:
    print(f"ha aprovado con: {promedio}")
elif 6> promedio >0 :
    print("lo siento no ha aprovado")
else:
    print("error los valores no estan definido dentro de la regla, solo valores entre 0 al 10")
#hacemos un salto de linea    
print()

"""9. Edad y Año de Nacimiento: Pide al usuario su edad y calcula su año de nacimiento usando la fecha actual. 
Imprime un mensaje con el año de nacimiento."""

print("-----noveno ejercicio------\n")
#solitamos al usuario el ingreso de su edad y lo transformamos en entero.
edad = int(input("inserte su edad: "))
año_Actual = 2025 #se establece el año actual.
#presentamos al usuario su año de nacimiento
print(f"su año de nacimiento es: {año_Actual - edad} \n")
print()#hacemos un salto de linea

"""10.Clasificación de Números: Solicita al usuario que ingrese tres números. Luego, 
 imprime el número más grande, el más pequeño y el promedio de los tres números."""

print("-----Decimo ejercicio------\n")
#solicitamos al usuario que ingrese 3 numero y lo transformamos a entero
num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))
num3 = int(input("ingrese el tercer numero entero: "))

#hacemos una lista con las 3 datos que ingreso el usuario.
regla = [num1, num2, num3]

#presentamos en pantalla el valos mas grande, mas pequeño y el promedio de los valores
print(f"El numero mas gande es: {max(regla)}")
print(f"El numero mas pequeño es: {min(regla)}")
#! sum: suma los valores de la lista y len: suma la cantidad de elementos que hay en la lista
print(f"El promedio de los 3 numero es: {round(sum(regla)/len(regla),2)}") #? sacamos el promedio con sum() divido para len()
print()#hacemos un salto de linea

"""11.Descuento de Producto con Validación: Solicita al usuario el precio de un producto y
 el porcentaje de descuento. calcula y muestra el precio con el descuento aplicado."""
 
print("-----Decimo primero ejercicio------\n")
 
#pedimos que el usuario ingrese el precio del producto.
producto = float(input("ingrese el precio del producto: "))
#pedimos que el usuario solicite el descuento.
print("por favor solo se realiza el descuento en numeros enteros del 0 al 100")
descuento = int(input("ingrese el porcentaje de descuento: "))
descuento_Aplicado = (producto * (descuento/100))
precio_Descontado = producto - descuento_Aplicado
print(f"Se descuenta: {descuento_Aplicado}, El precio del producto con el descuento es: {precio_Descontado}")
print()#hacemos un salto de linea


""" 12.Conversión de Divisas: Solicita al usuario que ingrese una cantidad en dólares. 
 Convierte esa cantidad a euros (1 USD = 0.85 EUR) y muestra el resultado."""
 
print("-----Decimo segundo ejercicio------\n")
 
#solicitamos al usuario que ingrese la cantidad en dolares.
usd = float(input("Ingrse la cantidad de USD: $ "))
#establecemos el precio del euro en que se encuentra actualmente.
euro= 0.85
#realizamos la conversion.
conversion = usd * euro
#presentamos el resultado.
print(f"Su conversion en euro es: € {round(conversion,2)}")
print()#hacemos un salto de linea

"""13.Cálculo de Área y Perímetro de un Rectángulo: Pide al usuario que ingrese el largo y 
 el ancho de un rectángulo. Luego, calcula y muestra el área y el perímetro."""
 
print("-----Decimo segundo ejercicio------\n")

#solicitamos al usuario que ingrese el largo y el ancho.
largo = float(input("Ingrese el largo de un rectangulo: "))
ancho = float(input("Ingrese el ancho de un rectangulo: "))
#calculamos el area bxh.
area = ancho * largo
#calculamos el perimetro de sus lados l+l+l+l.
perimetro = (ancho * 2) + (largo * 2)
#presentamos los valores.
print(f"El area del rectangulo es: {area} m^2, el perimetro del rectangulo es: {perimetro} m")