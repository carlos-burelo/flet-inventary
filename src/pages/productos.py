from src.elements import *
from flet import icons, KeyboardEvent, SnackBar
from src.layout.page import page
from src.db.db import db
from src.models.product import Producto
from src.pages.components.edit_product_form import EditProductForm
from src.pages.components.new_product_form import NewProductForm
from src.pages.components.delete_product_form import DeleteProductForm
from src.pages.components.navbar import Navbar
import _

@page(route="/productos")
def ProductsPage():
    data = db.productos.obtener_todos_los_productos()
    row_names = Producto.PROPERTIES

    def search(e: KeyboardEvent):
        value = e.control.value
        all_products = db.productos.obtener_todos_los_productos()
        if value == "":
            data = all_products
        else:
            data = [product for product in all_products if value.lower() in product.nombre.lower()]
        datasource = create_datasource(data, row_names, edit, delete)
        _table.rows = datasource[1]
        _.root.update()

    def edit(item: Producto):
        def hande_edit(product_updated: Producto):
            edit_form.open = False
            db.productos.actualizar_producto(product_updated)
            _table.clean()
            nuevos_datos = db.productos.obtener_todos_los_productos()
            _table.rows = create_datasource(nuevos_datos, row_names, edit, delete)[1]
            _table.update()
            _.root.update()
        edit_form = EditProductForm(item, hande_edit)       
    
    def delete(item: Producto):
        def hande_delete(item: Producto):
            delete_form.open = False
            db.productos.eliminar_producto(item.id)
            _table.clean()
            nuevos_datos = db.productos.obtener_todos_los_productos()
            _table.rows = create_datasource(nuevos_datos, row_names, edit, delete)[1]
            _table.update()
            _.root.update()
        delete_form = DeleteProductForm(item, hande_delete)


    def new(e):
        def handle_save(new_product: Producto):
            new_form.open = False 
            db.productos.añadir_producto(new_product)
            _table.clean()
            nuevos_datos = db.productos.obtener_todos_los_productos()
            _table.rows = create_datasource(nuevos_datos, row_names, edit, delete)[1]
            _table.update()
            _.root.snack_bar = SnackBar(
                content=h3("Producto añadido correctamente"),
                bgcolor=colors.GREEN
            )

            _.root.snack_bar.open = True
            _.root.update()
        new_form = NewProductForm(handle_save)

    
    _table = table(data=data, row_names=row_names, edit_callback=edit, delete_callback=delete)

    return [
        Navbar(),
        img(src="src/assets/logo.png", w=300, h=100),
        row([
            input(label="Buscar...", icon=icons.SEARCH, on_change=search, expand=True),
            button("Nuevo producto", icon=icons.ADD, on_click=new),
        ]),
        column([_table], w=1400, h=400)
    ]