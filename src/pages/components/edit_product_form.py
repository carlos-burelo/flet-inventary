from src.elements import dialog, column, input, button, colors
from src.models import Producto
from src.utils.filters import NumbersOnlyInputFilter, DecimalInputFilter


def EditProductForm(item: Producto, edit_callback, w=300, h=350):
    _id = input(label="ID", visible=False, value=str(item.id))
    _name = input(label="Nombre", value=item.nombre)
    _category = input(label="Categoría", value=item.categoria)
    _details = input(label="Detalles", multiline=True, value=item.descripcion)
    _price = input(label="Precio", value=str(item.precio),input_filter=DecimalInputFilter())
    _stock = input(label="Stock", value=str(item.stock), input_filter=NumbersOnlyInputFilter())

    def handle_edit(e):
        updated_product = Producto(
            id=int(str(_id.value)),
            nombre=str(_name.value),
            categoria=str(_category.value),
            descripcion=str(_details.value),
            precio=float(str(_price.value)),
            stock=int(str(_stock.value))
        )
        edit_callback(updated_product)

    return dialog(
        title="Editar producto",
        content=column([_name, _category, _details, _price, _stock], w=w, h=h),
        action=button("Guardar", color=colors.BLUE_800, on_click=handle_edit)
    )