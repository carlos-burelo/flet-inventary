from flet import Text, TextStyle, FontWeight

def h1(text: str):
    return Text(text, size=30, color="#000000", style=TextStyle(weight=FontWeight.BOLD))

def h2(text: str):
    return Text(text, size=25, color="#000000", style=TextStyle(weight=FontWeight.BOLD))

def h3(text: str):
    return Text(text, size=20, color="#000000", style=TextStyle(weight=FontWeight.BOLD))

def h4(text: str):
    return Text(text, size=18, color="#000000", style=TextStyle(weight=FontWeight.BOLD))