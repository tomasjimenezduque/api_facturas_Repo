from typing import List
from ProductosPorFactura import ProductosPorFactura

class Factura():
    def __init__(self, Fecha, Numero, Total):
        self.Fecha = Fecha
        self.Numero = Numero
        self.Total = Total
        self.productos: List[ProductosPorFactura] = []

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

    def agregar_producto(self, producto_factura: ProductosPorFactura) -> None:
        self.productos.append(producto_factura)