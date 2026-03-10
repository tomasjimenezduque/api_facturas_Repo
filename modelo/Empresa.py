from Cliente import Cliente

class Empresa(Cliente):
    def __init__(self, Codigo_Pers, Email, Nombre_Pers, Telefono, Credito, Codigo, Nombre):
        # Se pasa la info al constructor de Cliente
        super().__init__(Codigo_Pers, Email, Nombre_Pers, Telefono, Credito)
        self.Codigo = Codigo
        self.Nombre = Nombre

    def getCodigo(self):
        return self.Codigo
    
    def setCodigo(self, Codigo):
        self.Codigo = Codigo

    def getNombre(self):
        return self.Nombre

    def setNombre(self, Nombre):
        self.Nombre = Nombre