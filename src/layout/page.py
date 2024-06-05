from functools import wraps
from flet import View, CrossAxisAlignment, Column, colors
import _

def page(route: str, w:float = 650, h: float = 600):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            controls = func(*args, **kwargs)
            return View(
                route=route,
                bgcolor=colors.WHITE,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Column(
                        width=w,
                        height=h,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=controls
                    )
                ]
            )
        return wrapper
    return decorator
