import re

from ..base_line import line
from ..base_magic import base_magic
from ..magic_helpers import *

class line_toggle(line, base_magic):
    def __init__(
        self, 
        label:str,
        key:str,
        default:bool,
        ask_each_time:str,
    ) -> dict:
        self.default = default
        line.__init__(self, label) # no leftify, toggle is always right aligned
        base_magic.__init__(self, key, ask_each_time, attrs=dict(
            key=key,
            default=default,
            ask_each_time=ask_each_time,
        ))

    @AddField('toggle')
    def to_html(self, params, UUID_glyphs):
        toggle_state = params.get(self.key, self.default)
        if isinstance(toggle_state, bool):
            toggle_elem = {
                True: {'class':['toggle','on'], 'value':'', 'attrs':self.attrs},
                False:{'class':['toggle','off'], 'value':'', 'attrs':self.attrs},
            }[toggle_state]
        elif isinstance(toggle_state, dict):
            toggle_elem = base_magic.to_html(self, params, UUID_glyphs)[0] # extract from list
        else:
            raise ValueError(f'Unexpected type for toggle_state: {type(toggle_state)}')
        return [{
            **line.to_html(self),
            **toggle_elem,
        }]

    def blank(self):
        return value_dct(
            [value_dct(self.blank_text, attrs={})], #wrap as an inline var
            attrs=self.attrs,
            css_class = ['inline-line'],
            empty=True,
        )