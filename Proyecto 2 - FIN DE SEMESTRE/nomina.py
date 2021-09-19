from componentes import *
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesRol import *
from datetime import *
import time
# Procesos de las Opciones del Menu Mantenimiento
def empAdministrativos():
    borrarPantalla()
    gotoxy(10,4);print("__________________CREACION DE EMPLEADO ADMINISTRATIVO________________")
    valida = Valida()
    nom = valida.solo_letras("Ingrese el nombre del empleado: ", "Ingrese solo letras : ",10,5)
    # Objeto Deprtamento
    archiDep = Archivo("./archivos/departamento.txt", "|")
    while True:
        dep = valida.solo_numeros("Ingrese numero departamento:","!Ingrese solo numero! ", 10, 6)
        if int(dep) +1 > len(archiDep.leer()):
            gotoxy(40,6); print("              No existe                 "); time.sleep(2)
            gotoxy(40,6), print(" "*50)
            pass
        else: break
    infoDep = archiDep.buscar(dep)
    objDep = Departamento(infoDep[1], infoDep[0])
    gotoxy(60, 6); print("---------->" + objDep.descripcion)
    # Objeto Cargo
    archiCargo = Archivo("./archivos/cargo.txt", "|")
    while True:
        carg = valida.solo_numeros("Ingrese numero cago: ","Ingrese solo numero : ", 10, 7)
        if int(carg) +1 > len(archiCargo.leer()):
            gotoxy(40,7); print("              No existe                 "); time.sleep(2)
            gotoxy(40,7), print(" "*50)
            pass
        else: break
    infoCargo = archiCargo.buscar(carg)
    objCargo = Cargo(infoCargo[1], infoCargo[0])
    gotoxy(60,7); print("---------->" + objCargo.descripcion)
    # ---------------------------------------------------------------------

    dir = valida.solo_letras("Ingrese la direccion: ","Ingrese solo letras:",10,8)
    ced = valida.validar_cedula("Numero de cedula: ", "Dato no invalido", 10, 9)
    telf = valida.validar_cedula("Numero de telefono: ", "Dato no valido", 10, 10)
    dia = valida.validar_dia("Ingrese dia de ingreso: ", "Dato no valido ", 10, 11)
    mes = valida.validar_mes("Ingrese mes de ingreso: ", "Dato no valido ", 10, 12)
    ann = valida.validar_ann("Ingrese año de ingreso: ", "Dato no valido", 10, 13)
    fechaing = date(ann, mes, dia)
    sueldo = valida.solo_decimales("Numero sueldo: ", "!Ingrese solo numero! ", 10, 14)
    archiEmp = Archivo("./archivos/administrativo.txt", "|")
    ListaEmpAdm = archiEmp.leer()
    numid = len(ListaEmpAdm) + 1
    Empleadoid = "A" + str(numid)
    objEmpleado = Administrativo(nom, objDep, objCargo
                                 , dir, ced, telf, fechaing, sueldo, Empleadoid)
    infoEmpleado = objEmpleado.getEmpleado()
    while True:
        grabar = valida.solo_letras("Esta seguro de Grabar El registro(s/n):", "Ingrese solo letra:", 15, 15)
        if grabar in ['s', 'n']:
            break
        else:
            pass
    if grabar == "s":
        archiEmp.escribirM([infoEmpleado[:-1]], "a")
        gotoxy(10, 16); print("****************TRABAJADOR INGRESADO AL SISTEMA*****************"); time.sleep(2)
        gotoxy(10, 17); print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)

    else: gotoxy(10, 16); print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)


