from flet import DataRow

def tr(*items):
    return DataRow(
        cells=[*items]
   )   