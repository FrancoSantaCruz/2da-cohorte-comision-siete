'''
Paradigma: una forma de ver/hacer las cosas (algoritmos).

Progrmación Imperativa

Paradigma Funcional: Modulos reutilizables llamdos Funciones.
def mi_funcion():
    pass

Paradigma Programación Orientada a Objetos.

# Que es una clase - objeto - instancia. 

# Definiendo mi clase "Auto"
class Auto:
    # Marca = "Ford"
    # Modelo = "Fiesta"
    # Color = "Azul"
    pass

# Instanciar una clase -> Crear una instancia de clase.
auto_franco = Auto("Toyota", "Etios", "Gris")
# auto_franco = Objeto

auto_valentina = Auto("Ford", "Fiesta", "Azul")

auto_gabriel = Auto("Chevrolet", "Camaro", "Amarillo")



### ATRIBUTOS
## Atributos de clase: Son atributos que todas las instancias
van a compartir obligatoriamente

## Atributos de Instancia: Son atributos que va a pertenecer
a cada instancia en particular

# Que es una clase - objeto - instancia. 

# Definiendo mi clase "Auto"
class Auto:
    ruedas = 4

    def __init__(self, marca, modelo, color):
        # Marca = "Ford"
        self.marca = marca

        # Modelo = "Fiesta"
        self.modelo = modelo

        # Color = "Azul"
        self.color = color

# Instanciar una clase -> Crear una instancia de clase.
# auto_franco = Objeto
auto_franco = Auto("Toyota", "Etios", "Gris")
print(auto_franco.ruedas)
print(auto_franco.marca)
print(auto_franco.modelo)
print(auto_franco.color)

print("-------------------")

auto_valentina = Auto("Ford", "Fiesta", "Azul")
print(auto_valentina.ruedas)
print(auto_valentina.marca)
print(auto_valentina.modelo)
print(auto_valentina.color)

print("-------------------")

auto_gabriel = Auto("Chevrolet", "Camaro", "Amarillo")
print(auto_gabriel.ruedas)
print(auto_gabriel.marca)
print(auto_gabriel.modelo)
print(auto_gabriel.color)

### MÉTODOS -> Los comportamientos de las clases.
## Métodos de Instancia
class Auto:
    ruedas = 4

    def __init__(self, marca, modelo, color):
        # Marca = "Ford"
        self.marca = marca

        # Modelo = "Fiesta"
        self.modelo = modelo

        # Color = "Azul"
        self.color = color

    # métodos de instancia
    def acelerar(self):
        print(f"El auto {self.marca} {self.modelo} aceleró! 🚗💨")

    def frenar(self):
        print(f"El auto {self.marca} {self.modelo} empezó a frenar! 🚗🛑")

        
auto_franco = Auto("Toyota", "Etios", "Gris")
auto_franco.frenar()
auto_valentina = Auto("Ford", "Fiesta", "Azul")
auto_valentina.acelerar()
auto_gabriel = Auto("Chevrolet", "Camaro", "Amarillo")
auto_gabriel.acelerar()
auto_gabriel.frenar()

## Métodos de clase
class Auto:
    ruedas = 4

    def __init__(self, marca, modelo, color):
        # Marca = "Ford"
        self.marca = marca

        # Modelo = "Fiesta"
        self.modelo = modelo

        # Color = "Azul"
        self.color = color

    # métodos de instancia
    def acelerar(self):
        print(f"El auto {self.marca} {self.modelo} aceleró! 🚗💨")

    def frenar(self):
        print(f"El auto {self.marca} {self.modelo} empezó a frenar! 🚗🛑")

    # método de clase
    @classmethod #Para definir que el método de abajo es un método de clase
    def incrementar_ruedas(cls):
        cls.ruedas += 1

auto_franco = Auto("Toyota", "Etios", "Gris")
print("Franco")
print(auto_franco.ruedas)

auto_valentina = Auto("Ford", "Fiesta", "Azul")
print("Valentina")
print(auto_valentina.ruedas)
auto_valentina.incrementar_ruedas()
print(auto_valentina.ruedas)

auto_gabriel = Auto("Chevrolet", "Camaro", "Amarillo")
print("Gabriel")
print(auto_gabriel.ruedas)



## Métodos estáticos
class Auto:
    ruedas = 4

    # Método constructor de la clase -> init -> initialize -> Inicializar -> Iniciar
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    # métodos de instancia
    def acelerar(self):
        print(f"El auto {self.marca} {self.modelo} aceleró! 🚗💨")

    def frenar(self):
        print(f"El auto {self.marca} {self.modelo} empezó a frenar! 🚗🛑")

    # método de clase
    @classmethod #Para definir que el método de abajo es un método de clase
    def incrementar_ruedas(cls):
        print("B")
        cls.ruedas += 1

    # métodos estáticos
    @staticmethod
    def calcular_distancia(velocidad, tiempo):
        print("C")
        return velocidad * tiempo
    

auto_franco = Auto("Toyota", "Etios", "Gris")
auto_franco.calcular_distancia(120, 4)

'''


#*******************************************
#***************  RESUMEN  *****************
#*******************************************

# Plantilla/Encuesta base -> Clase
class Auto:
    # Atributo de clase
    ruedas = 4

    # Método constructor
    def __init__(self, marca, modelo, color):
        #Atributos de instancia
        self.marca = marca
        self.modelo = modelo
        self.color = color

    # Métodos de instancia
    def acelerar(self):
        print(f"El auto {self.marca} {self.modelo} aceleró! 🚗💨")

    def frenar(self):
        print(f"El auto {self.marca} {self.modelo} empezó a frenar! 🚗🛑")

    # Métodos de clase
    @classmethod
    def incrementar_ruedas(cls):
        cls.ruedas += 1

    # Métodos estáticos
    @staticmethod
    def calcular_distancia(velocidad, tiempo):
        return velocidad * tiempo
    

# Objeto      Instancia de una clase
auto_franco = Auto("Toyota", "Etios", "Gris")