def empObreros():
    gotoxy(10, 4);print("__________________CREACION DE EMPLEADO OBRERO________________")
    valida = Valida()
    nom = valida.solo_letras("Ingrese el nombre del empleado: ", "Ingrese solo letras : ",10,5)
    # Objeto Deprtamento
    archiDep = Archivo("./archivos/departamento.txt", "|")
    while True:
        dep = valida.solo_numeros("Ingrese numero departamento:","!Ingrese solo numero! ", 10, 6)
        if int(dep) +1 > len(archiDep.leer()):
            gotoxy(40,6); print("              No existe                 "); time.sleep(2)
            gotoxy(40,6), print(" "*50)
            pass
        else: break
    infoDep = archiDep.buscar(dep)
    objDep = Departamento(infoDep[1], infoDep[0])
    gotoxy(60, 6); print("---------->" + objDep.descripcion)
    # Objeto Cargo
    archiCargo = Archivo("./archivos/cargo.txt", "|")
    while True:
        carg = valida.solo_numeros("Ingrese numero cago: ","Ingrese solo numero : ", 10, 7)
        if int(carg) +1 > len(archiCargo.leer()):
            gotoxy(40,7); print("              No existe                 "); time.sleep(2)
            gotoxy(40,7), print(" "*50)
            pass
        else: break
    infoCargo = archiCargo.buscar(carg)
    objCargo = Cargo(infoCargo[1], infoCargo[0])
    gotoxy(60,7); print("---------->" + objCargo.descripcion)
    # ---------------------------------------------------------------------

    dir = valida.solo_letras("Ingrese la direccion: ","Ingrese solo letras:",10,8)
    ced = valida.validar_cedula("Numero de cedula: ", "Dato no invalido", 10, 9)
    telf = valida.validar_cedula("Numero de telefono: ", "Dato no valido", 10, 10)
    dia = valida.validar_dia("Ingrese dia de ingreso: ", "Dato no valido ", 10, 11)
    mes = valida.validar_mes("Ingrese mes de ingreso: ", "Dato no valido ", 10, 12)
    ann = valida.validar_ann("Ingrese año de ingreso: ", "Dato no valido", 10, 13)
    fechaing = date(ann, mes, dia)
    sueldo = valida.solo_decimales("Numero sueldo: ", "!Ingrese solo numero! ", 10, 14)
    archiObr = Archivo("./archivos/obrero.txt", "|")
    ListaEmpObr = archiObr.leer()
    numid = len(ListaEmpObr) + 1
    Empleadoid = "O" + str(numid)
    objEmpleado = Obrero(nom, objDep, objCargo
                                 , dir, ced, telf, fechaing, sueldo, Empleadoid)
    infoEmpleado = objEmpleado.getEmpleado()
    while True:
        grabar = valida.solo_letras("Esta seguro de Grabar El registro(s/n):","Ingrese solo letra:",15,15)
        if grabar in ['s','n']: break
        else: pass
    if grabar == "s":
        archiObr.escribirM([infoEmpleado[:-1]], "a")
        gotoxy(10,16); print("****************TRABAJADOR INGRESADO AL SISTEMA*****************")
        time.sleep(2)
        gotoxy(10, 17); print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)
    else: gotoxy(10,16); print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)

def cargos():
   borrarPantalla()
   valida = Valida()
   gotoxy(20,2);print("__________________MANTENIMIENTO DE CARGOS______________________")
   gotoxy(15,5);print("Descripcion Cargo: ")
   gotoxy(33,5)
   desCargo = input()
   archiCargo = Archivo("./archivos/cargo.txt","|")
   cargos = archiCargo.leer()
   if cargos : idSig = int(cargos[-1][0])+1
   else: idSig=1
   cargo = Cargo(desCargo,idSig)
   datos = cargo.getCargo()
   datos = '|'.join(datos)
   while True:
       grabar = valida.solo_letras("Esta seguro de Grabar El registro(s/n):", "Ingrese solo letra:", 15, 6)
       if grabar in ['s', 'n']:
           break
       else:
           pass
   if grabar == "s":
    archiCargo.escribir([datos],"a")
    gotoxy(10, 7); print("****************CARGO INGRESADO AL SISTEMA*****************"); time.sleep(2)
    gotoxy(10, 8);print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)
   else:
       gotoxy(10, 7); print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)
# ...........................................................
# Opciones del Menu Novedades
def sobretiempos():
   borrarPantalla()
   gotoxy(20,2);print("INGRESO DE HORAS EXTRAS")
   empleado,entEmpleado = [],None
   aamm,h50,h100=0,0,0
   while not empleado:
      gotoxy(15,5);print("Empleado ID[    ]: ")
      gotoxy(27,5);id = input().upper()
      archiEmpleado = Archivo("./archivos/obrero.txt","|")
      empleado = archiEmpleado.buscar(id)
      if empleado:
          entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0])
          gotoxy(35,5);print(entEmpleado.nombre)
      else:
         gotoxy(27,5);print("No existe Empleado con ese codigo[{}]:".format(id))
         time.sleep(2);gotoxy(27,5);print(" "*40)
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(15,7);print("Horas50:")
   gotoxy(15,8);print("Horas100:")
   validar = Valida()
   aamm=validar.solo_numeros("","Dato no valido",23,6)
   #gotoxy(23,6);aamm = input()
   gotoxy(23,7);h50 = input()
   gotoxy(24,8);h100 = input()
   gotoxy(15,9);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,9);grabar = input().lower()
   if grabar == "s":
        archiSobretiempo = Archivo("./archivos/sobretiempo.txt","|")
        sobretiempos = archiSobretiempo.leer()
        if sobretiempos : idSig = int(sobretiempos[-1][0])+1
        else: idSig=1
        sobretiempo = Sobretiempo(entEmpleado,aamm,h50,h100,True,idSig)
        datos = sobretiempo.getSobretiempo()
        datos = '|'.join(datos)
        archiSobretiempo.escribir([datos],"a")
        gotoxy(10,10);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
        gotoxy(10, 15); print("****************SOBRETIEMPO INGRESADO AL SISTEMA*****************"); time.sleep(2)
        gotoxy(10, 15); print("****************REGRESANDO AL MENU SOBRETIEMPO*****************") ; time.sleep(2)
   else:
       gotoxy(10,10);input("Registro No fue Grabado\n presione una tecla para continuar...")
       gotoxy(10, 15); print("****************REGRESANDO AL MENU NOVEDAD*****************"); time.sleep(2)


