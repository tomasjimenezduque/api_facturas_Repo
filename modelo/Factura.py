class Factura():
    def __init__(self,Fecha,Numero,Total):
        self.Fecha = Fecha
        self.Numero = Numero
        self.Total = Total
        self.ProductosPorFactura = []

    def getFecha(self): 
        return self.Fecha

    def setFecha(self, Fecha):
        self.Fecha = Fecha

    def getNumero(self):
        return self.Numero

    def setNumero(self, Numero):
        self.Numero = Numero

    def getTotal(self):
        return self.Total

    def setTotal(self, Total):
        self.Total = Total