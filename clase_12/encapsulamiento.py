'''
ENCAPSULAMIENTO

Ventajas
1) Protege los datos.
2) Evita errores.

class Persona:
    _piernas = 2

    def __init__(self, nombre):
        #Atributo público
        self.nombre = nombre

        #Atributo protegido
        self._dni = 14994544

        #Atributo privado
        self.__saldo = 0

    def mostrar_saldo(self):
        print(f"El saldo de la persona {self.nombre} es: {self.__saldo}")


class Adulto(Persona):
    def mostrar_dni(self):
        print(f"El dni del adulto {self.nombre} es: {self._dni}")


p = Persona("Roman")
p.mostrar_saldo()

p = Adulto("Franco")
p.mostrar_dni()

print(p.nombre)
print(p._dni)
print(p.__saldo) # Esto da error


# Método Privado
class Calculadora:

    def sumar(self, valor_uno, valor_dos):
        if self.__verificar_numeros(valor_uno, valor_dos):
            return valor_uno + valor_dos
        else:
            return "Valores incorrectos. Ingresa valores numéricos"


    def restar(self, valor_uno, valor_dos):
        if self.__verificar_numeros(valor_uno, valor_dos):
            return valor_uno - valor_dos
        else:
            return "Valores incorrectos. Ingresa valores numéricos"


    def multiplicar(self, valor_uno, valor_dos):
        if self.__verificar_numeros(valor_uno, valor_dos):
            return valor_uno * valor_dos
        else:
            return "Valores incorrectos. Ingresa valores numéricos"
    
    def __verificar_numeros(self, numero_x, numero_y):
        # Estoy validando que los dos valores pasados por parámetros 
        # sean numéricos.
        if isinstance(numero_x, (int, float)) and isinstance (numero_y, (int, float)):
            return True
        else:
            return False
    
calc = Calculadora()
print(calc.sumar(2, 10))
print(calc.restar(2, 10))
print(calc.multiplicar(2, 10))
'''



'''
# GETTERS & SETTERS
Getters -> Get -> Obtener o Traer.
Setters -> Set -> Definir o Establecer.

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    #Getter
    def get_nombre(self):
        nom = self.__nombre.capitalize()
        return f"El nombre titular de la cuenta es {nom}"
    
    #Setter
    def set_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 3:
            self.__nombre = nuevo_nombre
        else:
            print("El nombre es demasiado corto.")

p1 = Persona("fRAnCo")
print(p1.get_nombre())
p1.set_nombre("FR")
p1.set_nombre("Sergio")
print(p1.get_nombre())
'''


'''
MÉTODOS MÁGICOS | MÉTODOS ESPECIALES | DUNDER METHODS

Double Underscore

__init__()

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"""
        Este objeto cumple con la necesidad de guardar la información de una persona específica. 
        Por ejemplo: {self.nombre} tiene {self.edad} años.
        """

    def __eq__(self, el_otro_objeto):
        #        p1.edad == p2.edad
        #           26   == 22
        return self.edad == el_otro_objeto.edad
    
    def __add__(self, el_otro_objeto):
        return self.edad + el_otro_objeto.edad

p1 = Persona("Franco", 26)
p2 = Persona("Roman", 22)

print(p1 == p2)
print(p1 + p2)

__lt__ less than <
__le__ less than or equal <= 
__gt__ greater than >
__ge__ greater than or equal >=
__eq__ equal ==
__nq__ not equal !=

class Comision:
    def __init__(self, alumnos):
        self.alumnos = alumnos

    def __len__(self):
        return len(self.alumnos)
    
comision_siete = Comision(["Franco", "Emmanuel", "Tiago", "Roman", "Valentina"])
comision_uno = Comision(["Franco", "Emmanuel",])
comision_cuatro = Comision(["Tiago", "Roman", "Valentina"])

print(len(comision_siete))
print(len(comision_uno))
print(len(comision_cuatro))
'''