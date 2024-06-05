from src.models.proveedor import Proveedor
from src.elements import dialog, column, button, colors, h3

def DeleteProviderForm(item: Proveedor, delete_callback):
    def handle_delete(e):
        delete_callback(item)

    return dialog(
        title="Eliminar proveedor",
        content=column([
            h3(f"¿Estás seguro de elimnar al proveedor: {item.nombre}?")
        ], w=300, h=100),
        action=button("Eliminar", color=colors.RED_800, on_click=handle_delete)
    )