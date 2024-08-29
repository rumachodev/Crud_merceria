class Carrito:
    def __init__(self):
        self.productos = []
        self.total = 0.0

    def vaciar_carrito(self):
        self.productos = []
        self.total = 0.0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto['precio']

    def obtener_total(self):
        return self.total
