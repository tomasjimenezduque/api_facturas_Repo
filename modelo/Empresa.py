class Empresa(Cliente):
    def __init__(self, Codigo, Nombre):
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