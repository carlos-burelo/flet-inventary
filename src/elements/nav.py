from flet import Row, MainAxisAlignment


def nav(*items):
    return Row(
        [*items],
        alignment=MainAxisAlignment.CENTER,
        spacing=20
    )