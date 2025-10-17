
#! =========================Proyecto final 2 - Citas medicas ====================================
# * Nombre: Arturo Parra
#? Fecha: 21/09/2025
# Bootcamp Ciencia de Datos + Inteligencia Artificial con Python
# Empresa: Codins Academy

"""
main.py - Sistema de Gestión de Pacientes y Doctores 
Conexión MySQL: host=localhost, user=root, password="", db=gestion_pacientes_simple"""

# GLOSARIO DE COMENTARIOS:
# #* Comentario importante o título
# #? Comentario de duda o descripción
# #! Comentario de advertencia o precaución



#* ===================== Importaciones necesarias ==============================
import re                      #? lo uso para validar el email con una expresión regular
from datetime import datetime, date   #? para validar fechas
import sys                     #? para salir del programa si hay un error grave

#* Conector MySQL (instalar con: pip install mysql-connector-python)
try:
    import mysql.connector
except Exception as e:
    print("[X] Falta instalar mysql-connector-python -> pip install mysql-connector-python")
    raise

#* ===================== Configuración de la base de datos =====================
DB_NAME = "gestion_pacientes_simple"
DB_CONFIG_SERVER = {
    "host": "localhost",
    "user": "root",
    "password": "root123" 
}
DB_CONFIG_DB = {
    **DB_CONFIG_SERVER,
    "database": DB_NAME
}

#* ===================== Funciones de conexión ================================
def conectar_servidor():
    #? Conecta solo al servidor (sin seleccionar base) para poder crear la BD.
    return mysql.connector.connect(**DB_CONFIG_SERVER)

def conectar_bd():
    """#* Conecta directamente a la base de datos del proyecto (ya creada)."""
    return mysql.connector.connect(**DB_CONFIG_DB)

#* ===================== Creación BD y tablas =================================
def crear_bd_si_no_existe():
    """#* Crea la BD si no existe para evitar errores al conectar a DB."""
    try:
        cnx = conectar_servidor()
        cur = cnx.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET utf8mb4")
        cnx.commit()
        cur.close(); cnx.close()
        print(f"[OK] Base de datos '{DB_NAME}' lista.")
    except mysql.connector.Error as err:
        print("[X] Error creando la BD:", err)
        sys.exit(1)  #! si no se crea la BD, no puedo seguir

