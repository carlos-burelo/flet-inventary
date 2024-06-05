from src.elements import dialog, column, input, button, colors
from src.models import Producto
from src.utils.filters import NumbersOnlyInputFilter, DecimalInputFilter

def NewProductForm(add_callback, h=350, w=300):
    _name = input(label="Nombre")
    _category = input(label="Categoría")
    _details = input(label="Detalles", multiline=True)
    _price = input(label="Precio",input_filter=DecimalInputFilter())
    _stock = input(label="Stock",input_filter=NumbersOnlyInputFilter())

    def handle_save(e):
        new_product = Producto(
            nombre=str(_name.value),
            categoria=str(_category.value),
            descripcion=str(_details.value),
            precio=float(str(_price.value)),
            stock=int(str(_stock.value))
        )
        add_callback(new_product)

    return dialog(
        title="Nuevo producto",
        content=column([_name, _category, _details, _price, _stock], w=w, h=h),
        action=button("Guardar", color=colors.BLUE_800, on_click=handle_save)
    )