# ________________________________________________________________________________________________________________
# 4. OPERACIONES DE CADENAS
# ________________________________________________________________________________________________________________

class Cadena:
    def __init__(self, cadena):
        self.cadena = cadena

    def recorrerCadena(self):
        for i in self.cadena: print(i)

    def buscarCaracter(self, buscado):
        for index, value in enumerate(self.cadena):
            if value == buscado:
                return "El caracter esta en la posicion {} ".format(index)
        return "El caracter no se encuentra en la cadena"

    def listaPosiciones(self, caracter):
        lista = []
        for index, value in enumerate(self.cadena):
            if value == caracter: lista.append(index)
        if not lista: print("El caracter o existe en la cadena")
        else: print(lista)

    def listaPalabras(self):
        aux = self.cadena
        aux = aux.split(" ")
        print("Los palabras fueron agregadas a una lista: ")
        return aux

    def cadenaLista(self):
        aux = self.cadena.split(" ")
        aux = " ".join(aux)
        aux += "."
        return aux

    def insertarDato(self, buscado, posicion):
        aux = ""
        if posicion > len(self.cadena):
            posicion = int(input("Ingrese otro valor de [0..{}]".format(len(self.cadena)-1)))
        for index, value in enumerate(self.cadena):
            if index == posicion:
                aux += buscado
                aux += value
            else: aux += value
        return aux

    def eliminarOcurrencias(self, buscado):
        aux= ""
        for i in self.cadena:
            if i == buscado:
                pass
            else: aux += i
        print(aux)

    def retornaValor(self, posicion):
        aux = ""
        for index, value in enumerate(self.cadena):
            if index == posicion:
                print("El valor es {}".format(value))
            else: aux += value
        return aux
    def concatenarCadena(self, dato):
        aux = self.cadena
        aux += " "
        aux += dato
        return aux
