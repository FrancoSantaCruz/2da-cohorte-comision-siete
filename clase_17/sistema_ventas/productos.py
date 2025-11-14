from db import conectar
from sqlite3 import Error

def agregar_producto():
    nombre = input("\nIngresar nombre del producto: ")
    precio = float(input("Ingresar precio del producto: "))

    conn, cursor = conectar()
    if not conn: 
        return
    
    try:
        cursor.execute("INSERT INTO producto (nombre, precio) VALUES (?, ?)", (nombre, precio))
        conn.commit()
        print("✅ Producto agregado.")
    except Error as e:
        print(f"❌ ERROR al agregar el producto: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def listar_productos():
    conn, cursor = conectar()
    if not conn: 
        return
    
    try:
        cursor.execute("SELECT * FROM producto;")
        productos = cursor.fetchall()

        print("\n📦 PRODUCTOS:")
        for producto in productos:
            print(f"#{producto["id"]} | {producto["nombre"]} - ARS${producto["precio"]}")
    except Error as e:
        print(f"❌ ERROR al recuperar todos los productos: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def modificar_producto():
    listar_productos()
    prod_id = int(input("\n Ingrese ID del producto a modificar: "))
    nuevo_producto = input("Ingrese el nuevo nombre: ")
    nuevo_precio = float(input("Ingrese el nuevo precio: "))

    conn, cursor = conectar()
    if not conn: 
        return
    
    try:
        cursor.execute(
            "UPDATE producto SET nombre = ?, precio = ? WHERE id = ?",
            (nuevo_producto, nuevo_precio, prod_id)
        )
        conn.commit()
        print("✏️ Producto actualizado.")
    except Error as e:
        print(f"❌ ERROR al modificar el producto: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def eliminar_producto():
    listar_productos()
    prod_id = int(input("\n Ingrese ID del producto que desea eliminar: "))

    conn, cursor = conectar()
    if not conn: 
        return
    
    try:
        cursor.execute("DELETE FROM producto WHERE id = ?", (prod_id,))
        conn.commit()
        print("🗑️ Producto eliminado")
    except Error as e:
        print(f"❌ ERROR al eliminar: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()