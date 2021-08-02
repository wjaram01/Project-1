# ________________________________________________________________________________________________________________
# 1. OPERACIONES CON NUMEROS
# ________________________________________________________________________________________________________________


class Menu:
    def __init__(self, lista):
        self.lista = lista

    def crearMenu(self):
        for j in range(0, len(self.lista)):
            print(self.lista[j])
        aux = int(input(("Selecione la opcion [1...{}]: ".format(len(self.lista)))))
        return aux


class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self):
        print("{} + {} = {}".format(self.numero1, self.numero2, (self.numero1 + self.numero2)))

    def resta(self):
        print("{} - {} = {}".format(self.numero1, self.numero2, (self.numero1 - self.numero2)))

    def multiplicacion(self):
        print("La multiplicacion entre los dos numeros es: {}".format((self.numero1 * self.numero2)))

    def division(self):
        while True:
            if self.numero2 != 0:
                print("La division entre los dos numeros es: {}".format((self.numero1 / self.numero2)))
                break
            elif self.numero2 == 0:
                print("Division sobre cero no aceptada, reingrese los numeros")  # Condicion si el segundo numero es 0
                self.numero1 = int(input("Ingrese el dividendo: "))
                self.numero2 = int(input("Ingrese el divisor diferente de 0: "))


class calEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)

    def multiplicacion(self):  # aplicar polimorfismo
        print(self.numero1 * self.numero2)

    def exponente(self):
        exponenciacion = self.numero1 ** self.numero2
        print("El valor del exponente {} elevado a {} es de: {}".format(self.numero1, self.numero2, exponenciacion))

    def valorAbsoluto(self, numero):
        if numero < 0 : print("El valor absoluto de {} es {}".format(numero, (numero * -1)))
        else: print("El valor absoluto de {} es {}".format(numero, numero))


class calCientifica(Calculadora):
    PI = 3.1416

    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)

    def circunferencia(self, radio):
        circunferencia = 2 * radio * calCientifica.PI
        print("La circunferencia del circulo de radio {} es de: {} mts.".format(radio, circunferencia))

    def areaCirculo(self, radio):
        area_circunferencia = calCientifica.PI * (radio ** 2)
        print("El area del circulo de radio {} es de: {} mts^2.".format(radio, area_circunferencia))

    def areaCuadrado(self, lado):
        area_cuadrado = lado * lado
        print("El area del cuadrado de lado {} es de: {} mts^2.".format(lado, area_cuadrado))
