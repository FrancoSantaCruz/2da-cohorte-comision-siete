# ESTRUCTURAS DE CONTROL
# Si - Si No - Si No, Si
# if - else  - elif

"""
edad = int(input("Ingresa tu edad para validar tu situación de voto: "))

if edad < 16:
    print("No podes votar. Sos menor de edad.")
elif edad >= 16 and edad < 18:
    print("Es opcional tu voto, pero se agradece tu patriotismo.")
elif edad < 70:
    print("Es OBLIGATORIO tu voto, te espero en la mesa")
else:
    print("Es opcional tu voto, se agradece el esfuerzo.")
"""

"""
# Quiero saber si el número ingresado es PAR. 

numero = int(input("Ingresa un número:"))

if numero % 2 == 0:
    print("El número es par")
else:
    print("No lo es.")
"""

"""
palabra = input("Ingresa una palabra:")

if palabra.isupper(): 
    print("La palabra está en mayúscula.")
elif palabra.islower():
    print("La palabra está en minúscula.")
elif palabra.isdigit():
    print("La palabra en realidad es un número.")
    palabra = int(palabra)
    resultado = palabra * 2
    print("El resultado es: ",resultado)
elif palabra.isalpha():
    print("Es una palabra")
else: 
    print("Es un caracter especial")
"""

"""
usuarios = {"Paola", "Roman", "Emmanuel", "Franco"}

usuarios = {
    "Paola": "miembro",
    "Roman": "vip",
    "Emmanuel": "administrador",
    "Franco": "miembro"
}

nombre = input("Ingresa el nombre que quieras buscar: ")

if nombre in usuarios:
    print("ACA ESTA :)")
else:
    print("No lo conozco.")
"""

#--------------------------------------------------------------------------
# BUCLES
# PARA - MIENTRAS
# FOR  - WHILE

# Para {variable} Desde {valor inicial} Hasta {valor final} Con Paso {valor} Hacer
# 	bloque de código
# FinPara

# Para valor Desde 0 Hasta 10 Con Paso 2 Hacer
#       Imprimir valor
# FinPara

# range(Hasta)
# range(Desde, Hasta)
# range(Desde, Hasta, Paso)

"""
for valor in range(0, 10, 1):
    print(valor)

for valor in range(0, 10, 2):
    print(valor)
"""

"""
usuarios = ["Paola", "Roman", "Emmanuel", "Franco"]

for nombre in usuarios:
    print(nombre)
"""

"""
usuarios = ["paOLA", "RoMaN", "EMMAnuel", "frANCo"]
print(usuarios)

for nombre in enumerate(usuarios):
    # Obtener el indice del nombre que quiero cambiar
    indice = nombre[0]
    # Hacer minúscula el nombre que está actualmente en la iteración.
    nuevo_nombre = nombre[1].capitalize()
    # cambiar el nombre mal escrito de la lista de usuarios al nuevo en minuscula mediante su indice
    usuarios[indice] = nuevo_nombre

    # usuarios[nombre[0]] = nombre[1].capitalize()

print(usuarios)
"""

# usuarios = {
#     "Paola": "miembro",
#     "Roman": "vip",
#     "Emmanuel": "administrador",
#     "Franco": "miembro"
# }

"""
for clave in usuarios:
    print(clave)
"""

"""
print(usuarios.keys())
for clave in usuarios.keys():
    print(clave)
"""

"""
print(usuarios.values())
for clave in usuarios.values():
    print(clave)
"""

"""
contador = 1

for clave, valor in usuarios.items():
    print("Iteración N°",contador)
    print("El usuario",clave,"tiene el rol",valor,"en la página.")
    contador += 1
"""

# WHILE

# Mientras <condicion sea verdadera> HACER
#       [ BLOQUE DE CODIGO ]
# Fin Mientras

"""
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
"""

"""
# BREAK
contador = 1
while contador <= 10:
    if contador == 5:
        print("El contador llegó a 5 🫡")
        break
    print(contador)
    contador += 1
"""

"""
# CONTINUE
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        print("El contador llegó a 5 🫡")
        continue
    print(contador)


print("El bucle terminó.")
"""

"""
while True:
    respuesta = input("¿Quieres salir del programa? (s/n)").lower()
    if respuesta == "s":
        break
    
    print("*")
        
print("Gracias por usar el programa 🫡")
"""

"""
bandera = True

while bandera:
    respuesta = input("¿Quieres salir del programa? (s/n)").lower()
    if respuesta == "s":
        bandera = False

    print("*")

print("Gracias por usar el programa 🫡")

numero = "-1.1"
numero=float(numero)
print(numero)

if numero.isdecimal():
    print("Lo es")
"""

# JUEGO DE ADIVINAR EL NUMERO GANADOR
# El usuario tiene 5 intentos para adivinar el número MISTERIOSO.

"""
1) Generar el número misterioso
2) Permitir que el jugador ingrese un número a adivinar
3) Validar si ese número es el número misterioso o en caso contrario, dar pistas
4) Restar intentos
"""

import random

numero_misterioso = random.randint(1, 50)
intentos = 0

while True:
    if intentos == 5:
        print("PERDISTE 🥲")
        respuesta = input("Presiona ENTER para volver a jugar")
        if respuesta == "":
            intentos = 0
            print("Bienvenido nuevamente!")
        else:
            break

    numero_adivinanza = input("Ingresa tu intento:")

    # VALIDAR EL DATO INGRESADO
    if not numero_adivinanza.isdigit():
        print("POR FAVOR! introducí un número entero 🤬")
        continue
        

    numero_adivinanza = int(numero_adivinanza)
    intentos += 1

    # 20 
    # >= 15          
    if numero_adivinanza < numero_misterioso and numero_adivinanza >= numero_misterioso - 5:
        print("Caliente 🥵, el número es por poco más bajo")
    elif numero_adivinanza < numero_misterioso:
        print("Frio 🥶, el número es muy BAJO")
    elif numero_adivinanza > numero_misterioso and numero_adivinanza <= numero_misterioso + 5:
        print("Caliente 🥵, el número es por poco más alto")
    elif numero_adivinanza > numero_misterioso:
        print("Frio 🥶, el número es muy ALTO")
    else:
        print("🥳🥳🥳¡¡¡GANASTE!!!🥳🥳🥳")
        break

print("Gracias por jugar 🙏")