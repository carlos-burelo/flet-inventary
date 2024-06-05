from flet import Row, MainAxisAlignment, CrossAxisAlignment, Control

def row(controls: list[Control], w: int = 650):
    return Row(
        width=w,
        controls=controls,
        vertical_alignment=CrossAxisAlignment.CENTER,
        alignment=MainAxisAlignment.CENTER,
    )