from src.layout.page import page
from src.elements import h1, column, input, button, img, h3
from flet import SnackBar, colors
import _
from src.db.db import db

@page(route="/")
def HomePage():
    _usuario = input(label="Email")
    _contraseña = input(label="Contraseña")

    def iniciar_sesion(e):
        email = str(_usuario.value)
        contraseña = str(_contraseña.value)
        usuario = db.usuarios.obtener_usuario_por_email(email)
        if usuario and usuario.password == contraseña:
            _.root.go("/productos")
        else:
            _.root.snack_bar = SnackBar(
                content=h3("Usuario o contraseña incorrectos"),
                bgcolor=colors.RED
            )
            _.root.snack_bar.open = True
            _.root.update()


    return [
        img(src="src/assets/logo.png", w=300, h=100),
        h1("Iniciar Sesión"),
        column([
            _usuario,
            _contraseña,
            button("Iniciar Sesión", on_click=iniciar_sesion)
        ], h=200, w=300)
    ]