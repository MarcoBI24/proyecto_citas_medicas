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
        
        
        
class Sistema():
    
    """Clase del sistema principal""" 
    
    
    def __init__(self):
        self.cuentas = []
    
    
    def crear_cuenta(self, nombre, apellido, dni,contraseña, correo, numero, fecha_nacimiento, pais, departamento, provincia, distrito, direccion):
        nuevo_usuario = Usuario(nombre, apellido, dni,contraseña, correo, numero, fecha_nacimiento, pais, departamento, provincia, distrito, direccion)
        self.cuentas.append(nuevo_usuario)
        print(f"Cuenta creada para {nombre}")
        
        
    def iniciar_sesion(self, dni, contraseña):
        for cuenta in self.cuentas:
            if cuenta.dni == dni and cuenta.contraseña ==  contraseña:
                cuenta.sesion_iniciada = True
                print("Sesion iniciada...")
            print("Nombre de usuario o contraseña incorrectos...")
        
    def cerrar_sesion(self, dni):
        for cuenta in self.cuentas:
            if cuenta.sesion_iniciada == True and cuenta.dni == dni:
                cuenta.sesion_iniciada = False
                print("Sesion cerrada...") 
                return
            print("NO SE PUDO CERRAR SESION..")
    

