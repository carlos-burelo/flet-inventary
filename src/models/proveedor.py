class Proveedor:
    def __init__(self, id: int = None, nombre: str = None, direccion: str = None, telefono: str = None): #type: ignore
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    PROPERTIES = ['id', 'nombre', 'direccion', 'telefono']