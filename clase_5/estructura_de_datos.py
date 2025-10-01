# variable = True

# string, int, float y bool
# ESTRUCTURA DE DATOS

"""
[] Listas -> list. Arreglos/Vectores/Arrays
Cada dato dentro de una estructura de datos se le llama ELEMENTO.
- Ordenadas
- Mutables
- Aceptar datos duplicados
- Son dinámicas
"""

# Ordenadas
# indices           0   ,     1    ,   2   ,   3
# lista_frutas = ["banana", "manzana", "pera", "kiwi"]

# print(lista_frutas)
# print(lista_frutas[2])

# Mutables
# lista_frutas[1] = "naranja"
# print(lista_frutas)

# lista_ejemplo = ["Franco", 26, True, 1.75, "Franco"]
# print(lista_ejemplo)

# Dinamismo
# lista_frutas = ["banana", "manzana", "pera", "kiwi"]
# lista_verduras = ["papa", "brocoli", "tomate", "lechuga"]

# lista_supermercado = ["harina", "huevos", lista_frutas, "leche", lista_verduras]
# print(lista_supermercado)

#      0   ,     1   ,                  2                   ,    3   ,                    4
# ['harina', 'huevos', ['banana', 'manzana', 'pera', 'kiwi'], 'leche', ['papa', 'brocoli', 'tomate', 'lechuga']]
# print(lista_frutas[2])
# print(lista_verduras[3])

# print(lista_supermercado[2][2])
# print(lista_supermercado[4][3])

# lista_supermercado.append("fosforos")
# print(lista_supermercado)

# lista_supermercado.remove("harina")
# print(lista_supermercado)

"""
() Tupla -> tuple
- Ordenadas
- InMutables
- Aceptar datos duplicados
- Son dinámicas
"""

# tupla_frutas = ("banana", "manzana", "pera", "kiwi")
# tupla_verduras = ("papa", "brocoli", "tomate", "lechuga")

# print(tupla_frutas[3])
# print(tupla_verduras[1])

# tupla_frutas = ("banana", "manzana", "pera", "pera", "pera")
# print(tupla_frutas.count("pera"))


"""
{} Conjuntos -> set
- desOrdenadas
- Mutables
- NO Acepta datos duplicados * 
- Son dinámicas
"""

# conjunto_frutas = {"banana", "manzana", "pera", "kiwi", "kiwi", "kiwi"}
# print(conjunto_frutas[2])
# conjunto_frutas.add("naranja")

# print(conjunto_frutas)

# tupla_frutas = ("banana", "manzana", "pera", "pera", "pera")

# conjunto = set(tupla_frutas)

# tupla_frutas = list(conjunto)
# print(tupla_frutas)

# Union - Interseccion - Diferencia
# conjunto_frutas = {"banana", "manzana", "pera", "kiwi", "tomate"}
# conjunto_verduras = {"papa", "brocoli", "tomate", "lechuga", "kiwi"}

# Union |
# union_conjunto = conjunto_frutas | conjunto_verduras
# print(union_conjunto)

# Intersección &
# interseccion_conjunto = conjunto_frutas & conjunto_verduras
# print(interseccion_conjunto)

# Diferencia -
# diferencia_conjunto = conjunto_frutas - conjunto_verduras
# print(diferencia_conjunto)

# verduras_no_le_gustan_por_caprichosa = {"limon", "mandioca", "brocoli"}

# conjunto = union_conjunto - verduras_no_le_gustan_por_caprichosa
# print(conjunto)

"""
{'clave': valor, 'clave': valor, ...} Diccionarios -> dict
- Ordenadas *
- Mutables
- NO Acepta datos duplicados *
- Son dinámicas
"""
tupla_frutas = ("banana", "manzana", "pera", "kiwi")
conjunto_verduras = {"papa", "brocoli", "tomate", "lechuga"}

mi_diccionario = {
    "nombre": "Franco", 
    "edad": 26, 
    "estudiante": False,
    "lista_supermercado": {
        "frutas": tupla_frutas,
        "verduras": conjunto_verduras
    },
    # "lista_frutas_por_comprar": tupla_frutas,
    # "lista_verduras_por_comprar": conjunto_verduras
    }

# mi_diccionario["edad"] = 30

# print(mi_diccionario)

# mi_diccionario["estado_civil"] = "Soltero"

# print(mi_diccionario)

# print(mi_diccionario.keys())
# print("------")
# print(mi_diccionario.values())

lista_frutas = ["banana", "manzana", "pera", "kiwi"]
lista_verduras = ["papa", "brocoli", "tomate", "lechuga"]

lista_supermercado = ["harina", "huevos", lista_frutas, "leche", lista_verduras]

# PARA
# contador = 1
# for fruta in lista_frutas:
#     print(contador,") ",fruta)
#     contador += 1
