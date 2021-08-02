from Operaciones_numeros import *
from Calculadoras import *
from Lista import *
from Cadena import *

import os
# ________________________________________________________________________________________________________________
# 1. OPERACIONES CON NUMEROS
# ________________________________________________________________________________________________________________


class Menu:
    def __init__(self, lista):
        self.lista = lista

    def crearMenu(self):
        for j in range(0, len(self.lista)):
            print(self.lista[j])
        lista = input(("Selecione la opcion [1...{}]: ".format(len(self.lista))))
        return lista


while True:
    print("-------MENU PRINCIPAL-----------")
    Menu.principal = Menu(("1) Calculadora", "2) Operacion de Numeros", "3) Tratamiento de Listas", "4) Operaciones de cadena", "5) Salir"))
    resp = Menu.principal.crearMenu()  # Esta funcion imprime la lista y a su vez retorna el numero de la opcion

    if resp == '1':  # Menu caluladora
        os.system("cls")
        print("Para accesar al menu de calculadora necesita ingresar dos numeros ")
        n1 = int(input("Ingrese el primer numero: "))  # INGRESO DE NUMEROS PARA LA CLASE
        n2 = int(input("Ingrese el segundo numero: "))

        while True:
            os.system("cls")
            Menu.Calculadora = Menu(("1) Suma", "2) Resta", "3) Multiplicacion", "4) Division", "5) Exponente", "6) Valor absoluto", "7) Circunferencia", "8) Area de circulo", "9) Area de cuadrado", "10) Salir"))
            resp_Calculadora = Menu.Calculadora.crearMenu()
            Usuario = Calculadora(n1, n2)
            Usuario1 = calEstandar(n1, n2)
            Usuario2 = calCientifica(n1, n2)

            if resp_Calculadora == '1':
                os.system("cls")
                print("-----SUMA------")
                Usuario.suma()
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Calculadora == '2':
                os.system("cls")
                print("-----RESTA------")
                Usuario.resta()
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Calculadora == '3':
                os.system("cls")
                print("-----MULTIPLICACION------")
                Usuario.multiplicacion()
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Calculadora == '4':
                os.system("cls")
                print("--------DIVISION--------")
                Usuario.division()
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Calculadora == '5':
                os.system("cls")
                print("---------EXPONENTE--------")
                Usuario1.exponente()
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Calculadora == '6':
                os.system("cls")
                print("--------VALOR ABSOLUTO--------")
                numero = float(input("Ingrese un numero: "))
                Usuario1.valorAbsoluto(numero)
                input("Presione una tecla para continuar...")

            elif resp_Calculadora == '7':
                os.system("cls")
                print("----------CALCULAR LA CIRCUNFERENCIA--------")
                radio = float(input("ingrese el radio: "))
                Usuario2.circunferencia(radio)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Calculadora == '8':
                os.system("cls")
                print("-----------AREA DEL CIRCULO__________")
                radio = float(input("ingrese el radio: "))
                Usuario2.areaCirculo(radio)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Calculadora == '9':
                os.system("cls")
                print("-------------AREA CUADRADO-----------")
                lado = float(input("ingrese el lado: "))
                Usuario2.areaCuadrado(lado)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Calculadora == '10': break

            else: print("Opcion no valida")

    elif resp == '2':  # Menu de operacion con numeros
        print("--------------------OPERACIONES DE NUMEROS------------")
        while True:
            os.system("cls")
            Menu.Op_numeros = Menu(("1) Presentar numeros de 1 a n", "2) Sumar numero de 1 a n", "3) Multiplo de cualquier numero", "4) Presentar divisores de un numero", "5) Numero Primo", "6) Factorial de un numero", "7) Fibonacci de una seriae de numeros", "8) Numero Perfecto", "9) Primos gemelos", "10) Numeros Amigos", " 11) Salir"))
            resp_Op_numeros = Menu.Op_numeros.crearMenu()
            Usuario = Basico()
            Usuario1 = Intermedio()

            if resp_Op_numeros == '1':
                os.system("cls")
                print("------------PRESENTAR NUMEROS DE 1 A N----------")
                n = int(input("Ingrese el numeros a contar: "))
                Usuario.numerosN(n)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_numeros == '2':
                os.system("cls")
                print("--------------ACUMULADOR DE 1 A N---------------")
                n = int(input("Ingrese el numeros a acumular: "))
                Usuario.sumaN(n)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_numeros == '3':
                os.system("cls")
                print("--------------CALCULAR MULTIPLOS DE UN NUMEROS------------")
                numero = int(input("Ingrese el numeros a calcular multiplos: "))
                multiplo = int(input("Ingrese el multiplo que se desea comprobar"))
                Usuario.multiplos(numero, multiplo)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_numeros == '4':
                os.system("cls")
                print("--------------CALCULAR DIVISORES DEL UN NUMERO-----------")
                numero = int(input("Ingrese el numeros a calcular los divisores: "))
                Usuario.divisoresNumero(numero)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_numeros == '5':
                os.system("cls")
                print("---------------COMPROBAR PRIMO-----------------")
                numero = int(input("Ingrese el numeros a comprobar si es primo: "))
                Usuario.primo(numero)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_numeros == '6':
                os.system("cls")
                print("---------------CALCULAR FACTORIAL--------------")
                numero = int(input("Ingrese el numeros a calcular el factorial: "))
                Usuario1.factorial(numero)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_numeros == '7':
                os.system("cls")
                print("---------------CALCULAR FIBONACCI--------------")
                numero = int(input("Ingrese el numero a calcular la posicion fibonacci: "))
                Usuario1.fibonacci(numero)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_numeros == '8':
                os.system("cls")
                print("---------------COMPROBAR SI ES PERFECTO------------")
                numero = int(input("Ingrese el numeros a comprobar si es perfecto: "))
                Usuario.perfecto(numero)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_numeros == '9':
                os.system("cls")
                print("----------------COMPROBAR SI SON PRIMOS GEMELOS-----------------")
                n1 = int(input("Ingrese el primer numero: "))
                n2 = int(input("INgrese el segundo numero: "))
                print(Usuario1.primosGemelos(n1, n2))
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_numeros == '10':
                os.system("cls")
                print("----------------COMPROBAR SI LOS NUMEROS SON AMIGOS--------------")
                n1 = int(input("Ingrese el primer numero: "))
                n2 = int(input("Ingrese el segundo numero: "))
                print(Usuario1.amigos(n1, n2))
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_numeros == '11':
                os.system("cls")
                break

            else:
                print("opcion no valida")
                os.system("cls")

    elif resp == '3':  # Menu de operaciones con listas
        os.system("cls")
        aux = []
        print("Antes de ingresar al menu listas, debe crear una lista")
        n = int(input("Cuantos numeros debe ingresar en la lista: "))
        for i in range(n):
            valor = int(input("Ingrese un numero ({}): ".format(i+1)))
            aux.append(valor)
        print(aux)
        os.system("cls")
        while True:
            os.system("cls")
            print("----------------------OPERACIONES CON LISTAS----------------------")
            Menu.Tr_listas = Menu(("1) Recorres y presentar los datos de una lista", "2) Buscar valor de una lista", "3) Retornar un lista con los factoriales", "4) Retornar una lista de numeros primos", "5) Recorrer una lista de dicionario con notas de alumnos", "6) Insertar un dato de una lista dada la posicion", "7) Eliminar todas las ocurrencias en un Lista", "8) Retornar cualquier valor de una lista eliminandolo", "9) Copiar cada elemento de una tupla a una lista", "10) Dar el vuelto a varios clientes", " 11) Salir"))
            resp_Tr_listas = Menu.Tr_listas.crearMenu()
            Usuario = Lista(aux)

            if resp_Tr_listas == '1':
                os.system("cls")
                print("----------------PRESENTAR LISTA-------------")
                Usuario.presentarLista()
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Tr_listas == '2':
                os.system("cls")
                print("-----------------BUSCAR VALOR EN UNA LISTA---------------")
                valor = int(input("ingrese el numero: "))
                print(Usuario.buscarLista(valor))
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Tr_listas == '3':
                os.system("cls")
                print("---------------RETORNAR UNA LISTA CON LOS FACTORIALES-----------------")
                print(Usuario.listaFactorial())
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Tr_listas == '4':
                os.system("cls")
                print("-------------------RETORNAR UNA LISTA DE NUMEROS PRIMOS-------------------")
                Usuario.listaPrimo()
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Tr_listas == '5':
                os.system("cls")
                listaNotasDiccionario = []
                print("-----------RECORRER UNA LISTA DE DICCIONARIOS CON NOTAS DE ALUMNOS---------")
                print("Se necesita crear un diccionario, cuando alumnos desea ingresar?")
                n = int(input())
                for i in range(n):
                    alumno = str(input("Ingrese el nombre del alumno: "))
                    nota1 = float(input("Ingrese la nota 1: "))
                    nota2 = float(input("Ingrese la nota 2: "))
                    aux = {"nombre" : alumno, "nota1": nota1, "nota2" : nota2}
                    listaNotasDiccionario.append(aux)
                    os.system("cls")
                Usuario.listaNotas(listaNotasDiccionario)
                input("presione una tecla para continuar..")

            elif resp_Tr_listas == '6':
                os.system("cls")
                print("----------------INSERTAR UN VALOR EN A LISTA-----------")
                valor = int(input("Ingrese el valor: "))
                posicion = int(input("Ingrese la posicion"))
                print(Usuario.insertarLista(valor, posicion))
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Tr_listas == '7':
                os.system("cls")
                print("-----------ELIMINAR OCURRENCIAS EN UNA LISTA------------")
                valor = int(input("Ingrese el valor: "))
                print(Usuario.eliminarLista(valor))
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Tr_listas == '8':
                os.system("cls")
                print("--------------RETORNAR UNA VALOR DE UNA LISTA ELIMINANDOLO------------")
                print(" ")
                print(Usuario.lista)
                posicion = int(input("Ingrese una posicion de [0... {}] posicion: ".format(len(Usuario.lista)-1)))
                os.system('cls')
                print(Usuario.retornaValorLista(posicion))
                input("Presione una tecla para continuar...")

            elif resp_Tr_listas == '9':
                os.system("cls")
                aux = []
                print("-------------------COPIAR TUPLA A LISTA--------------")
                print("Creando tupla")
                ele = int(input("Cuantos numeros desea ingresar: "))
                for i in range(ele):
                    n = int(input("Ingrese un numero ({}): ".format(i+1)))
                    aux.append(n)
                os.system("cls")
                tupla = tuple(aux)
                print(tupla)
                print(Usuario.copiarTuplaLista(tupla))
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Tr_listas == '10':
                os.system("cls")
                listaClientesDiccionario = []
                print("-----------RECORRER UNA LISTA DE DICCIONARIOS CON VUELTOS DE CLIENTES---------")
                print("Se necesita crear un diccionario, cuantos clientes desea ingresar?")
                n = int(input())
                for i in range(n):
                    cliente = str(input("Ingrese el nombre del cliente: "))
                    cupo = float(input("Ingrese la cupo: "))
                    aux = {"nombre": cliente, "cupo": cupo}
                    listaClientesDiccionario.append(aux)
                    os.system("cls")
                Usuario.vueltoLista(listaClientesDiccionario)
                input("presione una tecla para continuar..")

            elif resp_Tr_listas == "11":
                os.system("cls")
                break

            else:
                os.system("cls")
                print("Ingrese una opcion valida")

    elif resp == '4':  # Menu de operaciones con cadena
        os.system("cls")
        print("Antes de ingresar al menu cadena debe ingresar una cadena: ")
        cadena = input("Ingrese una oracion: ")
        while True:
            print("----------OPERACIONES DE CADENA----------")
            Menu.Op_cadenas = Menu(("1) Recorrer y presentar los datos de una cadena", "2) Buscar un carcater e una cadena", "3) Retornar una lista con las posiciones dado un caracter de la cadena", "4) Retornar una lista con todas las palabras de una cadena ", "5) Retornar una cadena a partir de una lista", "6) Insertar un dato en una cadena dada la posicion", "7) Eliminar todas las ocurrencias en una cadena", "8) Retornar cualquier valor de una cadena eliminandolo", "9) Concatenar cadenas", "10) Salir"))
            resp_Op_cadenas = Menu.Op_cadenas.crearMenu()
            Usuario = Cadena(cadena)

            if resp_Op_cadenas == '1':
                os.system("cls")
                print("---------------RECORRER Y PRESENTAR CADENA----------------")
                Usuario.recorrerCadena()
                os.system("cls")

            elif resp_Op_cadenas == '2':
                os.system("cls")
                print("---------------------BUSCAR UN CARACTER EN UNA CADENA-------------")
                buscado = input("Ingrese el caracter a buscar: ")
                print(Usuario.buscarCaracter(buscado))
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_cadenas == '3':
                os.system("cls")
                print("------------RETORNAR LA POSICION DE UN CARACTER EN UNA CADENA------------")
                caracter = input("Ingrese el caracter a buscar: ")
                Usuario.listaPosiciones(caracter)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_cadenas == '4':
                os.system("cls")
                print("----------------RETORNAR UNA LISTA CON LAS PALABRAS DE UNA CADENA--------------------")
                print(Usuario.listaPalabras())
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_cadenas == '5':
                os.system("cls")
                print("---------------RETORNAR UNA CADENA CON DE UNA LISTA DE PALABRAS----------------")
                print(Usuario.cadenaLista())
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_cadenas == '6':
                os.system("cls")
                print("------------------INSERTAR DATO EN UNA CADENA DADA LA POSICION----------------")
                print(Usuario.cadena)
                buscado = input("Ingrese el caracter o palabra a ingresar: ")
                posicion = int(input("Ingrese la posicion: "))
                print(Usuario.insertarDato(buscado, posicion))
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_cadenas == '7':
                os.system("cls")
                print("------------------ELIMINAR OCURRENCIAS EN A CADENA------------")
                buscado = input("Ingrese el caracter o palabra a eliminar")
                Usuario.eliminarOcurrencias(buscado)
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_cadenas == '8':
                os.system("cls")
                print("-------------RETORNAR UN VALOR DE LA CADENA ELIMINANDOLO--------------")
                print(Usuario.cadena)
                posicion = int(input("ingrese las posicion: "))
                os.system("cls")
                print(Usuario.retornaValor(posicion))
                input("Presione una tecla para continuar...")
                os.system("cls")

            elif resp_Op_cadenas == '9':
                os.system("cls")
                print("---------------AGREGAR DATOS A UNA CADENA-------------------")
                print(Usuario.cadena)
                dato = input("Ingrese el dato a ingresar en la cadena: ")
                posicion = input("Ingrese  la posicion donde desea agregar el dato")
                print("CONCATENADO")
                print(Usuario.cadena)
                print(Usuario.concatenarCadena(dato))
                input("Presione una tecla para continuar...")
                os.system("cls")

            else:
                break
                os.system("cls")
    elif resp == '5': exit()
