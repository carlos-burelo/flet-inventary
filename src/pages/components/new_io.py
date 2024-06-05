from src.elements import dialog, column, input, button, colors, input_radio,RadioOption
from src.models.movimiento import MovimientoStock
from datetime import datetime

def NewMovimientoStockForm(add_callback, h=350, w=300):

    entrada_salida = [
        RadioOption("Entrada", "entrada"),
        RadioOption("Salida", "salida")
    ]

    _producto_id = input(label="ID del Producto")
    _tipo = input_radio(options=entrada_salida, default=entrada_salida[0])
    _cantidad = input(label="Cantidad")

    def handle_save(e):
        new_movimiento = MovimientoStock(
            producto_id=int(str(_producto_id.value)),
            tipo=str(_tipo.value),
            cantidad=int(str(_cantidad.value)),
            fecha=str(datetime.now())
        )
        add_callback(new_movimiento)

    return dialog(
        title="Nuevo movimiento de stock",
        content=column([_producto_id, _tipo, _cantidad], w=w, h=h),
        action=button("Guardar", color=colors.BLUE_800, on_click=handle_save)
    )
