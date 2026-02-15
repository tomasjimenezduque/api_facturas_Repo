class Producto():
    def __init__(self, Codigo, Nombre, Stock, Valorunitario):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.Stock = Stock
        self.Valorunitario = Valorunitario

    def getCodigo(self):
        return self.Codigo

    def setCodigo(self, Codigo):
        self.Codigo = Codigo

    def getNombre(self):
        return self.Nombre

    def setNombre(self, Nombre):
        self.Nombre = Nombre

    def getStock(self):
        return self.Stock

    def setStock(self, Stock):
        self.Stock = Stock

    def getValorunitario(self):
        return self.Valorunitario

    def setValorunitario(self, Valorunitario):
        self.Valorunitario = Valorunitario