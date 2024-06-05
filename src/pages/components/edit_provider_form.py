from src.elements import dialog, column, input, button, colors
from src.models import Proveedor
from src.utils.filters import NumbersOnlyInputFilter


def EditProviderForm(item: Proveedor, edit_callback, w=300, h=350):
    _id = input(label="ID", visible=False, value=str(item.id))
    _name = input(label="Nombre", value=item.nombre)
    _phone = input(label="Teléfono", value=item.telefono, input_filter=NumbersOnlyInputFilter())
    _address = input(label="Dirección", value=item.direccion)


    def handle_edit(e):
        proveedor_actualizado = Proveedor(
            id=int(str(_id.value)),
            nombre=str(_name.value),
            telefono=str(_phone.value),
            direccion=str(_address.value)
        )
        edit_callback(proveedor_actualizado)

    return dialog(
        title="Editar proveedor",
        content=column([_name,
                        _phone,
                        _address,
                        ], w=w, h=h),
        action=button("Guardar", color=colors.BLUE_800, on_click=handle_edit)
    )