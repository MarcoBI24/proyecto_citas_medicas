import os
import sys
import csv
# import keyboard

class Usuario:
    def __init__(self, nombre, apellido, dni,contraseña, correo, numero, fecha_nacimiento, pais, departamento, provincia, distrito, direccion ):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.contraseña = contraseña
        self.correo = correo
        self.numero = numero
        self.fecha_nacimiento = fecha_nacimiento
        self.pais = pais
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.direccion = direccion
        self.sesion_iniciada = False
        self.citas = []
class Sistema():
    
    def __init__(self):
        self.cuentas = []
        self.ARCHIVO_CSV = 'cuentas.csv'
    def __iter__(self):
        return iter(self.lista)

    def crear_cuenta(self):
        nombre = input("Nombre : ") 
        apellido = input("Apellido : ") 
        dni = input("DNI : ")
        contraseña = input("Contraseña : ") 
        correo = input("Correo : ") 
        numero = input("Numero : ") 
        fecha_nacimiento = input("Fecha de nacimiento : ") 
        pais = input("Pais : ") 
        departamento = input("Departamento : ") 
        provincia = input("Provincia : ") 
        distrito = input("Distrito : ") 
        direccion = input("Direccion : ")
        nuevo_usuario = Usuario(nombre, apellido, dni,contraseña, correo, numero, fecha_nacimiento, pais, departamento, provincia, distrito, direccion)
        self.cuentas.append(nuevo_usuario)
        # Usuario("marco","berna","1234","1234","dedefe","denbfeh","denbfeh","denbfeh","denbfeh","denbfeh","denbfeh","denbfeh")
    def guardar_en_csv(self, nombre_archivo, datos):
        with open(nombre_archivo, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames="ignore")
            writer.writerows(datos)
    def cargar_desde_csv(self,nombre_archivo):
        try:
            with open(nombre_archivo, mode='r',encoding="utf8") as file:
                reader = csv.reader(file)
                for fila in reader:
                    self.cuentas.append(fila)
                # return array
        except FileNotFoundError:
            return []
    def iniciar_sesion(self, dni, contraseña):
        for cuenta in self.cuentas:
            if cuenta.dni == dni and cuenta.contraseña ==  contraseña:
                cuenta.sesion_iniciada = True
                return cuenta
        return None       
    def ver_us (self):
        print(self.cuentas[0].nombre) 
    def cerrar_sesion(self):
        for cuenta in self.cuentas:
            if cuenta.sesion_iniciada == True:
                cuenta.sesion_iniciada = False
                
                return {}
            print("NO SE PUDO CERRAR SESION..")
    def programar_cita(self,especialidad,medico,modalidad,fecha,hora,notas_adicionales):    
        for cuenta in self.cuentas:
            if cuenta.sesion_iniciada == True:
                cita = [
                    ["nombre", cuenta.nombre],
                    ["numero", cuenta.numero],
                    ["correo", cuenta.correo],
                    ["especialidad", especialidad],
                    ["medico", medico],
                    ["modalidad", modalidad],
                    ["fecha", fecha],
                    ["hora", hora],
                    ["notas adicionales", notas_adicionales]
                ]
                cuenta.citas.append(cita)
                
    # def ver_citas(self):
    
            
    def borrar_parte_linea(self,):
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[K')
        
        sys.stdout.flush()
        
    # Monitorear eventos de teclado

    # def mi_cuenta(self):
    #     # for cuenta in self.cuentas:
    #     #     if cuenta.sesion_iniciada == True:
                
sistema = Sistema()
usuario = {}
dato = Usuario("marco","berna","1234","1234","dedefe","denbfeh","denbfeh","denbfeh","denbfeh","denbfeh","denbfeh","denbfeh")
print(dato)
sistema.guardar_en_csv(sistema.ARCHIVO_CSV, dato)
def espacios(cadena, ancho, separacion, centrar):
    if centrar:
        espacio_adicional = (ancho - len(cadena)) // 2
        izquierda = espacio_adicional
        derecha = ancho - len(cadena) - izquierda
        return separacion * izquierda + cadena + separacion * derecha
    else:
        return " " + cadena + separacion * (ancho - len(cadena))

def mostrar_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    print("╭" + "─" * (23 * columnas + 1) + "╮")
    
    for i in range(filas):
        elemento_1 = espacios(matriz[i][0], 15, " ", True)
        elemento_2 = espacios(matriz[i][1], 30, " ", False)
        print("│" + elemento_1 + "│" + elemento_2 + "│")
        
        if i < filas - 1:
            print("├" + "─" * (23 * columnas + 1) + "┤")

    print("╰" + "─" * (23 * columnas + 1) + "╯")


while True:
    # MOSTRAR PANTALLA DE INICIO
    titulo = """ 
█▀▀ █ ▀█▀ ▄▀█ █▀   █▀▄▀█ █▀▀ █▀▄ █ █▀▀ ▄▀█ █▀
█▄▄ █ ░█░ █▀█ ▄█   █░▀░█ ██▄ █▄▀ █ █▄▄ █▀█ ▄█

    """
    print(titulo)
    if usuario == {}:        
        print("""
[1] Iniciar sesion
[2] Registrarte
[0] Salir
""")
        opcion = input(" > ")
        
        if opcion == "1":
            while True:
                os.system("cls")
                print("          INICIAR SESION        \n")
                dni = input("DNI : ")
                contraseña = input("Contraseña : ")
                usuario = sistema.iniciar_sesion(dni, contraseña)
                os.system("cls")
                if usuario != None:
                    print("Iniciando sesion...")
                    break
                else:
                    print("Nombre de usuario o contraseña incorrectos...")
        elif opcion == "2":
           
            os.system("cls")
            print(titulo)
            sistema.crear_cuenta()
            os.system("cls")
            print(f"¡Felicidades ya  tienes una cuenta!")
            print("Retornando...")
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            os.system("cls") #limpiar pantalla
            print("Opcion invalida")
    else:
        print(f"Bienvenido {usuario.nombre}...")
        
        print(""" 
              
[1] Programar cita
[2] Ver citas 
[3] Mi cuenta
[0] Cerrar sesión

        """)
        
        opcion = input(" > ")
        if opcion == "1":
            os.system("cls")
            print(f"""

                PROGRAMAR CITA
                
Nombre : {usuario.nombre}
Numero {usuario.numero}
Correo : {usuario.correo}""")
            especialidad = input("Especialidad : ")
            medico = input("Nombre del medico : ")
            modalidad = input("Modalidad : ")
            fecha = input("Fecha : ")
            hora = input("Hora : ")
            notas_adicionales = input("Notas adicionales : ")
            
            sistema.programar_cita(especialidad,medico,modalidad,fecha,hora,notas_adicionales)
            os.system("cls")
            print(f"Cita programada para el dia {fecha}")

        elif opcion == "2":
            os.system("cls")
            # sistema.ver_citas()
            if len(usuario.citas) == 0:
                
                print("Tiene 0 citas. Reserve una porfavor")
            else:
                # print(usuario.citas)
                
                print("=" * 50)
                print(" "*22 + "CITAS" + " "*22 )
                for cita in usuario.citas:
                    mostrar_matriz(cita)
                    print("\n\n")
                print("=" * 70)
                
                # for citas in usuario.citas:    
                     
                
        elif opcion == "3":
            os.system("cls")
            panel = f"""
                     MI CUENTA
            
Nombre : {usuario.nombre}
Apellido : {usuario.apellido} 
DNI : {usuario.dni}
Contraseña : {"*"*len(usuario.contraseña)} 
Numero : {usuario.numero} 
Fecha nacimiento : {usuario.fecha_nacimiento} 
Pais : {usuario.pais} 
Provincia : {usuario.provincia} 
Distrito : {usuario.distrito}
Direccion : {usuario.direccion}
                            
                            """
            print(panel)
            opc = input("¿Desea modificar algun dato? Si/No > ")
            
            if opc.lower() == "si" :
                print("\n Dejar en blanco para mantener el valor actual \n")
                usuario.nombre = input("nombre > ") or usuario.nombre
                usuario.apellido = input("apellido > ") or usuario.apellido
                usuario.dni = input("dni > ") or usuario.dni
                usuario.contraseña = input("contraseña > ") or usuario.contraseña
                usuario.numero = input("numero > ") or usuario.numero
                usuario.fecha_nacimiento = input("fecha de nacimiento > ") or usuario.fecha_nacimiento
                usuario.pais = input("pais > ") or usuario.pais
                usuario.provincia = input("provincia > ") or usuario.provincia
                usuario.distrito = input("distrito > ") or usuario.distrito
                usuario.direccion = input("direccion > ") or usuario.direccion
                print("¡Datos Actualizados!")
            elif opc.lower() == "no":
                os.system("cls")
                pass

        elif opcion == "0":
           usuario = sistema.cerrar_sesion()
           if usuario == {}:
                os.system("cls")
                print("Cerrando sesion...") 
           else: 
               print("Hubo un error al cerrar sesion")
            
            
# HACER EL VOUCHER
# agregar el strip() al actualizar los datos
# agregar <(flecha izq) > (flecha der) pulsaciones de teclado para mostrar las citas
# poner codigo a cada cita 
