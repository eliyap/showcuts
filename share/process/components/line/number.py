import re, copy

from ..base_line import line
from ..title.number import number
from ..base_magic import html_slot
from ..magic_helpers import *

class line_number(line, number):
    def __init__(
        self, 
        label:str,
        key:str,
        default:str,
        blank_text:str,
        ask_each_time:str,
    ) -> dict:
        line.__init__(self, label) # no leftify
        number.__init__(self, key, default, blank_text, ask_each_time)

    @AddField('number')
    def to_html(self, params, UUID_glyphs):
        return [{
            **line.to_html(self),
            **html_slot(
                missing = lambda self: [self.missing()],
                blank = lambda self: [self.blank()],
                non_magic = lambda self, parameter: [value_dct(parameter, attrs=self.attrs)],
            )(self, params, UUID_glyphs)[0],
        }]

    def missing(self):
        if self.default == None: # NOTE: do not allow falsy values (0, '', etc.)
            return self.blank()
        else:
            return value_dct(
                self.default, 
                attrs=self.attrs,
                empty=False,
            )

    def blank(self):
        return value_dct(
            self.blank_text, 
            attrs=self.attrs,
            empty=True,
        )