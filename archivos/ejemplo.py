"""
Manipulacion de archivos

funcion open()  es la funcion mas basica de interactuar con archivos en python
Leer, escribir, añadir funciones que nos permite la funcion open

la funcion open unicamente me permite trabajr con archivos de texto plano
(csv, json, txt, database)

variable = open("nombre del archivo", modo)

nombre del archivo => se coloque la ruta y el nombre.
modo
'r' read lectura, solo lee
'w' write escritura, borra todo y reescribe
'a' append agregar al final
'+' actualizacion o varias cosas 
'x' unicamente para creacion de archivos
'b' binario. (imagenes, audios)
't' 'textos'

SIEMPRE QUE REALICE UNA OPERACION CON UN ARCHIVO es fundamental cerrar el archivo para 
liberar recursos.

"""
#documento = open("nota.txt",'r') #lee el documento
#print(documento)

"""Metodos para interactuar con los archivos
LECTURA
"""
#read(size) lee todo el texto o el documento
#print(documento.read(10)) #lee el documento y su argumento la cantidad de caracteres
print()
#print(documento.readline(100))
#saltos_lineas = documento.readlines()
#lectura_cursor = documento.tell()
#print(saltos_lineas)
#print(lectura_cursor)

#!nuevo documento escritura
#* documento_new= open("documentos/nuevo.txt", "w")
#*si el archivo no existe se crea #ojo esto borra lo que hace el documento que ha estado escrito
#documento_new= open("documentos/nuevo.txt", "a")# a agrega texto al final
#documento_new.write("\nhola") 
#documento_new.writelines(["\ncomo estan", "\nmi nombre es Arturo"])
#documento_new.close()#* cierra el archivo
# WITH OPEN
# exacatamente lo mismo que el open pero generando un cierre del documento por defecto
# ya no hace falta declarar la variable 
#with open( nombre del archivo o ruta, modo) as nombre referente al archivo

#with open ("salarios2.txt", "w") as salario: 
    #salario.write("$ 1000 se gasta cada 15 dias en la obra")
#with open ("salarios2.txt", "a") as salario:
    #salario.write("$ 1000 se gasta cada 15 dias en la obra")
with open ("salarios2.txt", "r+") as d:
    lectura = d.read()
    print(f"el contenido es {lectura}")
    d.seek(0,2)#mueve el cursor
    d.write("\n ejemplo")
    # coloca el cursor al final
                # 0 no se mueve en posicion
                # 2 referencia seria el final del archivo