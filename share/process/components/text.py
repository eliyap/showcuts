class text:
    def __init__(self, text:str):
        self.text = text

    def to_html(self, *_, **__) -> dict:
        return [{'value': self.text, 'class': ['text'], 'key':'None'}]