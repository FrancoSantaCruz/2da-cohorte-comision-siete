from db import conectar
from productos import listar_productos
from sqlite3 import Error

def registrar_venta():
    print("\nSeleccione un producto")
    listar_productos()

    producto_id = int(input("\nIngrese ID del producto vendido: "))
    cantidad = int(input("Ingrese cantidad vendida: "))

    conn, cursor = conectar()
    if not conn: 
        return
    
    try:
        cursor.execute(
            "INSERT INTO venta (producto_id, cantidad) VALUES (?, ?)",
            (producto_id, cantidad)
        )
        conn.commit()
        print("💸🤑💳🪙💰 Venta registrada.")
    except Error as e:
        print(f"❌ ERROR al registrar una venta: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


def listar_ventas():
    
    conn, cursor = conectar()
    if not conn: 
        return
    
    try:
        cursor.execute("""
            SELECT 
                venta.id AS venta_id,
                producto.nombre AS producto_nombre,
                producto.precio AS producto_precio,
                venta.cantidad AS cantidad,
                (producto.precio * venta.cantidad) AS total
            FROM venta
            JOIN producto ON producto.id = venta.producto_id;
        """)
        ventas = cursor.fetchall()

        print("\n🪙 VENTAS:")
        for venta in ventas:
            print(f"#{venta["venta_id"]} | {venta["producto_nombre"]}(ARS${venta["producto_precio"]} unidad) x {venta["cantidad"]} unidades -> Total ARS${venta["total"]}.")
    except Error as e:
        print(f"❌ ERROR al obtener las ventas: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()