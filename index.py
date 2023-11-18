            
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

    def crear_cuenta(self, nombre, apellido, dni,contraseña, correo, numero, fecha_nacimiento, pais, departamento, provincia, distrito, direccion):
        nuevo_usuario = Usuario(nombre, apellido, dni,contraseña, correo, numero, fecha_nacimiento, pais, departamento, provincia, distrito, direccion)
        self.cuentas.append(nuevo_usuario)

    def iniciar_sesion(self, dni, contraseña):
        for cuenta in self.cuentas:
            if cuenta.dni == dni and cuenta.contraseña ==  contraseña:
                cuenta.sesion_iniciada = True
                print("Sesion iniciada...")
                return cuenta
        print("Nombre de usuario o contraseña incorrectos...")
        return None       
        
    def cerrar_sesion(self, dni):
        for cuenta in self.cuentas:
            if cuenta.sesion_iniciada == True and cuenta.dni == dni:
                cuenta.sesion_iniciada = False
                print("Sesion cerrada...") 
                
                return
            print("NO SE PUDO CERRAR SESION..")
    def programar_cita(self,nombre , numero , correo , especialidad , medico , tipo_cita , fecha , hora , notas_adicionales):
        for cuenta in self.cuentas:
            if cuenta.sesion_iniciada == True:
                cita = {
                    "nombre" : nombre,
                    "numero" : numero,
                    "correo" : correo,
                    "especialidad" : especialidad,
                    "medico" : medico,
                    "tipo_cita" : tipo_cita,
                    "fecha" : fecha,
                    "hora" : hora,
                    "notas_adicionales" : notas_adicionales
                }
                cuenta.citas.append(cita)
                print(f"Cita programada para el dia {fecha}")
        
#mostrar el menu
#eligir opcion entre iniciar sesion o registrarse
# si es iniciar sesion que le pida su dni y su contraseña
# luego mostrarle su cuenta y las opciones
# si es registrase que le pida todos los datos
#luego digirle a la pantalla de inicio
sistema = Sistema()
usuario = {}
while True:
    # MOSTRAR PANTALLA DE INICIO
    titulo = """
 
█▀▀ █ ▀█▀ ▄▀█ █▀   █▀▄▀█ █▀▀ █▀▄ █ █▀▀ ▄▀█ █▀
█▄▄ █ ░█░ █▀█ ▄█   █░▀░█ ██▄ █▄▀ █ █▄▄ █▀█ ▄█
    """
    print(titulo)
    if usuario == {}:        
        print("[1] Iniciar sesion")
        print("[2] Registrarte")    
        opcion = input()
        
        if opcion == "1":
            while True:
                dni = input("DNI : ")
                contraseña = input("Contraseña : ")
                usuario = sistema.iniciar_sesion(dni,contraseña)
                if usuario != None:
                    break
            print(f"Bienvenido {usuario.nombre}")
        elif opcion == "2":
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
            sistema.crear_cuenta(nombre, apellido, dni,contraseña, correo, numero, fecha_nacimiento, pais, departamento, provincia, distrito, direccion)
            print(f"¡Felicidades {nombre} ya  tienes una cuenta!")
            print("Retornando...")
    else:
        print(f"Hola {usuario.nombre}...")
        print("[1] Programar cita ")
        print("[2] Ver citas")
        opcion = input()
        if opcion == "1":
            print(f"Nombre : {usuario.nombre}")
            print(f"Numero {usuario.numero}")
            print(f"Correo : {usuario.correo}")
            especialidad = input("Especialidad : ")
            medico = input("Nombre del medico : ")
            tipo_cita = input("Tipo de cita : ")
            fecha = input("Fecha : ")
            hora = input("Hora : ")
            notas_adicionales = input("Notas adicionales : ")
            sistema.programar_cita(nombre, numero, correo, especialidad, medico, tipo_cita, fecha, hora, notas_adicionales)
        elif opcion == "2":
            for cita in usuario.citas:
                print(cita)
            
            print("-____________________-")
            
