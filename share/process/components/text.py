from .magic_helpers import AddField
class text:
    def __init__(self, text:str):
        self.text = text

    @AddField('text')
    def to_html(self, *_, **__) -> dict:
        return [{
            'value': self.text, 
            'class': ['text'], 
            'attrs':{
                'key':None,
            },
        }]