class Persona():
    def __init__(self, Codigo, Email, Nombre, Telefono):
        self.Codigo = Codigo
        self.Email = Email
        self.Nombre = Nombre
        self.Telefono = Telefono
        self.Facturas = []

    def getCodigo(self):
        return self.Codigo

    def setCodigo(self, Codigo):
        self.Codigo = Codigo

    def getEmail(self):
        return self.Email

    def setEmail(self, Email):
        self.Email = Email
        
    def getNombre(self):
        return self.Nombre

    def setNombre(self, Nombre):
        self.Nombre = Nombre

    def getTelefono(self):
        return self.Telefono

    def setTelefono(self, Telefono):
        self.Telefono = Telefono