def crear_tablas_si_no_existen():
    """#* Crea las tablas pacientes, doctores y citas con llaves foráneas (InnoDB)."""
    # Tabla pacientes
    ddl_pacientes = """
    CREATE TABLE IF NOT EXISTS pacientes (
        id_paciente INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
        fecha_nacimiento DATE NOT NULL,
        telefono VARCHAR(15),
        email VARCHAR(50)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    # Tabla doctores
    ddl_doctores = """
    CREATE TABLE IF NOT EXISTS doctores (
        id_doctor INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
        especialidad VARCHAR(50) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    # Tabla citas (sin CHECK para compatibilidad con MySQL 5.7)
    ddl_citas = """
    CREATE TABLE IF NOT EXISTS citas (
        id_cita INT AUTO_INCREMENT PRIMARY KEY,
        id_paciente INT,
        id_doctor INT,
        fecha_cita DATETIME NOT NULL,
        motivo TEXT,
        estado VARCHAR(20) NOT NULL,
        CONSTRAINT fk_cita_paciente
            FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente)
            ON UPDATE CASCADE ON DELETE RESTRICT,
        CONSTRAINT fk_cita_doctor
            FOREIGN KEY (id_doctor) REFERENCES doctores(id_doctor)
            ON UPDATE CASCADE ON DELETE RESTRICT
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    try:
        cnx = conectar_bd()
        cur = cnx.cursor()
        cur.execute(ddl_pacientes)
        cur.execute(ddl_doctores)
        cur.execute(ddl_citas)
        cnx.commit()
        cur.close(); cnx.close()
        print("[OK] Tablas listas.")
    except mysql.connector.Error as err:
        print("[X] Error creando tablas:", err)
        sys.exit(1)

#* ===================== Validaciones ========================
def validar_email(email):
    #* El email puede estar vacío. Si trae texto, debe ser válido.
    if email is None or email.strip() == "":
        return True  #? email es opcional
    patron = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return re.match(patron, email) is not None

def validar_fecha_nacimiento(fecha_texto):
    #* Formato requerido: YYYY-MM-DD. No puede ser futura ni menor a 1900.
    try:
        f = datetime.strptime(fecha_texto, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Formato inválido (usa YYYY-MM-DD).")
    if f > date.today():
        raise ValueError("La fecha no puede ser en el futuro.")
    if f < date(1900, 1, 1):
        raise ValueError("La fecha es demasiado antigua (mínimo 1900-01-01).")
    return f

def validar_fecha_hora_cita(fecha_hora_texto):
    """#* Formato requerido: YYYY-MM-DD HH:MM (24 horas)."""
    try:
        return datetime.strptime(fecha_hora_texto, "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError("Formato inválido (usa YYYY-MM-DD HH:MM).")

#* ===================== Gestión de Pacientes =================================
def registrar_paciente():
    print("\n== Registrar Paciente ==")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ").strip()
    telefono = input("Teléfono (opcional): ").strip()
    email = input("Email (opcional): ").strip()

    if nombre == "" or apellido == "":
        print("[X] El nombre y el apellido son obligatorios.")
        return

    try:
        validar_fecha_nacimiento(fecha_nac)
    except ValueError as e:
        print("[X] Error en fecha de nacimiento ->", e)
        return

    if not validar_email(email):
        print("[X] Email inválido.")
        return

    try:
        cnx = conectar_bd()
        cur = cnx.cursor()
        cur.execute(
            "INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, telefono, email) VALUES (%s,%s,%s,%s,%s)",
            (nombre, apellido, fecha_nac, telefono if telefono else None, email if email else None)
        )
        cnx.commit()
        print("[OK] Paciente creado con ID:", cur.lastrowid)
        cur.close(); cnx.close()
    except mysql.connector.Error as err:
        print("[X] Error en BD:", err)

def listar_pacientes():
    print("\n== Listado de Pacientes ==")
    try:
        cnx = conectar_bd()
        cur = cnx.cursor()
        cur.execute("SELECT id_paciente, nombre, apellido, fecha_nacimiento, telefono, email FROM pacientes ORDER BY id_paciente")
        filas = cur.fetchall()
        if not filas:
            print("(sin registros)")
        else:
            print(f"{'ID':<5} {'Nombre':<15} {'Apellido':<15} {'Nacimiento':<12} {'Teléfono':<15} {'Email'}")
            print("-"*80)
            for f in filas:
                print(f"{f[0]:<5} {f[1]:<15} {f[2]:<15} {str(f[3]):<12} {str(f[4] or ''):<15} {f[5] or ''}")
        cur.close(); cnx.close()
    except mysql.connector.Error as err:
        print("[X] Error en BD:", err)

#* ===================== Gestión de Doctores ==================================
def agregar_doctor():
    print("\n== Agregar Doctor ==")
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    especialidad = input("Especialidad: ").strip()

    if nombre == "" or apellido == "" or especialidad == "":
        print("[X] Nombre, apellido y especialidad son obligatorios.")
        return

    try:
        cnx = conectar_bd()
        cur = cnx.cursor()
        cur.execute(
            "INSERT INTO doctores (nombre, apellido, especialidad) VALUES (%s,%s,%s)",
            (nombre, apellido, especialidad)
        )
        cnx.commit()
        print("[OK] Doctor agregado con ID:", cur.lastrowid)
        cur.close(); cnx.close()
    except mysql.connector.Error as err:
        print("[X] Error en BD:", err)

def eliminar_doctor():
    print("\n== Eliminar Doctor ==")
    try:
        id_d = int(input("ID del doctor a eliminar: ").strip())
    except ValueError:
        print("[X] Debe ser un número.")
        return

    try:
        cnx = conectar_bd()
        cur = cnx.cursor()

        #! Verifico si el doctor tiene citas, si tiene, NO permito borrar (control referencial a nivel app)
        cur.execute("SELECT COUNT(*) FROM citas WHERE id_doctor=%s", (id_d,))
        cantidad = cur.fetchone()[0]
        if cantidad and cantidad > 0:
            print(f"[X] No se puede eliminar: el doctor tiene {cantidad} cita(s) registradas. Cancela o reasigna esas citas primero.")
            cur.close(); cnx.close()
            return

        cur.execute("DELETE FROM doctores WHERE id_doctor=%s", (id_d,))
        cnx.commit()
        if cur.rowcount == 0:
            print("[X] No existe un doctor con ese ID.")
        else:
            print("[OK] Doctor eliminado.")
        cur.close(); cnx.close()
    except mysql.connector.Error as err:
        print("[X] Error en BD:", err)

def listar_doctores():
    print("\n== Listado de Doctores ==")
    try:
        cnx = conectar_bd()
        cur = cnx.cursor()
        cur.execute("SELECT id_doctor, nombre, apellido, especialidad FROM doctores ORDER BY id_doctor")
        filas = cur.fetchall()
        if not filas:
            print("(sin registros)")
        else:
            print(f"{'ID':<5} {'Nombre':<15} {'Apellido':<15} {'Especialidad'}")
            print("-"*60)
            for f in filas:
                print(f"{f[0]:<5} {f[1]:<15} {f[2]:<15} {f[3]}")
        cur.close(); cnx.close()
    except mysql.connector.Error as err:
        print("[X] Error en BD:", err)

#* ===================== Gestión de Citas =====================================
def programar_cita():
    print("\n== Programar Cita ==")
    try:
        id_p = int(input("ID paciente: ").strip())
        id_d = int(input("ID doctor: ").strip())
    except ValueError:
        print("[X] Los IDs deben ser numéricos.")
        return

    fecha_hora = input("Fecha y hora (YYYY-MM-DD HH:MM): ").strip()
    motivo = input("Motivo (opcional): ").strip()

    try:
        validar_fecha_hora_cita(fecha_hora)
    except ValueError as e:
        print("[X] Error en fecha/hora ->", e)
        return

    try:
        cnx = conectar_bd()
        cur = cnx.cursor()

        #! Verifico que existan paciente y doctor
        cur.execute("SELECT 1 FROM pacientes WHERE id_paciente=%s", (id_p,))
        if not cur.fetchone():
            print("[X] El paciente no existe.")
            cur.close(); cnx.close()
            return
        cur.execute("SELECT 1 FROM doctores WHERE id_doctor=%s", (id_d,))
        if not cur.fetchone():
            print("[X] El doctor no existe.")
            cur.close(); cnx.close()
            return

        # estado por defecto: Programada
        cur.execute("""
            INSERT INTO citas (id_paciente, id_doctor, fecha_cita, motivo, estado)
            VALUES (%s,%s,%s,%s,%s)
        """, (id_p, id_d, fecha_hora, motivo if motivo else None, "Programada"))
        cnx.commit()
        print("[OK] Cita programada con ID:", cur.lastrowid)
        cur.close(); cnx.close()
    except mysql.connector.Error as err:
        print("[X] Error en BD:", err)

def listar_citas():
    print("\n== Listado de Citas ==")
    try:
        cnx = conectar_bd()
        cur = cnx.cursor()
        cur.execute("""
            SELECT c.id_cita, c.fecha_cita, c.estado,
                   p.id_paciente, p.nombre, p.apellido,
                   d.id_doctor, d.nombre, d.apellido, d.especialidad,
                   c.motivo
            FROM citas c
            LEFT JOIN pacientes p ON p.id_paciente = c.id_paciente
            LEFT JOIN doctores d ON d.id_doctor = c.id_doctor
            ORDER BY c.fecha_cita DESC, c.id_cita DESC
        """)
        filas = cur.fetchall()
        if not filas:
            print("(sin registros)")
        else:
            print(f"{'ID':<5} {'Fecha/Hora':<17} {'Estado':<12} {'Paciente':<22} {'Doctor (Esp.)':<28} {'Motivo'}")
            print("-"*120)
            for r in filas:
                idc, fecha, estado, pid, pnom, pape, did, dnom, dape, desp, mot = r
                paciente_txt = f"[{pid}] {pnom} {pape}" if pid else "(sin)"
                doctor_txt = f"[{did}] {dnom} {dape} ({desp})" if did else "(sin)"
                print(f"{idc:<5} {str(fecha)[:16]:<17} {estado:<12} {paciente_txt:<22} {doctor_txt:<28} {mot or ''}")
        cur.close(); cnx.close()
    except mysql.connector.Error as err:
        print("[X] Error en BD:", err)

def cambiar_estado_cita():
    print("\n== Cambiar Estado de Cita ==")
    try:
        idc = int(input("ID de la cita: ").strip())
    except ValueError:
        print("[X] Debe ser un número.")
        return

    print("Estados: 1) Programada  2) Completada  3) Cancelada")
    opcion = input("Elige (1-3): ").strip()
    mapa = {"1": "Programada", "2": "Completada", "3": "Cancelada"}
    nuevo_estado = mapa.get(opcion, "Programada")

    try:
        cnx = conectar_bd()
        cur = cnx.cursor()
        cur.execute("UPDATE citas SET estado=%s WHERE id_cita=%s", (nuevo_estado, idc))
        cnx.commit()
        if cur.rowcount == 0:
            print("[X] No existe una cita con ese ID.")
        else:
            print("[OK] Estado actualizado a:", nuevo_estado)
        cur.close(); cnx.close()
    except mysql.connector.Error as err:
        print("[X] Error en BD:", err)

#* ===================== Menús (texto sencillo) ================================
def menu_pacientes():
    while True:
        print("\n--- Gestión de Pacientes ---")
        print("1. Registrar nuevo paciente")
        print("2. Listar pacientes")
        print("3. Volver")
        opcion = input("Opción (1-3): ").strip()
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            listar_pacientes()
        elif opcion == "3":
            break
        else:
            print("[X] Opción inválida.")

def menu_doctores():
    while True:
        print("\n--- Gestión de Doctores ---")
        print("1. Agregar doctor")
        print("2. Eliminar doctor (control referencial)")
        print("3. Listar doctores")
        print("4. Volver")
        opcion = input("Opción (1-4): ").strip()
        if opcion == "1":
            agregar_doctor()
        elif opcion == "2":
            eliminar_doctor()
        elif opcion == "3":
            listar_doctores()
        elif opcion == "4":
            break
        else:
            print("[X] Opción inválida.")

def menu_citas():
    while True:
        print("\n--- Gestión de Citas ---")
        print("1. Programar cita")
        print("2. Listar citas")
        print("3. Cambiar estado de cita")
        print("4. Volver")
        opcion = input("Opción (1-4): ").strip()
        if opcion == "1":
            programar_cita()
        elif opcion == "2":
            listar_citas()
        elif opcion == "3":
            cambiar_estado_cita()
        elif opcion == "4":
            break
        else:
            print("[X] Opción inválida.")

def menu_principal():
    while True:
        print("\n=== Sistema Clínica Médica ===")
        print("1. Gestión de Pacientes")
        print("2. Gestión de Doctores")
        print("3. Gestión de Citas")
        print("4. Salir")
        opcion = input("Opción (1-4): ").strip()
        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_doctores()
        elif opcion == "3":
            menu_citas()
        elif opcion == "4":
            print("Hasta pronto.")
            break
        else:
            print("[X] Opción inválida.")

#* ===================== Punto de entrada =====================================
def main():
    print("Inicializando... (creando BD y tablas si faltan)")
    crear_bd_si_no_existe()
    crear_tablas_si_no_existen()
    menu_principal()

if __name__ == "__main__":
    main()
