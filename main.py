from flet import Page, app, RouteChangeEvent, ThemeMode, View
from src.pages.productos import ProductsPage
from src.pages.inicio import HomePage
from src.pages.proveedores import ProvidersPage
from src.pages.movimientos import MovimientosStockPage
from typing import cast
import _

routes = {
    "/": HomePage,
    "/productos": ProductsPage,
    "/proveedores": ProvidersPage,
    "/movimientos-stock": MovimientosStockPage
}

def main(page: Page):
    global _
    _.root = page
    page.theme_mode = ThemeMode.LIGHT
    page.views.clear()
    def route_change(route: RouteChangeEvent):
        page_func = routes.get(route.route)
        if page_func:
            page.views.clear()
            result = cast(View, page_func())
            page.views.append(result)
            page.update()
        else:
            page.update()

    def view_pop(_):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

app(target=main)

