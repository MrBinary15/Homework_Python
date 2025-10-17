def procesar_empleados():
    empleados = []
    list_empleados = []

    def list_empleado():
        try:
            with open("Personal.csv", 'r') as documento:
                personas = [linea.strip() for linea in documento]
                personas.pop(0)  # quita la cabecera
                for persona in personas:
                    nombre, edad, cedula, rol, salario = persona.split(",")
                    list_empleados.append({
                        "nombre": nombre,
                        "edad": int(edad),
                        "cedula": int(cedula),
                        "rol": rol,
                        "salario": float(salario)
                    })
        except Exception as e:
            print(e)

    list_empleado()  # aquí sí llamamos a la función para llenar la lista

    # Mostrar empleados con salario mayor a 200
    print("Empleados con salario mayor a 200:")
    for trabajador in list_empleados:
        if trabajador["salario"] > 200:
            print(trabajador)

    # Guardar empleados con salario mayor a 200
    with open("EmpleadosAltosSalarios.csv", "w") as archivo:
        archivo.write("Nombre,Edad,Cedula,Rol,Salario\n")
        for trabajador in list_empleados:
            if trabajador["salario"] > 200:
                archivo.write(f'{trabajador["nombre"]},{trabajador["edad"]},{trabajador["cedula"]},{trabajador["rol"]},{trabajador["salario"]}\n')

    # Mostrar empleados con edad menor a 25
    print("\nEmpleados con edad menor a 25:")
    for trabajador in list_empleados:
        if trabajador["edad"] < 25:
            print(trabajador)

    # Guardar empleados jóvenes
    with open("EmpleadosJovenes.csv", "w") as archivo:
        archivo.write("Nombre,Edad,Cedula,Rol,Salario\n")
        for trabajador in list_empleados:
            if trabajador["edad"] < 25:
                archivo.write(f'{trabajador["nombre"]},{trabajador["edad"]},{trabajador["cedula"]},{trabajador["rol"]},{trabajador["salario"]}\n')


procesar_empleados()