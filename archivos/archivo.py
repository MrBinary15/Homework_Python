with open("datos.csv", "r+") as datos:
    datos1 = datos.readlines()
    print(datos1)
    print("los productos son:")
    datos.write("\n5, sacapunta, 0.25")
    datos1.pop(0)#pop elimina elementos
    
    
for dato in datos1:
    print(dato.strip())#strip elimina espacios en la final y en el incio   