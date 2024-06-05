class MovimientoStock:
    def __init__(self, id: int = None, producto_id: int = None, cantidad: int = None, tipo: str=None, fecha: str=None): # type: ignore
        self.id = id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.tipo = tipo
        self.fecha = fecha
    
    PROPERTIES = ['id', 'producto_id', 'cantidad', 'tipo', 'fecha']