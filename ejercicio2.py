"""EJERCICIO8
Genere un diccionario con los siguientes datos 
nombre, apellido, edad, puesto
luego muestre los datos en consola
"""
base_Datos= {
    "nombre:" : "Arturo",
    "apellido:" : "Parra",
    "edad:": 18,
    "puesto:" : "Dev Python"
}
print(base_Datos)

for titulo, descricion in base_Datos.items():
    print(titulo.upper(), descricion)
"""
EJERCICIO9
En base a la estructura anterior 
genere un lista de 2 diccionario solicitando el ingreso de los datos
"""
