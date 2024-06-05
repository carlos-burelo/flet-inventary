from flet import BorderSide, Border, colors

BORDER_COLOR = colors.BLACK26
BORDER_WIDTH = 1

UNIQUE_BORDER = BorderSide(color=BORDER_COLOR, width=BORDER_WIDTH)


ALL_BORDERS = Border(
    bottom=BorderSide(color=BORDER_COLOR, width=BORDER_WIDTH),
    top=BorderSide(color=BORDER_COLOR, width=BORDER_WIDTH),
    left=BorderSide(color=BORDER_COLOR, width=BORDER_WIDTH),
    right=BorderSide(color=BORDER_COLOR, width=BORDER_WIDTH),
)