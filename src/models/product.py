class Producto:
    def __init__(self, id: int = None, nombre: str = None, descripcion: str = None, categoria: str = None, precio: float = None, stock: int = None): # type: ignore
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    PROPERTIES = ['id', 'nombre', 'descripcion', 'categoria', 'precio', 'stock']