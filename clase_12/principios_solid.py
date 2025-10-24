'''
S - Single Responsibility Principle | Principio de Responsabilidad Única
Una clase debe tener una sola razón para cambiar -> Una sola responsabilidad.
'''
# INCORRECTO
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


    def guardar_en_db(self):
        print(f"Guardando {self.nombre} en la base de datos")


    def enviar_email_bienvenida(self):
        print(f"Enviando email de bienvenida a {self.email}")



# CORRECTO
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class RepositorioUsuarios:
    def guardar_db(self, usuario):
        print(f"Guardando {usuario.nombre} en la base de datos...")

    def guardar_archivos(self, usuario):
        print(f"Guardando en archivo .json")


class ServicioMensajeria:
    def enviar_bienvenida(self, usuario):
        print(f"Enviando email de bienvenida a {usuario.email}")

    






'''
O - Open/Closed Principle
El código debe estar ABIERTO para extenderse
pero CERRADO para ser modificado. 
'''
# INCORRECTO
class CalculadoraDescuentos:
    def calcular(self, tipo, precio):
        if tipo == "navidad":
            return precio * 0.9
        elif tipo == "black_friday":
            return precio * 0.8
        elif tipo == "aniversario":
            return precio * 0.7
        

# CORRECTO

class Descuento:
    def aplicar(self, precio):
        return precio


class DescuentoNavidad(Descuento):
    def aplicar(self, precio):
        return precio * 0.9


class DescuentoBlackFriday(Descuento):
    def aplicar(self, precio):
        return precio * 0.8


class DescuentoAniversario(Descuento):
    def aplicar(self, precio):
        return precio * 0.7
#######
def mostrar_precio(descuento, precio):
    print("Precio final:", descuento.aplicar(precio))

desc = Descuento()
desc.aplicar()

mostrar_precio(DescuentoNavidad(), 1000)
mostrar_precio(DescuentoBlackFriday(), 1000)
mostrar_precio(DescuentoAniversario(), 1000)




'''
L - Liskov Substitution Principle
'''
# INCORRECTO
class Ave:
    def volar(self):
        print("Estoy volando!")

class colibrí(Ave):
    pass

class Pinguino(Ave):
    def volar(self):
        raise Exception("No puedo volar 😢")

# CORRECTO
class Ave:
    def poner_huevos():
        print("🥚🥚🥚🐣🐣🐣🍳")

class AveVoladora(Ave):
    def volar(self):
        print("Estoy volando!")

class Pinguino(Ave):
    def nadar(self):
        print("Estoy nadando!")






'''
I - Interface Segregation Principle
'''
# INCORRECTO
class Trabajador:
    def trabajar(self):
        pass

    def cocinar(self):
        pass

    def conducir(self):
        pass

class Programador(Trabajador):
    def trabajar(self):
        print("Escribiendo código...")

    def cocinar(self):
        pass  # No tiene sentido

    def conducir(self):
        pass  # ????


# CORRECTO
class Trabajador:
    def trabajar(self):
        pass

class Cocinero:
    def cocinar(self):
        pass
    def cortar_ingredientes(self):
        pass
    def definir_recetas(self):
        pass

class Conductor:
    def conducir(self):
        pass

class Programador(Trabajador):
    def trabajar(self):
        print("Escribiendo código...")

class Chef(Trabajador, Cocinero):
    def trabajar(self):
        print("Preparando ingredientes...")
    def cocinar(self):
        print("Cocinando comida deliciosa!")





'''
D - Dependency Inversion Principle
'''

# INCORRECTO
class Motor:
    def encender(self):
        print("Motor encendido")

class Auto:
    def __init__(self):
        self.motor = Motor()

    def arrancar(self):
        self.motor.encender()



# CORRECTO
class Motor:
    def encender(self):
        print("Motor encendido")

class MotorElectrico:
    def encender(self):
        print("Motor eléctrico encendido 🔋")

class MotorGas:
    def encender(self):
        print("Motor a gas encendido ⛽")

class Auto:
    def __init__(self, motor):
        self.motor = motor

    def arrancar(self):
        self.motor.encender()

auto1 = Auto(Motor())
auto2 = Auto(MotorElectrico())
auto3 = Auto(MotorGas())

auto1.arrancar()  
auto2.arrancar()
auto3.arrancar()

