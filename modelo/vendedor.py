from Persona import Persona

class Vendedor(Persona):
    def __init__(self, Codigo, Email, Nombre, Telefono, Carnet, Direcion):
        super().__init__(Codigo, Email, Nombre, Telefono)
        self.Carnet = Carnet
        self.Direcion = Direcion

    def getCarnet(self):
        return self.Carnet

    def setCarnet(self, Carnet):
        self.Carnet = Carnet

    def getDirecion(self):
        return self.Direcion

    def setDirecion(self, Direcion):
        self.Direcion = Direcion