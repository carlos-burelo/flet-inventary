from flet import AlertDialog, RoundedRectangleBorder, Control, colors, padding, MainAxisAlignment,Text, TextStyle, FontWeight
from src.elements.button import button
import _

def dialog(content: Control, action: Control, title: str = "Dialog"):
    def close_dlg(e):
        modal.open = False
        _.root.update()

    modal =  AlertDialog(
        shape=RoundedRectangleBorder(radius=10),
        content=content,
        elevation=2,
        title=Text(title, color=colors.BLUE_800, style=TextStyle(weight=FontWeight.W_700)),
        bgcolor=colors.WHITE,
        content_padding=padding.all(10),
        actions_alignment=MainAxisAlignment.END,
        actions=[
            action,
            button(text="Cancelar", on_click=close_dlg, color=colors.RED_800),
        ],
    )
    _.root.dialog = modal
    modal.open = True
    _.root.update()

    return modal