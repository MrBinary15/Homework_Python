
#! =========================Taller n° 7 ====================================
# * Nombre: Arturo Parra
#? Fecha: 20/09/2025
# Bootcamp Ciencia de Datos + Inteligencia Artificial con Python
# Empresa: Codins Academy

"""Clase CuentaBancaria (Encapsulamiento)
Requisitos:
Atributos privados: __saldo y __titular.
Métodos públicos:
depositar(monto): Añade dinero al saldo.
retirar(monto): Resta dinero del saldo (validando que no sea mayor al saldo disponible).
consultar_saldo(): Muestra el saldo actual.

"""
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular   # atributo privado
        self.__saldo = saldo       # atributo privado
        
    def depositar(self, monto):
        if monto > 0: # no puede haber depostivos negativos
            self.__saldo += monto
            print(f"Se depositaron ${monto}. Saldo actual: ${self.__saldo}")
        else:
            print("El monto a depositar debe ser positivo.")
            
    def retirar(self, monto):
            if monto > 0: # monto valido
                if monto <= self.__saldo:
                    self.__saldo -= monto
                    print(f"Se retiraron ${monto}. Saldo actual: ${self.__saldo}")
                else:
                    print("Fondos insuficientes.")
            else:
                print("El monto a retirar debe ser positivo.")
                
    def consultar_saldo(self):
        return f"Saldo actual: ${self.__saldo}"
    def consultar_titular(self):
        return f"Titular: {self.__titular}"

cuenta = CuentaBancaria("Juan Pérez", 1000)
print(cuenta.consultar_titular())
print(cuenta.consultar_saldo())

cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(2000) # fondos insuficientes

class CuentaBancaria:

    def __init__(self,titular,saldo=0):        
        self.__saldo = saldo
        self.__titular = titular
    
    def depositar(self,monto):
        self.__saldo+=monto
        
    def retirar(self,monto):
        if monto>self.__saldo:
            return ("Monto mayor al Saldo")
        else:
            self.__saldo =self.__saldo - monto
            return (f"Usted retiro {monto}")    
    def consultar_saldo(self):
        return (f"Su Saldo Actual es: {self.__saldo}")    


"""
Juego de Cartas (POO Avanzado)
Crea clases para representar un juego de cartas simple:
Carta: Tiene palo (♥, ♦, ♣, ♠) y valor (A, 2, ..., K).
Mazo: Contiene 52 cartas y métodos como barajar() y repartir().
Jugador: Tiene una mano de cartas.
"""
import random 

class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
    marca = "patito"
    def __str__ (self):
        return (f" {self.valor} de {self.palo}")

class Naipe:
    palos=["Corazon","Diamantes","Treboles","Picas"]
    valor=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    #creacion del naipe
    def __init__(self):
        self.cartas = [Carta(palos,valor) for palos in self.palos for valor in self.valor]# Crea cada Carte en el naipe
    #barajar
    def barajar(self):
        random.shuffle(self.cartas) # para usar shuffle es necesario el random
    #Repartir
    def repatir(self):
        return self.cartas.pop()
    
class Jugador:
    def __init__(self,nombre,edad):
        self.nombre = nombre # atributo dinamico que yo asigno el valor al crearlo
        self.edad = edad # 
        self.mano=[] # atributo dinamico asignando el valor con logica
    
    # recibir_carta
    def recibir_carta(self, carta):
        self.mano.append(carta)
    # mostrar_mano()
    def ver_mano(self):
        for carta in self.mano:
            print(f" {carta}")
    # lanzar una carta
    def lanzarcarta(sefl):
        random.shuffle(sefl.mano)
        carta = sefl.mano[-1]  # selecciona la ultima carta     
        return (f"lanzo la carta:{carta}")
            
naipe = Naipe()
naipe.barajar()
    
jugador1=Jugador("Carlos", 29)
jugador2=Jugador("Maria", 25)
    
for jugador in range(5):
    jugador1.recibir_carta(naipe.repatir())
    jugador2.recibir_carta(naipe.repatir())
print("Jugador 1") 
jugador1.ver_mano()
print("Jugador2")
jugador2.ver_mano()


"""
Sistema de Gestión de Empleados
Descripción del Problema:
Una empresa necesita desarrollar un sistema para gestionar su personal. Debes crear una estructura de clases que represente diferentes tipos de empleados, cada uno con características y comportamientos específicos.
Requisitos Técnicos:
Clase Persona:
Atributos: nombre (string) y edad (int)
Método: presentarse() que retorna un string con la presentación
Clase Abstracta Trabajador (ABC):
Métodos abstractos: calcular_salario() y trabajar()
Clase Empleado (hereda de Persona y Trabajador):
Atributos adicionales: salario_base (float) y _fecha_contratacion (privado)
Implementar los métodos abstractos
Getter para la fecha de contratación formateada
Clase Gerente (hereda de Empleado):
Atributo adicional: bono (float)
Sobrescribir calcular_salario() para incluir el bono
Sobrescribir trabajar() con comportamiento específico
Clase Desarrollador (hereda de Empleado):
Atributo adicional: lenguaje (string)
Sobrescribir trabajar() para indicar el lenguaje de programación
Funcionalidades Esperadas:
Herencia múltiple: Empleado hereda de Persona y Trabajador
Abstracción: Trabajador como clase abstracta
Polimorfismo: Métodos calcular_salario() y trabajar() con comportamientos diferentes
Encapsulación: Fecha de contratación como atributo privado
Manejo de fechas: Formateo correcto de la fecha
"""
from abc import ABC, abstractmethod
from datetime import datetime

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
    def presentarse(self):
        return f"Soy {self.nombre}"

class Trabajador(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass
    
    @abstractmethod
    def trabajar(self):
        pass
    
class Empleado(Persona, Trabajador):
    def __init__(self,nombre,edad, salario_base):
        Persona.__init__(self,nombre, edad)
        self.salario_base = salario_base
        self.__fechadecontrato = datetime.now() # obten fecha y hora actual
    
    def calcular_salario(self):
        return self.salario_base
    
    def trabajar(self):
        return "trabajando....."
    
    def get_fecha(self):
        return self.__fechadecontrato.strftime("%d/%m/%Y, %H:%M:%S")

class Gerente(Empleado):
    def __init__(self, nombre ,edad, salario_base, bono):
        super().__init__(nombre, edad ,salario_base)
        self.bono = bono
        
    def calcular_salario(self):
        return self.salario_base + self.bono
    
    def trabajar(self):
        return "Controlando al personal"
        
empleados = [
    Gerente("Juan",35,1000,500),
    Gerente("Guillermo", 55, 1000, 1000),
    Gerente("Felipe",29,200,100)  
]

for empleado in empleados:
    print(empleado.presentarse())
    print(empleado.trabajar())
    print(f"su salario es {empleado.calcular_salario()}")
    print(f"fecha de contratacion fue {empleado.get_fecha()}")