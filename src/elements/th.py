from flet import DataColumn, Text, TextStyle,FontWeight, TextOverflow

def th(text: str):
    return DataColumn(Text(text, overflow=TextOverflow.FADE, style=TextStyle(weight=FontWeight.W_700)))