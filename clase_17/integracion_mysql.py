import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conn = mysql.connector.connect(
        host="localhost", 
        user="root", 
        password="2726", 
        database="com7_mysql"
    )
        if conn.is_connected():
            print("✅ Conexión exitosa a la base de datos!")
            cursor = conn.cursor(dictionary=True) #SELECT -> Diccionario en lugar de Tupla
            return conn, cursor
        else:
            print("❌ Error al conectar a MySQL")
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
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
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                edad INT,
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
        sql = "INSERT INTO persona (nombre, edad, direccion) VALUES (%s, %s, %s)"
        valores = (nombre, edad, direccion)
        cursor.execute(sql, valores)

        conn.commit()
        print(f"✔️  Persona insertada con ID: {cursor.lastrowid}")
    except Error as e:
        print(f"❌ ERROR al crear la tabla: {e}")
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
        print(f"❌ ERROR al crear la tabla: {e}")
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
        cursor.execute("SELECT * FROM persona WHERE id = %s", (persona_id,))
        persona = cursor.fetchone()

        if persona:
            print(f"🔍  Persona encontrada: {persona["nombre"]} con direccion en {persona["direccion"]}")
        else:
            print(f"⚠️  No se encontró a una persona con ese ID.")

    except Error as e:
        print(f"❌ ERROR al crear la tabla: {e}")
        conn.rollback()
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
            SET nombre = %s, edad = %s, direccion = %s
            WHERE id = %s
        """
        valores = (nombre, edad, direccion, persona_id)
        cursor.execute(sql, valores)

        if cursor.rowcount > 0:
            conn.commit()
            print(f"✔️  Persona con ID {persona_id} actualizada correctamente.")
        else: 
           print("⚠️ No se encontró una persona con ese ID.") 
    except Error as e:
        print(f"❌ ERROR al crear la tabla: {e}")
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
        cursor.execute("DELETE FROM persona WHERE id = %s", (persona_id,))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"✔️  Persona con ID {persona_id} fué eliminada con éxito.")
        else: 
           print("⚠️ No se encontró una persona con ese ID.") 
    except Error as e:
        print(f"❌ ERROR al crear la tabla: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

# create_person("Guillermo", 21, "Av. Alvear 5231")
# create_person("Lorena", 27, "Av. Paraguay 152")

# read_all_person()

# read_person_by_id(3)
# read_person_by_id(99)

# update_person(3, "Mauricio", 23, "Av Marconi 321")
# update_person(44, "Valen", 23, "Av Marconi 321")
# read_all_person()

# delete_person(3)
# read_all_person()