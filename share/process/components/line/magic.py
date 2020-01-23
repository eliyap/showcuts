from ..base_magic import base_magic, html_slot
from ..base_line import line
from ..magic_helpers import *

class line_magic(base_magic, line):
    def __init__(
        self, 
        label:str,
        key:str, 
        blank_text:str,
    ):
        '''Line variant of `magic` title field.
        
        Does not accept `ask_each_time`, as far as I know.
        '''
        base_magic.__init__(self, key, ask_each_time=None, attrs=dict(
            label=label,
            key=key,
            ask_each_time=None,
            blank_text=blank_text,
        ))
        line.__init__(self, label, leftify=False)
        self.blank_text = blank_text
    
    @AddField('magic')
    def to_html(self, params, UUID_glyphs) -> [dict]:
        return [{
            **line.to_html(self),
            **html_slot(
            missing=lambda self: [self.blank()],
            blank=lambda self: [self.blank()],
            non_magic=lambda self, parameter: [magic_dct(parameter, attrs=self.attrs)]
        )(self, params, UUID_glyphs)[0],
        }]

    def blank(self) -> dict:
        return value_dct(
            self.blank_text,
            attrs=self.attrs,
            css_class=['choose'],
            empty=False,
        )
