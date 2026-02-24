from Persona import Persona

class Cliente(Persona):
    def __init__(self, Codigo, Email, Nombre, Telefono, Credito):
        super().__init__(Codigo, Email, Nombre, Telefono)
        self.Credito = Credito

    def getCredito(self):
        return self.Credito

    def setCredito(self, Credito):
        self.Credito = Credito