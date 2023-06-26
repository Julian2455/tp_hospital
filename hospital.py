def contar_camas():
    datos=open("habitaciones.csv","r")
    total=0
    for x in datos.readlines():
        if "LIBRE" in x:
            total+=1
    datos.close()
    return total

def contar_pacientes():
    datos=open("habitaciones.csv","r")
    total=0
    for x in datos.readlines():
        lista=x.split(";")
        if len(lista)>2:
            total+=1
    datos.close()
    return total

def validar_dni(dni):
    datos=open("habitaciones.csv","r")
    c=0
    for x in datos.readlines():
        linea=x.split(";")
        if len(linea)>2:
            original=linea[3]
            if original==dni:
                c+=1
    datos.close()
    if c==0:
        return True
    else:
        return False

def cargar_paciente(nom,apell,dni):
    datos=open("habitaciones.csv","r")
    lista=[]
    c=0
    for x in datos.readlines():
        control=x.split(";")
        num=control[0]
        num=int(num)
        if num<10:
            if c==0:
                if "LIBRE" in x:
                    separado=x.splitlines()
                    cadena=separado[0]
                    cadena=cadena[:1]+";"+nom+";"+apell+";"+dni+"\n"
                    lista.append(cadena)
                    c=1
                else:
                    separado=x.splitlines()
                    cadena=separado[0]+"\n"
                    lista.append(cadena)
            else:
                separado=x.splitlines()
                cadena=separado[0]+"\n"
                lista.append(cadena)
        else:
            if c==0:
                if "LIBRE" in x:
                    separado=x.splitlines()
                    cadena=separado[0]
                    cadena=cadena[:2]+";"+nom+";"+apell+";"+dni+"\n"
                    lista.append(cadena)
                    c=1
                else:
                    separado=x.splitlines()
                    cadena=separado[0]+"\n"
                    lista.append(cadena)
            else:
                separado=x.splitlines()
                cadena=separado[0]+"\n"
                lista.append(cadena)
        datos.close()
    datos=open("habitaciones.csv","w")
    for x in lista:
        datos.write(x)
    datos.close()

def alta_paciente(dni):
    dni=str(dni)
    datos=open("habitaciones.csv","r")
    lista=[]
    c=0
    for x in datos.readlines():
        control=x.split(";")
        num=control[0]
        num=int(num)
        if num<10:
            if c==0:
                if dni in x:
                    mostrar=x.split(";")
                    print(f'El paciente {mostrar[2]}, {mostrar[1]} fue dado de alta con exito')
                    print(f'La habitacion N°{mostrar[0]}, ahora se encuentra disponible')
                    separado=x.splitlines()
                    cadena=separado[0]
                    cadena=cadena[:1]+";LIBRE"+"\n"
                    lista.append(cadena)
                    c=1
                else:
                    separado=x.splitlines()
                    cadena=separado[0]+"\n"
                    lista.append(cadena)
            else:
                separado=x.splitlines()
                cadena=separado[0]+"\n"
                lista.append(cadena)
        else:
            if c==0:
                if dni in x:
                    mostrar=x.split(";")
                    print(f'El paciente {mostrar[2]}, {mostrar[1]} fue dado de alta con exito')
                    print(f'La habitacion N°{mostrar[0]}, ahora se encuentra disponible')
                    separado=x.splitlines()
                    cadena=separado[0]
                    cadena=cadena[:2]+";LIBRE"+"\n"
                    lista.append(cadena)
                    c=1
                else:
                    separado=x.splitlines()
                    cadena=separado[0]+"\n"
                    lista.append(cadena)
            else:
                separado=x.splitlines()
                cadena=separado[0]+"\n"
                lista.append(cadena)
    if c==0:
        print("EL DNI: {dni} no se encuentra en la lista")
    datos=open("habitaciones.csv","w")
    for x in lista:
        datos.write(x)
    datos.close()

def disponibles():
    datos=open("habitaciones.csv","r")
    for x in datos.readlines():
        if "LIBRE" in x:
            linea=x.split(";")
            print(f'Habitacion {linea[0]} DISPONIBLE')
        else:
            linea=x.split(";")
            print(f'Habitacion {linea[0]} ----------')
    datos.close()

def ocupadas():
    datos=open("habitaciones.csv","r")
    for x in datos.readlines():
        if "LIBRE" not in x:
            linea=x.split(";")
            linea[3]=linea[3][:-1]
            print(f'{linea[2]}, {linea[1]}, DNI: {linea[3]}, Habitacion: {linea[0]}')
    datos.close()

def restaurar():
    datos=open("habitaciones.csv","w")
    for x in range(20):
        datos.write(f'{x+1};LIBRE\n')
    datos.close()

while True:
    print("1 <--Mostrar habitaciones disponibles")
    print("2 <--Mostrar pacientes")
    print("3 <--Ingresar paciente")
    print("4 <--Dar de alta a un paciente")
    print("5 <--Dar de alta a TODOS LOS PACIENETES")
    print("6 <--Salir")
    opc=int(input("\nIngrese la opcion: "))
    if opc==1:
        disponibles()
        print("\n")
    elif opc==2:
        if contar_pacientes()==0:
            print("No hay pacientes ingresados")
        else:
            ocupadas()
        print("\n")
    elif opc==3:
        if contar_camas()!=0:
            nombre=input("Nombre del paciente: ")
            apellido=input("Apellido del paciente: ")
            dni=int(input("DNI del paciente: "))
            dni=str(dni)
            if validar_dni(dni)==True:
                cargar_paciente(nombre,apellido,dni)
            else:
                print(f'ERROR, el DNI: {dni} ya se encuentra registrado')
            print("\n")
        else:
            print(f'NO ES POSIBLE INGRESAR AL PACIENTE, NO HAY HABITACIONES DISPONIBLES\n')
    elif opc==4:
        dni=int(input("DNI del paciente: "))
        dni=str(dni)
        alta_paciente(dni)
        print("\n")
    elif opc==5:
        while True:
            print("Se daran de alta a todos los pacientes, esta seguro?")
            print("1 <--CONFIRMAR")
            print("2 <--CANCELAR")
            confirmar=int(input("Ingrese la opcion: "))
            print("\n")
            if confirmar==1:
                restaurar()
                print("TODOS LOS PACIENETES HAN SIDO DADOS DE ALTA")
                break
            elif confirmar==2:
                break
            else:
                print("OPCION NO VALIDA\n")
    elif opc==6:
        break
    else:
        print("OPCION NO VALIDA\n")