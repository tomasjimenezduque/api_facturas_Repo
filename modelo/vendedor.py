from api_facturas.modelo import Persona
class Vendedor(Persona):
    def __init__(self, Carnet, Direcion):
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