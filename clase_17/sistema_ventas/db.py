import sqlite3
from sqlite3 import Error

def conectar():
    try:
        conn = sqlite3.connect("ventas.db")
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()
        return conn, cursor
    except Error as e:
        print(f"❌ Error al conectar a la BD: {e}")
        return None, None
    
def crear_tablas():
    conn, cursor = conectar()
    if not conn:
        return
    
    try:
        # 1 venta -> 1 solo producto.
        # 1 producto -> en muchas ventas
        # ventas -> producto (1:n)

        # Tabla de producto
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS producto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL
            );
        """)

        # Tabla de venta (FK)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS venta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto_id INTEGER NOT NULL,
                cantidad INTEGER NOT NULL,
                FOREIGN KEY (producto_id) REFERENCES producto(id)
            );
        """)

        conn.commit()
        print("✔️  Tablas creadas correctamente.")
    except Error as e:
        print(f"❌ Error al crear las tablas: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()



#     try:
        

#     except Error as e:
#         print(f"❌ ERROR ****: {e}")
#         conn.rollback()
#     finally:
#         cursor.close()
#         conn.close()