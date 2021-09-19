from helpers import *
from entidadesRol import *
from componentes import *
from crudArhivos import *
from nomina import *

# Menu Proceso Principal
opc=''
while opc !='5':  
    borrarPantalla()
    print("")
    menu = Menu("------------MENU PRINCIPAL----------------",["1) Mantenimiento","2) Novedades","3) Rol de Pago","4) Salir"],10,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='7':
            borrarPantalla()    
            menu1 = Menu("-----------------MENU MANTENIMIENTO-------------",["1) Empleados Administrativos","2) Empleados Obreros","3) Cargos","4) Departamentos","5) Empresa","6) Parametros","7) Salir"],10,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                borrarPantalla()
                empAdministrativos()
            elif opc1 == "2":
                borrarPantalla()
                empObreros()
            elif opc1 == "3":
                borrarPantalla()
                cargos()
            elif opc1 == "4":
                borrarPantalla()
                crearDepartamento()
            elif opc1 == "5":
                borrarPantalla()
                Mantenimiento_Empresa()
            elif opc1 == "6":
                borrarPantalla()
                print("----------------DEDUCCIONES--------------")
                archDecc = Archivo("./archivos/deducciones.txt", "|")
                infoDecc = archDecc.leer()[0]
                objDecc = Deduccion(float(infoDecc[0]), float(infoDecc[1]), float(infoDecc[2]))
                objDecc.mostrarDeduccion()
                while True:
                    gotoxy(10,8); print("Desea cambiar los valores[s/n]:")
                    resp = (input()).lower()
                    if resp in ["s","n"]:break
                    else:
                        gotoxy(50,8); print("     No Valido         ")
                        time.sleep(2)
                        gotoxy(50,8); print(" "*50)
                if resp == "s":
                    borrarPantalla()
                    parametro()
                else: pass
                gotoxy(10,10); print("*****************REGRESANDO AL MENU MANTENIMIENTO**************")
                time.sleep(2); borrarPantalla()

            elif opc1 == "7":
                break
    elif opc == "2":
        while True:
            borrarPantalla()
            menu2 = Menu("----------------MENU NOVEDADES-------------",["1) Sobretiempo","2) Prestamos","3) Salir"],10,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                sobretiempos()
            elif opc2 == "2":
                CrearPrestamos()
            elif opc2 == "3":break
    elif opc == "3":
        while True:
            borrarPantalla()
            menu3 = Menu("---------------MENU ROL----------------",["1) Rol Administrativos","2) Rol Obreros","3) Consulta Rol","4) Salir"],10,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                rolAdministrativo()
            elif opc3 == "2":
                rolObrero()
            elif opc3 == "3":
                consultaRol()
            elif opc3 == "4":
                break
    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")
           exit()
    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

