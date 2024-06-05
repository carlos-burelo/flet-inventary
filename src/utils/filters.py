from flet import NumbersOnlyInputFilter, InputFilter

class DecimalInputFilter(InputFilter):
    def __init__(self):
        super().__init__(r"\d+(\.\d+)?")