def CrearPrestamos():
    borrarPantalla()
    validar = Valida()
    gotoxy(20,2); print("INGRESO DE VALOR DEL PRESTAMO")
    gotoxy(15,4); print("Obrero-Administrativo(O/A): ")
    opc = validar.solo_letras(" ","Error: Solo letras", 15,5).upper()
    if opc == "A":
            gotoxy(15,6);print("A D M I N I S T R A T I V O")
            gotoxy(15,7);print("Empleado ID[    ]: ")
            gotoxy(27,7);id = input().upper()
            archiEmp = Archivo("./archivos/administrativo.txt","|")
            empleado= archiEmp.buscar(id)
            entEmpleado = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0])
            gotoxy(35,6);print(entEmpleado.nombre)
    else:
            print("O B R E R O")
            gotoxy(15,6);print("Empleado ID[    ]: ")
            gotoxy(27,6);id = input().upper()
            archiEmp = Archivo("./archivos/obrero.txt","|")
            empleado= archiEmp.buscar(id)
            entEmpleado = Obrero(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],empleado[8],empleado[0])
            gotoxy(35,6);print(entEmpleado.nombre)

    gotoxy(15,7);print("Periodo[aaaamm]")
    gotoxy(15,8);print("Valor:")
    gotoxy(15,9);print("Número de Pago:")
    gotoxy(15,10);print("Saldo:")
    validar = Valida()
    aamm=validar.solo_numeros("","Error: Solo numeros",23,7)
    valor=validar.solo_decimales("","Error: Solo numeros",33,8)
    numP=validar.solo_decimales("","Error: Solo numeros",33,9)
    saldo=validar.solo_decimales("", "Error: Solo numeros",33,10)
    gotoxy(15,11);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(54,11);grabar = input().lower()
    if grabar == "s":
        archiPrestamo = Archivo("./archivos/prestamo.txt","|")
        prestamos = archiPrestamo.leer()
        if prestamos : idSig = int(prestamos[-1][0])+1
        else: idSig=1
        prestamos = Prestamo(entEmpleado,aamm,valor,numP, saldo,True,idSig)
        datos = prestamos.getPrestamo()
        datos = '|'.join(datos)
        archiPrestamo.escribir([datos],"a")
        gotoxy(10,13);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
        gotoxy(10, 14); print("****************PRESTAMO INGRESADO AL SISTEMA*****************"); time.sleep(2)
        gotoxy(10, 15); print("****************REGRESANDO AL MENU NOVEDAD*****************") ; time.sleep(2)
    else:
        gotoxy(10,13);input("Registro No fue Grabado\n presione una tecla para continuar...")
        gotoxy(10, 14); print("****************REGRESANDO AL MENU NOVEDAD*****************") ; time.sleep(2)

