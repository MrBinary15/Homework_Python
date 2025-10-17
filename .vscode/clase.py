"""
Manipulacion de archivos

funcion open()  es la funcion mas basica de interactuar con archivos en python
Leer, escribir, añadir funciones que nos permite la funcion open

la funcion open unicamente me permite trabajr con archivos de texto plano
(csv, json, txt, database)

variable = open("nombre del archivo", modo)

nombre del archivo => se coloque la ruta y el nombre.
modo
'r' read lectura
'w' write escritura
'a' append agregar
'+' actualizacion o varias cosas 
'x' unicamente para creacion de archivos
'b' binario. (imagenes, audios)
't' 'textos'

SIEMPRE QUE REALICE UNA OPERACION CON UN ARCHIVO es fundamental cerrar el archivo para 
liberar recursos.

"""

documento = open("nota.txt", "r") # Abrir el archivo en modo lectura tipo txt
print(documento)

"""Metodos para interactuar con los archivos
LECTURA
"""
#read(size) lee todo el texto o el documento
#print("Leo todo")
#print(documento.read())
#print(documento.read(10))

#readline() lee una linea completa incluyendo salto de linea
print("Linea por linea")
print(documento.readline())
print(documento.tell()) # tell() me indica la posicion del cursor
print(documento.readline())
print(documento.tell())

#readlines() lee toda las lineas del archivo y devuelve en una lista
lineas = documento.readlines() # tambien guarda los salto de linea
print(lineas)

documento.close()

"""Metodos para interactuar con los archivos
ESCRITURA "w" abre el documento y lo reescribe desde 0
Si el archivo no existe lo crea
"""
nota=open("documentos/contactos.txt","w")

# write() escribe una caedna de texto o string

nota.write("Pedro \n")
#writelines()
# no se colocan saltos de linea por defecto
nota.writelines(["Juan \n", "carlos"])
nota.close
print("Archivo Escrito")

"""Metodos para interactuar con los archivos
Agregacion o append "a" 
"""
productos=open("documentos/productos.txt","a")
productos.write("\nCOMPUTADORA")
print("Archivo actualizado")
productos.close()

# WITH OPEN
# exacatamente lo mismo que el open pero generando un cierre del documento por defecto
# ya no hace falta declarar la variable 
#with open( nombre del archivo o ruta, modo) as nombre referente al archivo

ruta="salarios.txt"
with open(ruta,"a") as salarios:
    salarios.write("\nPRUEBA")
    
print( "Uso de modo +")
with open(ruta,"r+") as d: # r+ lectura y escritura
    contenido=d.readlines()
    print("el contenido es: ")
    print(contenido)
    d.write("\n Esta es mi escritura")
    print("listo")
    
    # ? podemos mover el cursor => seek()
    d.seek(0,2) # coloca el cursor al final
                # 0 no se mueve en posicion
                # 2 referencia seria el final del archivo
    d.write("asdasdasds")
    print("listo")
    

# Buena practica 
# MANIPULAR CON FUNCIONES SEPARADAS UN ARCHIVO

# en su mayoria open with open manipula csv, db

# Obtener los productos con sus precios 
with open("documentos/items.csv",'r') as products:
    productos=products.readlines()
    print(productos)
    productos.pop(0) # pop por defecto elimina el ultimo elemento => (0) la posicion deseada
    print("los productos son: ")
    for item in productos:
        print(item.strip()) # elimina espacio y saltos de linea al inico y final
    
#agregar un objeto
with open("documentos/items.csv","a") as products:
    products.write("\n3,goma,0.75")
    

# Algoritmo real
"""
db <=> app <=> usuario

1. leer la DB
2. Mostrar la DB optenida la user
3. El usuario interactua
4. Confirma el stock en DB
5. Se genera la comprar con la factura
6. Se actuliza la db con la compra

""" 


# Ejemplo de automatizacion ( envio de correo masivos ).
    

    
    
    
    


    
    
    
    










