### HERENCIA
'''
## ESTRUCTURA PRINCIPAL DE HERENCIA

class Vehiculo:
    def __init__(self, marca, modelo, color, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando 🚗💨")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} frenó 🛑🚗")

class Auto(Vehiculo):
    pass

class Moto(Vehiculo):
    pass


vehiculo_franco = Vehiculo("Toyota", "Etios", "Gris", 4)
vehiculo_franco.acelerar()
print(vehiculo_franco.ruedas)

auto_valentina = Auto("Ford", "Fiesta", "Azul", 4)
auto_valentina.acelerar()
auto_valentina.frenar()
print(auto_valentina.ruedas)

moto_laura = Moto("Honda", "Biz", "Rojo", 2)
moto_laura.acelerar()
'''


'''
## ADHESION Y REDEFINICION DE MÉTODOS EN CLASES HIJAS

class Vehiculo:
    def __init__(self, marca, modelo, color, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando 🚗💨")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} frenó 🛑🚗")

class Auto(Vehiculo):
    def abrir_puerta(self):
        print(f"El dueño apagó la alarma y abrio la puerta del {self.marca} {self.modelo}.")


class Moto(Vehiculo):
    def acelerar(self):
        print(f"La {self.marca} {self.modelo} está acelerando 🏍️💨")

    def frenar(self):
        print(f"La {self.marca} {self.modelo} frenó 🛑🏍️")


vehiculo_franco = Vehiculo("Toyota", "Etios", "Gris", 4)


auto_valentina = Auto("Ford", "Fiesta", "Azul", 4)
auto_valentina.abrir_puerta()
auto_valentina.acelerar()
auto_valentina.frenar()

moto_laura = Moto("Honda", "Biz", "Rojo", 2)
moto_laura.acelerar()
moto_laura.frenar()
'''

'''
## FUNCIÓN SUPER()

class Vehiculo:
    def __init__(self, marca, modelo, color, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando 🚗💨")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} frenó 🛑🚗")


class Auto(Vehiculo):
    def __init__(self, marca, modelo, color, ruedas, duenio):
        super().__init__(marca, modelo, color, ruedas)
        self.duenio = duenio

    def abrir_puerta(self):
        print(f"{self.duenio} apagó la alarma y abrio la puerta del {self.marca} {self.modelo}.")


class Moto(Vehiculo):
    def acelerar(self):
        super().acelerar()
        print(f"La {self.marca} {self.modelo} está acelerando 🏍️💨")

    def frenar(self):
        print(f"La {self.marca} {self.modelo} frenó 🛑🏍️")


vehiculo_franco = Vehiculo("Toyota", "Etios", "Gris", 4)

auto_valentina = Auto("Ford", "Fiesta", "Azul", 4, "Valentina")
auto_valentina.abrir_puerta()

moto_laura = Moto("Honda", "Biz", "Rojo", 2)
moto_laura.acelerar()
'''

'''
### HERENCIA MULTIPLE

class Nadador:
    def saludar(self):
        print("Te saludo desde el agua!")

    def nadar(self):
        print("Nadando en el agua")

class Caminante:
    def saludar(self):
        print("Te saludo desde la orilla!")

    def caminar(self):
        print("Caminando sobre tierra")

class Pinguino(Nadador, Caminante):
    pass

happy_feet = Pinguino()
happy_feet.saludar()


# MRO Method Resolution Order
# Orden de Búsqueda de Métodos
print(Pinguino.mro())

# [
#   <class '__main__.Pinguino'>, 
#   <class '__main__.Nadador'>, 
#   <class '__main__.Caminante'>, 
#   <class 'object'>
# ]


class SerVivo():
    def presentarse(self):
        print("Soy un ser vivo")

class Nadador(SerVivo):
    def presentarse(self):
        print("Soy un nadador")
        super().presentarse()

class Caminante(SerVivo):
    def presentarse(self):
        print("Soy un caminante")
        super().presentarse()

class Pinguino(Nadador, Caminante):
    def presentarse(self):
        print("Soy un pinguino")
        super().presentarse()
        print("¿Los pinguinos vuelan?")


print(Pinguino.__mro__)
p = Pinguino()
p.presentarse()
'''

'''
### POLIMORFISMO
# Poli -> Muchos o multiple
# Morfismo (Morpho) -> Formas
# Multiples formas

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def calcular_sueldo_anual(self):
        sueldo_anual = 12 * self.sueldo * (1 + 1/100) # +%1
        print(f"El sueldo anual de {self.nombre} (EMPLEADO BASE) es de ARS${sueldo_anual}")


class Programador(Empleado):
    def calcular_sueldo_anual(self):
        sueldo_anual = 12 * self.sueldo * (1 + 10/100) # +%10
        print(f"El sueldo anual de {self.nombre} (PROGRAMADOR) es de ARS${sueldo_anual}")

class Diseniador(Empleado):
    def calcular_sueldo_anual(self):
        sueldo_anual = 12 * self.sueldo * (1 + 7/100) # +%7
        print(f"El sueldo anual de {self.nombre} (DISEÑADOR) es de ARS${sueldo_anual}")



empleados = [
    Empleado("Franco", 1500),
    Programador("Gisela", 2200),
    Diseniador("Roman", 1800),
    Empleado("Sergio", 2600),
    Programador("Emmanuel", 1450),
    Diseniador("Rodrigo", 3300),
    Empleado("Maria", 2600),
    Programador("Laura", 1450),
    Diseniador("Valentina", 3000),
]


def liquidacion_sueldos_anuales():
    for empleado in empleados:
        empleado.calcular_sueldo_anual()

liquidacion_sueldos_anuales()
'''