from enum import Enum
from flet import CupertinoButton, colors, padding

class Display(Enum):
    BLOCK = "block"
    INLINE = "inline"

def button(text:str, color:str = colors.BLUE_800, on_click=None, display:Display=Display.INLINE, icon=None):
    return CupertinoButton(
        text=text,
        icon=icon,
        color=colors.WHITE,
        height=45,
        bgcolor=color,
        on_click=on_click,
        expand=display==Display.BLOCK,
        padding=padding.symmetric(horizontal=20, vertical=10),
    )