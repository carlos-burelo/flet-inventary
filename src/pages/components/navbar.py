from src.elements import nav, a, icons

def Navbar():
    return nav(
            a(href="/", icon=icons.LOGOUT_ROUNDED, tooltip="Cerrar Sesión"),
            a(href="/productos", icon=icons.SHOPPING_BAG, tooltip="Productos"),
            a(href="/proveedores", icon=icons.LOCAL_SHIPPING, tooltip="Proveedores"),
            a(href="/movimientos-stock", icon=icons.STORAGE, tooltip="Movimientos de Stock"),
        )