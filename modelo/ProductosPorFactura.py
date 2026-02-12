class ProductosPorFactura():
    def __init__(self,Cantidad,Subtotal):
        self.Cantidad = Cantidad
        self.Subtotal = Subtotal

    def getCantidad(self):
        return self.Cantidad

    def setCantidad(self, Cantidad):
        self.Cantidad = Cantidad

    def getSubtotal(self):
        return self.Subtotal    
    
    def setSubtotal(self, Subtotal):
        self.Subtotal = Subtotal