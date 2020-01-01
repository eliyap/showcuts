class line:
    def __init__(
        self,
        label:str,
        leftify = False, # determines whether the element is left / right aligned
    ):
        self.label = label
        self.leftify = leftify

    def to_html(self):
        return {'label':self.label}