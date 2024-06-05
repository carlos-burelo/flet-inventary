from flet import DataCell, Text, Control, TextOverflow
from typing import Union

def td(content: Union[str, Control]):
    if isinstance(content, Control):
        return DataCell(content)
    else:
        return DataCell(Text(content, overflow=TextOverflow.NONE))

