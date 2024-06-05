from src.elements import dialog, column, input, button, colors
from src.models import Proveedor
from src.utils.filters import NumbersOnlyInputFilter, DecimalInputFilter

def NewProviderForm(add_callback, h=350, w=300):
    _name = input(label="Nombre")
    _phone = input(label="Teléfono", input_filter=NumbersOnlyInputFilter())
    _address = input(label="Dirección")


    def handle_save(e):
        nuevo_proveedor = Proveedor(
            nombre=str(_name.value),
            direccion=str(_address.value),
            telefono=str(_phone.value)
        )
        add_callback(nuevo_proveedor)

    return dialog(
        title="Nuevo proveedor",
        content=column([_name,
                        _phone,
                        _address,
                        ], w=w, h=h),
        action=button("Guardar", color=colors.BLUE_800, on_click=handle_save)
    )