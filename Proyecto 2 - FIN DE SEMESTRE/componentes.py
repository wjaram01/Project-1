from helpers import borrarPantalla, gotoxy
import time
class Menu:
    def __init__(self,titulo="",opciones=[],col=6,fil=1):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil +=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col+5,self.fil+2)
        opc = input("Elija opcion[1...{}]:".format(len(self.opciones))) 
        return opc   

class Valida:
    def solo_numeros(self,mensaje,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil);valor = input(mensaje)
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col+50,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col+50,fil);print(" "*20)
        return valor

    def solo_letras(self,mensaje,mensajeError,col,fil):
        while True:
            gotoxy(col,fil); valor = str(input("{}".format(mensaje)))
            if valor.isalpha():
                break
            else:
                gotoxy(col + 50, fil); print(mensajeError)
                time.sleep(1)
                gotoxy(col + 50, fil); print(" " * 30)
        return valor

    def solo_decimales(self,mensaje,mensajeError,col,fil):
        while True:
            gotoxy(col,fil); valor = str(input("{}".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
                else:
                    gotoxy(col + 50, fil);
                    print(mensajeError)
                    time.sleep(1)
                    gotoxy(col + 50, fil);
                    print(" " * 30)
            except:
                gotoxy(col + 50, fil); print(mensajeError)
                time.sleep(1)
                gotoxy(col + 50, fil); print(" " * 30)
        return valor

    def validar_cedula(self, mensaje, mensajeError,col,fil):
        while True:
            gotoxy(col,fil)
            valor = input(mensaje)
            try:
                if int(valor) > 0:
                    if len(valor) == 10:
                        break
                    else:
                        gotoxy(col + 50, fil);
                        print(mensajeError)
                        time.sleep(1)
                        gotoxy(col + 50, fil);
                        print(" " * 30)
            except:
                gotoxy(col+50,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col+50,fil);print(" "*30)
        return valor

    def validar_dia(self,mensaje, mensajeError,col,fil):
        while True:
            gotoxy(col,fil)
            valor = input(mensaje)
            try:
                if 0 < int(valor) < 31:
                    break
                else:
                    gotoxy(col + 50, fil);
                    print(mensajeError)
                    time.sleep(1)
                    gotoxy(col + 50, fil);
                    print(" " * 20)
            except:
                gotoxy(col+50,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col+50,fil);print(" "*20)
        return int(valor)

    def validar_mes(self,mensaje, mensajeError,col,fil):
        while True:
            gotoxy(col,fil)
            valor = input(mensaje)
            try:
                if 0 < int(valor) < 13:
                    break
                else:
                    gotoxy(col + 50, fil);
                    print(mensajeError)
                    time.sleep(1)
                    gotoxy(col + 50, fil);
                    print(" " * 20)
            except:
                gotoxy(col+50,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col+50,fil);print(" "*20)
        return int(valor)

    def validar_ann(self,mensaje, mensajeError,col,fil):
        while True:
            gotoxy(col,fil)
            valor = input(mensaje)
            try:
                if 1900 < int(valor) < 2100:
                    break
                else:
                    gotoxy(col + 50, fil);
                    print(mensajeError)
                    time.sleep(1)
                    gotoxy(col + 50, fil);
                    print(" " * 20)
            except:
                gotoxy(col+50,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col+50,fil);print(" "*20)
        return int(valor)

    
class otra:
    pass    

