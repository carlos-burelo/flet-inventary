from flet import DataTable, IconButton, Column, ScrollMode, icons, Row, MainAxisAlignment, TextStyle
from src.utils.borders import ALL_BORDERS, UNIQUE_BORDER
from src.elements.td import td
from src.elements.th import th
from src.elements.tr import tr

def table(data, row_names: list[str], edit_callback=None, delete_callback=None):
    columns, rows = create_datasource(data, row_names, edit_callback, delete_callback)

    return DataTable(
            border=ALL_BORDERS,
            border_radius=10,
            data_row_max_height=40,
            data_row_min_height=10,
            vertical_lines=UNIQUE_BORDER,
            show_checkbox_column=True,
            checkbox_horizontal_margin=10,
            sort_ascending=True,
            sort_column_index=0,
            column_spacing=20,
            heading_row_height=40,
            horizontal_margin=10,
            columns=columns,
            rows=rows,
        )

def action_buttons(item, edit_callback=None, delete_callback=None):
    buttons = []

    if edit_callback:
        edit_button = IconButton(
            icon=icons.EDIT_ROUNDED,
            on_click=lambda _: edit_callback(item),
        )
        buttons.append(edit_button)

    if delete_callback:
        delete_button = IconButton(
            icon=icons.DELETE_ROUNDED,
            on_click=lambda _: delete_callback(item),
        )
        buttons.append(delete_button)

    return td(Row([*buttons], spacing=0, alignment=MainAxisAlignment.START))  # Devolver celdas con los botones de acción


def create_datasource(data, row_names, edit = None, delete = None):
    columns = []
    rows = []

    if data:
        first_item = data[0]
        columns = [th(attr.upper()) for attr in first_item.__dict__.keys()]
        if (edit != None or delete != None):
            columns.append(th('Actions'.upper()))

    for item in data:
        cells = []
        for attr in row_names:
            cells.append(td(str(getattr(item, attr, ''))))
        if (edit != None or delete != None):
            action_cells = action_buttons(item, edit, delete)
            cells.append(action_cells)
        rows.append(tr(*cells))
    return columns, rows