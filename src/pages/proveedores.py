from src.layout.page import page
from src.elements import column, row, input, button, img, nav,a, icons, table, create_datasource
from src.pages.components.edit_provider_form import EditProviderForm
from src.pages.components.new_provider_form import NewProviderForm
from src.pages.components.delete_provider_form import DeleteProviderForm
from src.pages.components.navbar import Navbar
from src.db.db import db
from src.models.proveedor import Proveedor
import _

@page(route="/proveedores")
def ProvidersPage():
    data = db.proveedores.obtener_todos_los_proveedores()

    def search(e):
        value = e.control.value
        all_providers = db.proveedores.obtener_todos_los_proveedores()
        if value == "":
            data = all_providers
        else:
            data = [provider for provider in all_providers if value.lower() in provider.nombre.lower()]
        _table.rows = create_datasource(data, Proveedor.PROPERTIES, edit, delete)[1]
        _.root.update()

    def edit(item: Proveedor):
        def handle_edit(provider_updated: Proveedor):
            edit_form.open = False
            db.proveedores.actualizar_proveedor(provider_updated)
            _table.clean()
            nuevos_datos = db.proveedores.obtener_todos_los_proveedores()
            _table.rows = create_datasource(nuevos_datos, Proveedor.PROPERTIES, edit, delete)[1]
            _table.update()
            _.root.update()
        edit_form = EditProviderForm(item, handle_edit)

    def delete(item: Proveedor):
        def handle_delete(item: Proveedor):
            delete_form.open = False
            db.proveedores.eliminar_proveedor(item.id)
            _table.clean()
            nuevos_datos = db.proveedores.obtener_todos_los_proveedores()
            _table.rows = create_datasource(nuevos_datos, Proveedor.PROPERTIES, edit, delete)[1]
            _table.update()
            _.root.update()
        delete_form = DeleteProviderForm(item, handle_delete)

    def new(e):
        def handle_save(new_provider: Proveedor):
            new_form.open = False
            db.proveedores.añadir_proveedor(new_provider)
            _table.clean()
            nuevos_datos = db.proveedores.obtener_todos_los_proveedores()
            _table.rows = create_datasource(nuevos_datos, Proveedor.PROPERTIES, edit, delete)[1]
            _table.update()
            _.root.update()
        new_form = NewProviderForm(handle_save)

    _table = table(data=data, row_names=Proveedor.PROPERTIES, edit_callback=edit, delete_callback=delete)
    return [
        Navbar(),
        img(src="src/assets/logo.png", w=300, h=100),
        row([
            input(label="Buscar...", icon=icons.SEARCH, on_change=search, expand=True),
            button("Nuevo proveedor", icon=icons.ADD, on_click=new),
        ]),
        column([_table], w=1400, h=400)
    ]