# opciones de Rol de Pago
def rolAdministrativo():
   borrarPantalla()
   # Se ingresa los datos del rol a procesar
   gotoxy(20,2);print("ROL ADMINISTRATIVO")
   aamm=0
   gotoxy(15,6);print("Periodo[aaaamm]")
   validar = Valida()
   aamm=validar.solo_numeros("","Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de Procesar el Rol(s/n):")
   gotoxy(54,7);grabar = input().lower()
   entEmpAdm = None
   # Se procesa el rol con la confirmacion del usuario
   if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/administrativo.txt","|")
        ListaEmpAdm = archiEmp.leer()
        if ListaEmpAdm :
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            print(empresa)
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2], empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt","|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]),float(deducciones[1]),float(deducciones[2]))
            #print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(),aamm)
            for empleado in ListaEmpAdm:
              #print(empleado)
              entEmpAdm = Administrativo(empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6],empleado[7],float(empleado[8]),empleado[0])
              #print(entEmpAdm.nombre,entEmpAdm.sueldo)
              nomina.calcularNominaDetalle(entEmpAdm,entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabAdm.txt","|")
            archiRol.escribir([datosCab],"a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetAdm.txt","|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado           
            for dt in datosDet:
                dt = nomina.aamm+'|'+'|'.join(dt)
                archiDet.escribir([dt],"a")
            # imprimir rol

            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,"O B R E R O S")
            nomina.mostrarDetalleNomina()

   else:
       gotoxy(10,10);input("Rol No fue Procesado\n presione una tecla para continuar...")

   input("               Presione una tecla continuar...")

def consultaRol():
   borrarPantalla()
   validar = Valida()
   # Se ingresa los datos del rol a Consultar
   gotoxy(20,2);print("CONSULTA DE ROL OBRERO - ADMINISTRATIVO")
   rol=0
   aamm=""
   gotoxy(15,4);print("Obrero-Administrativo(O/A): ")
   gotoxy(15,6);print("Periodo[aaaamm]")
   gotoxy(44,4)
   rol=input().upper()
   aamm=validar.solo_numeros("","Error: Solo numeros",23,6)
   gotoxy(15,7);print("Esta seguro de consultar el Rol(s/n):")
   gotoxy(54,7);procesar = input().lower()
   if procesar == "s":
        if rol == "A":
            tit = "A D M I N I S T R A T I V O"
            archiRolCab = Archivo("./archivos/rolCabAdm.txt","|")
            archiRolDet = Archivo("./archivos/rolDetAdm.txt","|")
        else:
            tit = "O B R E R O"
            archiRolCab = Archivo("./archivos/rolCabObre.txt","|")
            archiRolDet = Archivo("./archivos/rolDetObre.txt","|")
        cabrol = archiRolCab.buscar(aamm)
        if cabrol:
            entCabRol = Nomina(cabrol[1],cabrol[0])
            entCabRol.totIngresos=float(cabrol[2])
            entCabRol.totDescuentos=float(cabrol[3])
            entCabRol.totPagoNeto=float(cabrol[4])
            detalle= archiRolDet.buscarLista(aamm)
            for det in detalle:
                entCabRol.detalleNomina.append(det[1:])
            # print(entCabRol.getNomina())
            # print(entCabRol.getDetalle())
            # input()
            # imprimir rol    
            archiEmpresa = Archivo("./archivos/empresa.txt","|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0],empresa[1],empresa[2],empresa[3])
            entCabRol.mostrarCabeceraNomina(entEmpresa.razonSocial,entEmpresa.direccion,entEmpresa.telefono,entEmpresa.ruc,tit)
            entCabRol.mostrarDetalleNomina()
        else:
            gotoxy(10,10);input("No existe rol con ese periodo\n presione una tecla para continuar...")

   else:
       gotoxy(10,10);input("Consulta Cancelada\n presione una tecla para continuar...")
   input("               Presione una tecla continuar...")

def rolObrero():
    borrarPantalla()
    # Se ingresa los datos del rol a procesar
    gotoxy(20, 2);
    print("ROL OBRERO")
    aamm = 0
    gotoxy(15, 6);
    print("Periodo[aaaamm]")
    validar = Valida()
    aamm = validar.solo_numeros("","Error: Solo numeros", 23, 6)
    gotoxy(15, 7);
    print("Esta seguro de Procesar el Rol(s/n):")
    gotoxy(54, 7);
    grabar = input().lower()
    entEmpObr = None
    # Se procesa el rol con la confirmacion del usuario
    if grabar == "s":
        # Obtener lista de empleados a procesar el rol
        archiEmp = Archivo("./archivos/obrero.txt", "|")
        ListaEmpObr = archiEmp.leer()
        if ListaEmpObr:
            archiEmpresa = Archivo("./archivos/empresa.txt", "|")
            empresa = archiEmpresa.leer()[0]
            entEmpresa = Empresa(empresa[0], empresa[1], empresa[2], empresa[3])
            archiDeducciones = Archivo("./archivos/deducciones.txt", "|")
            deducciones = archiDeducciones.leer()[0]
            entDeduccion = Deduccion(float(deducciones[0]), float(deducciones[1]), float(deducciones[2]))
            # print(entDeduccion.getIess(),entDeduccion.getComision(),entDeduccion.getAntiguedad())
            nomina = Nomina(date.today(), aamm)
            for empleado in ListaEmpObr:
                # print(empleado)
                entEmpObr = Obrero(empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6],
                                   empleado[7], float(empleado[8]), empleado[0])
                nomina.calcularNominaDetalle(entEmpObr, entDeduccion)
            # grabar cabecera del rol
            datosCab = nomina.getNomina()
            datosCab = '|'.join(datosCab)
            archiRol = Archivo("./archivos/rolCabObre.txt", "|")
            archiRol.escribir([datosCab], "a")
            # grabar detalle del rol
            archiDet = Archivo("./archivos/rolDetObre.txt", "|")
            datosDet = nomina.getDetalle()
            # se graba en el detalle empleado por empleado
            for dt in datosDet:
                dt = nomina.aamm + '|' + '|'.join(dt)
                archiDet.escribir([dt], "a")
            # imprimir rol
            nomina.mostrarCabeceraNomina(entEmpresa.razonSocial, entEmpresa.direccion, entEmpresa.telefono,
                                         entEmpresa.ruc, "O B R E R O S")
            nomina.mostrarDetalleNomina()

    else:
        gotoxy(10, 10);
        input("Rol No fue Procesado\n presione una tecla para continuar...")

    input("               Presione una tecla continuar...")

def Mantenimiento_Empresa():
    valida = Valida()
    borrarPantalla()
    print("--------------------MANTENIMIENTO EMPRESA------------------")
    print(" ")
    gotoxy(10, 2); razonSocial = input("Ingrese la Razon Social: ")
    gotoxy(10, 3); direccion = input("Ingrese a direccion: ")
    telefono = valida.solo_numeros("Ingrese el numero de la empresa: ", "    INGRESE SOLO NUMEROS                  ",10, 4)
    ruc = valida.solo_numeros("Ingrese el RUC de la empresa: ", "    INGRESE SOLO NUMEROS                     ", 10,5)
    objEm = Empresa(razonSocial, direccion, telefono, ruc)
    aux = objEm.getEmpresa()
    archiEmp = Archivo("./archivos/empresa.txt", "|")
    while True:
        grabar = valida.solo_letras("Esta seguro de Grabar El registro(s/n):","Ingrese solo letra:",15,6)
        if grabar in ['s','n']: break
        else: pass
    if grabar == 's':
        archiEmp.escribirM([aux], "w")
        gotoxy(10,7); print("****************SE HA MODIFICADO INFORMACION DE LA EMPRESA EN EL SISTEMA*****************");time.sleep(5)
        gotoxy(10, 8); print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)
    else:
        gotoxy(10, 7); print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)

