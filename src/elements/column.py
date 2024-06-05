from flet import Column, Control, CrossAxisAlignment, ScrollMode

def column(items: list[Control], w: int = 650, h: int = 500):
    return Column(
        [*items],
        height=h,
        width=w,
        scroll=ScrollMode.ALWAYS,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )