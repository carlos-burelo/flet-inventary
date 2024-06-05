from src.elements import *
from flet import icons
from src.layout.page import page
from src.db.db import db
from src.models.movimiento import MovimientoStock
from src.pages.components.new_io import NewMovimientoStockForm
from src.pages.components.navbar import Navbar
import _

@page(route="/movimientos-stock")
def MovimientosStockPage():
    data = db.movimiento_stock.obtener_todos_los_movimientos()
    row_names = MovimientoStock.PROPERTIES

    def new(e):
        def handle_save(new_movimiento: MovimientoStock):
            new_form.open = False
            db.movimiento_stock.añadir_movimiento(new_movimiento)
            db.productos.actualizar_stock(new_movimiento.producto_id, new_movimiento.cantidad, new_movimiento.tipo)
            datasource = create_datasource(db.movimiento_stock.obtener_todos_los_movimientos(), row_names)
            _table.rows = datasource[1]
            _.root.update()
        new_form = NewMovimientoStockForm(handle_save)

    _table = table(data=data, row_names=row_names)

    return [
        Navbar(),
        img(src="src/assets/logo.png", w=300, h=100),
        row([
            button("Nuevo movimiento de stock", icon=icons.ADD, on_click=new),
        ]),
        column([_table], w=1400, h=400)
    ]
