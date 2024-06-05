from ast import If
from src.models.movimiento import MovimientoStock
from src.models.product import Producto
from src.models.proveedor import Proveedor
from src.models.usuario import Usuario
from src.db.sqlite import Database


GET_ALL_PRODUCTS = "SELECT * FROM producto"
INSERT_PRODUCT = "INSERT INTO producto (nombre, precio, descripcion, stock, categoria) VALUES (?, ?,?, ?, ?)"
UPDATE_PRODUCT = "UPDATE producto SET nombre = ?, precio = ?, descripcion = ?, stock = ?, categoria = ? WHERE id = ?"
DELETE_PRODUCT = "DELETE FROM producto WHERE id = ?"
INCREMENT_PRODUCT_STOCK = "UPDATE producto SET stock = stock + ? WHERE id = ?"
DECREMENT_PRODUCT_STOCK = "UPDATE producto SET stock = stock - ? WHERE id = ?"


GET_ALL_PROVIDERS = "SELECT * FROM proveedor"
INSERT_PROVIDER = "INSERT INTO proveedor (nombre, direccion, telefono) VALUES (?, ?, ?)"
UPDATE_PROVIDER = "UPDATE proveedor SET nombre = ?, direccion = ?, telefono = ? WHERE id = ?"
DELETE_PROVIDER = "DELETE FROM proveedor WHERE id = ?"


GET_ALL_STOCK_MOVEMENTS = "SELECT * FROM movimiento_stock"
INSERT_STOCK_MOVEMENT = "INSERT INTO movimiento_stock (producto_id, cantidad, tipo) VALUES (?, ?, ?)"
UPDATE_STOCK_MOVEMENT = "UPDATE movimiento_stock SET producto_id = ?, cantidad = ?, tipo = ? WHERE id = ?"
DELETE_STOCK_MOVEMENT = "DELETE FROM movimiento_stock WHERE id = ?"


GET_ALL_USERS = "SELECT * FROM usuario"
GET_USER_BY_EMAIL = "SELECT * FROM usuario WHERE email = ?"
INSERT_USER = "INSERT INTO usuario (nombre, email, password) VALUES (?, ?, ?)"
UPDATE_USER = "UPDATE usuario SET nombre = ?, email = ?, password = ? WHERE id = ?"
DELETE_USER = "DELETE FROM usuario WHERE id = ?"



class TablaProductos:
    def __init__(self):
        self.db = Database()

    def obtener_todos_los_productos(self) -> list[Producto]:
        rows = self.db.execute_query(GET_ALL_PRODUCTS, fetchall=True)
        if rows is None:
            return []
        return [Producto(*row) for row in rows]
    
    def añadir_producto(self, p: Producto):
        self.db.execute_query(INSERT_PRODUCT, (p.nombre, p.precio, p.descripcion, p.stock, p.categoria))

    def actualizar_producto(self, p: Producto):
        self.db.execute_query(UPDATE_PRODUCT, (p.nombre, p.precio,p.descripcion, p.stock, p.categoria,  p.id))

    def eliminar_producto(self, id: int):
        self.db.execute_query(DELETE_PRODUCT, (id,))
    
    def actualizar_stock(self, producto_id: int, cantidad: int, tipo: str):
        if tipo == "entrada":
            self.db.execute_query(INCREMENT_PRODUCT_STOCK, (cantidad, producto_id))
        elif tipo == "salida":
            self.db.execute_query(DECREMENT_PRODUCT_STOCK, (cantidad, producto_id))



class TablaProveedotes:
    def __init__(self):
        self.db = Database()
    
    def obtener_todos_los_proveedores(self):
        rows = self.db.execute_query(GET_ALL_PROVIDERS, fetchall=True)
        return [Proveedor(*row) for row in rows]
    
    def añadir_proveedor(self, p: Proveedor):
        self.db.execute_query(INSERT_PROVIDER, (p.nombre, p.direccion, p.telefono))

    def actualizar_proveedor(self, p: Proveedor):
        self.db.execute_query(UPDATE_PROVIDER, (p.nombre, p.direccion, p.telefono, p.id))
    
    def eliminar_proveedor(self, id: int):
        self.db.execute_query(DELETE_PROVIDER, (id,))


class TablaMovimientosStock:
    def __init__(self):
        self.db = Database()

    def obtener_todos_los_movimientos(self):
        rows=self.db.execute_query(GET_ALL_STOCK_MOVEMENTS, fetchall=True)
        return [MovimientoStock(*row) for row in rows]

    def añadir_movimiento(self, m: MovimientoStock):
        self.db.execute_query(INSERT_STOCK_MOVEMENT, (m.producto_id, m.cantidad, m.tipo))


class TablaUsuarios:
    def __init__(self):
        self.db = Database()

    def obtener_todos_los_usuarios(self):
        rows = self.db.execute_query(GET_ALL_USERS, fetchall=True)
        return [Usuario(*row) for row in rows]
    
    def añadir_usuario(self, u: Usuario):
        self.db.execute_query(INSERT_USER, (u.nombre, u.email, u.password))

    def actualizar_usuario(self, u: Usuario):
        self.db.execute_query(UPDATE_USER, (u.nombre, u.email, u.password, u.id))

    def eliminar_usuario(self, id: int):
        self.db.execute_query(DELETE_USER, (id,))

    def obtener_usuario_por_email(self, email: str):
        row = self.db.execute_query(GET_USER_BY_EMAIL, (email,))
        return Usuario(*row) if row else None

class db:
    productos = TablaProductos()
    proveedores = TablaProveedotes()
    movimiento_stock = TablaMovimientosStock()
    usuarios = TablaUsuarios()