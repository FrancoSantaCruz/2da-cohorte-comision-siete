"""
Una función es un bloque de código DEFINIDO
el cual puede recibir(o no) datos
procesa esos datos en un algoritmo
y puede devolver(o no) una respuesta.
"""

"""
# ESTRUCTURA BASICA
def saludar_comision():
    print("Hola")
    print("comisión")
    print("siete")
    print("🧑‍🏫")

saludar_comision()

resultado = input("Ingresa un numero")
# Recibe un mensaje
# Imprime ese mismo mensaje en terminal
# Pone en espera la terminal
# Obtiene el valor enviado por terminal
# devuelve como resultado ese valor.
"""

"""
# RETORNO
def saludar_comision():
    return "Hola comisión siete 🧑‍🏫"

respuesta = saludar_comision()
print(respuesta)

print(saludar_comision())
"""

"""
# PARAMETROS & ARGUMENTOS -> variables momentáneas y locales.

#                               PARAMETROS
def saludar_comision(numero_comision, tipo_saludo):
    return f"{tipo_saludo} comisión {numero_comision} 🧑‍🏫"

#                              ARGUMENTOS
resultado = saludar_comision("dos", "Holaa")
print(resultado)

resultado = saludar_comision("siete", "Buenos días")
print(resultado)

resultado = saludar_comision("cuatro", "Adioss")
print(resultado)

resultado = saludar_comision("nueve", "Hi")
print(resultado)


def sumar(valor_uno, valor_dos):
    resultado = valor_uno + valor_dos
    return resultado

print(sumar(5, 10))
print(sumar(10, 15))
print(sumar(2500, 500))
"""


"""
# TIPOS DE PARAMETROS
# Parámetros posicionales
def saludar_comision(numero_comision, tipo_saludo):
    return f"{tipo_saludo} comisión {numero_comision} 🧑‍🏫"

print(saludar_comision("siete", "Hola"))

# Valor por Defecto
def saludar_comision(numero_comision, tipo_saludo="Holaa"):
    return f"{tipo_saludo} comisión {numero_comision} 🧑‍🏫"

saludar_comision()
print(saludar_comision("siete"))
print(saludar_comision("siete", "Buenos días"))

# *args
def sumar(*args):
    resultado = 0
    for valor in args:
        resultado += valor

    return resultado


res = sumar(15, 25, 45, 5, 10, 50, 200, 10, 5)
print(f"El resultado de la operación es: {res}")

# **kwargs
def receta_de_cocina(titulo, **kwargs):
    print("****************************")
    print(f"RECETA DE {titulo.upper()}")
    print("****************************")
    for ingrediente, cantidad in kwargs.items():
        print(f"- {cantidad} de {ingrediente}.")

receta_de_cocina(
    "Empanadas de carne",
    tapas_de_empanadas=12,
    carne="1/2 kg",
    aceitunas="a gusto",
    huevos="4 unidades",
    cebolla="1/2 kg"
)

receta_de_cocina(
    "pastel de papa",
    papa="2 kg",
    carne="1 kg",
    aceitunas="a gusto",
    huevos="4 unidades",
    cebolla="1/2 kg"
)
"""

'''
# JUEGO MODULARIZADO
def generador_numero_ganador():
    import random
    return random.randint(1, 50)

def pedir_numero():
    numero = input("Ingresa tu intento:")

    if not numero.isdigit():
        print("POR FAVOR! introducí un número entero 🤬")
        return None
        
    return int(numero)

def verificar_intento(adivinanza, misterioso):
    if adivinanza < misterioso and adivinanza >= misterioso - 5:
        print("Caliente 🥵, el número es por poco más bajo")
    elif adivinanza < misterioso:
        print("Frio 🥶, el número es muy BAJO")
    elif adivinanza > misterioso and adivinanza <= misterioso + 5:
        print("Caliente 🥵, el número es por poco más alto")
    elif adivinanza > misterioso:
        print("Frio 🥶, el número es muy ALTO")
    else:
        print("🥳🥳🥳¡¡¡GANASTE!!!🥳🥳🥳")
        return True
    return False

def iniciar_juego():
    numero_misterioso = generador_numero_ganador()
    intentos = 0

    while True:
        if intentos == 5:
            print("PERDISTE 🥲")
            respuesta = input("Presiona ENTER para volver a jugar")
            if respuesta == "":
                intentos = 0
                numero_misterioso = generador_numero_ganador()
                print("Bienvenido nuevamente!")
                continue
            else:
                break

        numero_adivinanza = pedir_numero()
        if numero_adivinanza == None:
            continue

        intentos += 1
            
        if verificar_intento(numero_adivinanza, numero_misterioso):
            break

    print("Gracias por jugar 🙏")

iniciar_juego()

# verificar_intento(10, 12)
# verificar_intento(5, 12)
# verificar_intento(14, 12)
# verificar_intento(20, 12)
# verificar_intento(12, 12)

# print(pedir_numero())
# print(type(pedir_numero()))
'''

'''
# variable alcance GLOBAL
nombres = ["Franco", "Emmanuel", "Roman"]

def saludar_comision(numero_comision, tipo_saludo, lista):
    # Variable alcance LOCAL
    mensaje = f"{tipo_saludo} comisión {numero_comision} 🧑‍🏫"
    print(lista)
    return mensaje

print(saludar_comision("siete", "Hola", nombres))
'''