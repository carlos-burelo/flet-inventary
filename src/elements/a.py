from flet import IconButton
import _

def a(icon: str, href: str = "/", tooltip: str = "Default"):
    return IconButton(icon, on_click=lambda a: _.root.go(href), tooltip=tooltip)