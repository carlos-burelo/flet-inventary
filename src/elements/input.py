from cProfile import label
from flet import TextField, RadioGroup, Radio, Column

def input(label, value=None, input_filter=None, icon=None, on_change=None, on_submit=None, visible=True, expand=False, multiline=False):
    return TextField(
        label=label, 
        visible=visible,
        value=value, 
        input_filter=input_filter,
        height=90 if multiline is True else 45,

        prefix_icon=icon,
        on_change=on_change,
        on_submit=on_submit,
        expand=expand,
        multiline=multiline,
        min_lines=2 if multiline is True else 1
    )


class RadioOption:
    def __init__(self, label: str, value: str):
        self.label = label
        self.value = value

def input_radio(options: list[RadioOption], default:RadioOption = None): # type: ignore
    return RadioGroup(
        Column([Radio(label=option.label, value=option.value) for option in options]),
        value=default.value if default is not None else None,
    )