def parametro():
    borrarPantalla()
    validar = Valida()
    gotoxy(10,2);print("MANTENIMIENTO DE DEDUCCIONES")
    iess=validar.solo_decimales("Iess: ","Error: Solo numeros",10,4)
    comision=validar.solo_decimales("Comision: ","Error: Solo numeros",10,5)
    antiguedad=validar.solo_decimales("Antiguedad: ","Error: Solo numeros",10,6)
    gotoxy(10,7);print("Esta seguro de Grabar El registro(s/n):")
    gotoxy(10,8);grabar = input().lower()
    if grabar == "s":
       archiDeducciones = Archivo("./archivos/deducciones.txt","|")
       archiDeducciones.leer()
       dedu = Deduccion(iess,comision,antiguedad)
       datos= dedu.getDeduccion()
       datos = '|'.join(datos)
       archiDeducciones.escribir([datos],"w")
       gotoxy(10,9);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
       gotoxy(10, 11); print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)
    else:
       gotoxy(10,10); input("Registro No fue Grabado\n presione una tecla para continuar...")
       gotoxy(10, 12); print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)

def crearDepartamento():
    valida = Valida()
    gotoxy(10,6); print("-----------------------CREACION DE DEPARTAMENTO-------------------")
    archiDepartamentos = Archivo("./archivos/departamento.txt", "|")
    descripcion = valida.solo_letras("Ingrese la descripcion: ", "                   Ingrese solo letras",10,7)
    id = len(archiDepartamentos.leer()) + 1
    objDep = Departamento(descripcion, id)
    aux = [objDep.getid, objDep.descripcion]
    while True:
        grabar = valida.solo_letras("Esta seguro de Grabar El registro(s/n):","Ingrese solo letra:",15,15)
        if grabar in ['s','n']: break
        else: pass
    if grabar == "s":
        archiDepartamentos.escribirM([aux], "a")
        gotoxy(10, 16); print("****************DEPARTAMENTO INGRESADO AL SISTEMA*****************"); time.sleep(2)
        gotoxy(10, 17); print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)
    else:
        gotoxy(10, 16); print("****************REGRESANDO AL MENU MANTENIMIENTO*****************"); time.sleep(2)
