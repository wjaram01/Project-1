# ________________________________________________________________________________________________________________
# 3. TRATAMIENTO DE LISTAS
# ________________________________________________________________________________________________________________
from Operaciones_numeros import *


class Lista(Intermedio):
    def __init__(self, lista):
        self.lista = lista

    def presentarLista(self):
        for i in self.lista: print(i)

    def buscarLista(self, valor):
        for pos, ele in enumerate(self.lista):
            if ele == valor: return "Su valor esta en la posicion {} en la lista {}".format(pos+1, self.lista)
        else: return "valor no encontrado en lista"

    def listaFactorial(self):
        aux = []
        for i in self.lista:
            aux1 = super().factorial(i)
            aux.append(aux1)
        print()
        print("Los factoriales de la lista son:")
        return aux

    def listaPrimo(self):
        aux = []
        for i in self.lista:
            aux1 = super().primo(i)
            if aux1: aux.append(i)
        if not aux: print("No hay numeros primos en la lista ingresada")
        else: print("Lista de numeros primos ", aux)

    def listaNotas(self, listaNotasDiccionario):
        for i in listaNotasDiccionario:
            for elementos in i.items():
                print(elementos)

    def insertarLista(self,valor, posicion):
        aux = []
        if posicion >= len(self.lista):
            aux = self.lista
            aux.append(valor)
            return aux
        for index, value in enumerate(self.lista):
            if index == posicion:
                aux.append(valor)
                aux.append(value)
            else: aux.append(value)
        return aux

    def eliminarLista(self, valor):
        aux = []
        if valor not in self.lista: return "Valor no se encuentra en lista"
        for index, value in enumerate(self.lista):
            if valor == value: aux = self.lista[:index] + self.lista[index+1:]
        return "Valor {} eliminado de la lista: {} ".format(valor, aux)

    def retornaValorLista(self, posicion):
        aux = []
        if posicion >= len(self.lista):
            print("Se ha superado la longitud de la lista, revise la posicion [0...{}]".format(len(self.lista)-1))
            posicion = int(input("Ingrese la posicion nuevamente: "))

        for index, value in enumerate(self.lista):
            if index == posicion:
                pass
            else: aux.append(value)
        return aux


    def copiarTuplaLista(self, tupla):
        aux = []
        for value in tupla: aux.append(value)
        return "Lista: {}".format(aux)

    def vueltoLista(self, listaClientesDiccionario):
        for i in listaClientesDiccionario:
            for elementos in i.items():
                print(elementos)

