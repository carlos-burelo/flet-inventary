from src.elements import dialog, column, button, colors, h3
from src.models import Producto

def DeleteProductForm(item: Producto, delete_callback):
    def handle_delete(e):
        delete_callback(item)

    return dialog(
        title="Eliminar producto",
        content=column([
            h3(f"¿Estás seguro de eliminar el producto {item.nombre}?")
        ], w=300, h=100),
        action=button("Eliminar", color=colors.RED_800, on_click=handle_delete)
    )