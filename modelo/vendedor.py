class Vendedor(Persona):
    def __init__(self, carnet, direcion):
        self.carnet = carnet
        self.direcion = direcion

    def getCarnet(self):
        return self.carnet

    def setCarnet(self, carnet):
        self.carnet = carnet

    def getDirecion(self):
        return self.direcion

    def setDirecion(self, direcion):
        self.direcion = direcion