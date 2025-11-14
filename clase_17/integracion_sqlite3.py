import sqlite3
from sqlite3 import Error

def conectar():
    try:
        conn = sqlite3.connect("com7_sqlite3.db")
        conn.row_factory = sqlite3.Row # = dictionary=True

        print("✅ Conexión exitosa a la base de datos SQLite3!")
        cursor = conn.cursor()

        return conn, cursor
    except Error as e:
        print(f"❌ Error al conectar a SQLite3: {e}")
        return None, None

# Create Table
def create_table():
    conn, cursor = conectar()
    if not conn:
        return

    try:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS persona (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) NOT NULL,
                edad INTEGER,
                direccion VARCHAR(200)
            )
        """
        )
        conn.commit()
        print("✔️  Tabla 'persona' creada o verificada correctamente.")
    except Error as e:
        print(f"❌ ERROR al crear la tabla: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# CRUD
# Create person
def create_person(nombre, edad, direccion):
    conn, cursor = conectar()
    if not conn:
        return

    try:
        sql = "INSERT INTO persona (nombre, edad, direccion) VALUES (?, ?, ?)"
        valores = (nombre, edad, direccion)
        cursor.execute(sql, valores)

        conn.commit()
        print(f"✔️  Persona insertada con ID: {cursor.lastrowid}")
    except Error as e:
        print(f"❌ ERROR al registrar a la persona: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Read all person -> Traer TODOS los registros de la tabla
def read_all_person():
    conn, cursor = conectar()
    if not conn:
        return

    try:
        cursor.execute("SELECT * FROM persona;")
        personas = cursor.fetchall()

        print("📃  Todas las personas registradas: ")

        for persona in personas:
            print(f"El usuario {persona['nombre']} tiene {persona['edad']} años.")

    except Error as e:
        print(f"❌ ERROR al intentar recuperar todas las personas: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Read one person -> Traer UN solo registro de la tabla
def read_person_by_id(persona_id):
    conn, cursor = conectar()
    if not conn:
        return

    try:
        cursor.execute("SELECT * FROM persona WHERE id = ?", (persona_id,))
        persona = cursor.fetchone()

        if persona:
            print(f"🔍  Persona encontrada: {persona["nombre"]} con direccion en {persona["direccion"]}")
        else:
            print(f"⚠️  No se encontró a una persona con ese ID.")

    except Error as e:
        print(f"❌ ERROR al intentar recuperar a la persona por su ID: {e}")
        conn.rollback() #Rollback opcional
    finally:
        cursor.close()
        conn.close()

# Update person -> Modificar o editar un solo registro de la tabla
def update_person(persona_id, nombre, edad, direccion):
    conn, cursor = conectar()
    if not conn:
        return

    try:
        sql = """
            UPDATE persona
            SET nombre = ?, edad = ?, direccion = ?
            WHERE id = ?
        """
        valores = (nombre, edad, direccion, persona_id)
        cursor.execute(sql, valores)

        if cursor.rowcount > 0:
            conn.commit()
            print(f"✔️  Persona con ID {persona_id} actualizada correctamente.")
        else: 
           print("⚠️ No se encontró una persona con ese ID.") 
    except Error as e:
        print(f"❌ ERROR al actualizar a la persona: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# Delete person -> Eliminar un solo registro de la tabla
def delete_person(persona_id):
    conn, cursor = conectar()
    if not conn:
        return

    try:
        cursor.execute("DELETE FROM persona WHERE id = ?", (persona_id,))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"✔️  Persona con ID {persona_id} fué eliminada con éxito.")
        else: 
           print("⚠️ No se encontró una persona con ese ID.") 
    except Error as e:
        print(f"❌ ERROR al intentar eliminar a la persona: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


# ###################################
# REPASO COMPARATIVO MySQL vs SQLite3
# ###################################

### CONNECT()
# MySQL -> necesitabamos credenciales.
# SQLite3 -> necesita el nombre del archivo.

# MySQL -> teniamos que validar si la conexión se realizaba satisfactoriamente.
# SQLite3 -> no.

# La manera en que configurabamos que los select nos devuelva
# los datos como diccionarios
# MySQL -> cursor(dictionary = True)
# SQLite3 -> conn.row_factory = sqlite3.Row

### DEFINICION DE CAMPOS
# MySQL -> AUTO_INCREMENT
# SQLite3 -> AUTOINCREMENT

# MySQL -> INT
# SQLite3 -> INTEGER

# MySQL -> AUTO_INCREMENT PRIMARY KEY
# SQLite3 -> PRIMARY KEY AUTOINCREMENT

### PLACEHOLDER
# MySQL -> "%s"
# SQLite3 -> "?"


# #####################
# PRUEBAS DE ESCRITORIO
# #####################

# conectar()

# create_table()

# create_person("Valentina", 32, "Av. Sarmiento 2451")
# create_person("Roman", 53, "Av. San Martin 5551")
# create_person("Franco", 15, "Av. Castilli 521")
# create_person("Guillermo", 21, "Av. Alvear 868")
# create_person("Lorena", 27, "Av. Paraguay 152")

# read_all_person()

# read_person_by_id(3)
# read_person_by_id(99)

# update_person(3, "Mauricio", 23, "Av Marconi 321")
# update_person(44, "Valen", 23, "Av Marconi 321")
# read_all_person()

# delete_person(3)
# read_all_person()