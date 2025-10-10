# Un módulo no es más que un archivo .py (python) que contiene
# funciones, clases y variables que podemos reutilizar en otros algoritmos/programas

"""
import datetime #datetime.py
print(datetime.datetime.now().day)
print(datetime.datetime.now().month)
print(datetime.datetime.now().year)
print("---")
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)

import math #math.py
print(math.asin(0.5))
print(math.e)
print(math.pi)

import random #random.py
limite_inferior = 0
limite_superior = 100
valor_aleatorio = random.randint(limite_inferior, limite_superior)
print(valor_aleatorio)
lista = ["banana", "manzana", "pera"]
random.shuffle(lista)
print(lista)
"""

"""
import biblioteca

biblioteca_principal = []

libro_uno = biblioteca.crear_libro("Desarrollo Web", "Roman Huel", 1992)
libro_dos = biblioteca.crear_libro("CiberSecurity", "Franco Riquelme", 2001)
libro_tres = biblioteca.crear_libro("Data Analytics", "Valentina Sapag", 2012)

biblioteca.agregar_libro(biblioteca_principal, libro_uno)
biblioteca.agregar_libro(biblioteca_principal, libro_dos)
biblioteca.agregar_libro(biblioteca_principal, libro_tres)

biblioteca.mostrar_todos_libros(biblioteca_principal)

resultado = biblioteca.buscar_libro(biblioteca_principal, "CiberSecurity")
if resultado != None:
    print(resultado)
else:
    print("404: Libro no existente")
"""

"""
# Para módulos estandar
import biblioteca
import biblioteca as bbl

bbl.agregar_libro()
bbl.mostrar_todos_libros()

# Para módulos personalizados.
from biblioteca import crear_libro, agregar_libro, mostrar_todos_libros, buscar_libro
from biblioteca import (
    crear_libro as crear,
    agregar_libro as agregar,
    mostrar_todos_libros as mostrar,
    buscar_libro as buscar,
)

crear()
agregar()
mostrar()
buscar()

# PSICOPATAS = Que dios te acompañe
from biblioteca import *
"""

"""
*********************
****** TKINTER ******
*********************


"""


