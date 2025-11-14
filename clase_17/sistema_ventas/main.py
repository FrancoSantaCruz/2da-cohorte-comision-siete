from db import crear_tablas
from productos import (
    agregar_producto,
    listar_productos,
    modificar_producto,
    eliminar_producto
)

from ventas import (
    registrar_venta,
    listar_ventas
)

def menu():
    crear_tablas()
    while True:
        print("\n=========================")
        print("    SISTEMA DE VENTAS    ")
        print("=========================")
        print("1. Agregar producto")
        print("2. Listar todos los productos")
        print("3. Modificar un producto")
        print("4. Eliminar un producto")
        print("5. Registrar una venta")
        print("6. Listar todas las ventas")
        print("7. Modificar una venta")
        print("8. Eliminar una venta")
        print("0. SALIR")
        print("=========================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            registrar_venta()
        elif opcion == "6":
            listar_ventas()
        elif opcion == "7":
            pass
        elif opcion == "8":
            pass
        elif opcion == "0":
            print("Muchas gracias!")
            break
        else:
            print("❌ OPCIÓN INVÁLIDA")
menu()