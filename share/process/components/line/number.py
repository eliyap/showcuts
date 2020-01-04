import re, copy

from ..base_line import line
from ..base_magic import base_magic
from ..magic_helpers import *

class line_number(line, base_magic):
    css_cls = ['number']

    def __init__(
        self, 
        label:str,
        key:str,
        blank_text:str,
        ask_each_time:str,
    ) -> dict:
        self.blank_text = blank_text
        line.__init__(self, label) # no leftify
        base_magic.__init__(self, key, ask_each_time)

    def to_html(self, params, UUID_glyphs):
        return [{
            **line.to_html(self),
            **self.line_html(params, UUID_glyphs),
        }]

    def line_html(self, params, UUID_glyphs):
        parameter = params.get(self.key, None)
        if parameter in [None, '']: 
            return self.blank()

        if not isinstance(parameter, dict): # non-magic variables
            return value_dct(
                parameter, 
                key=self.key,
                css_class=copy.deepcopy(self.__class__.css_cls),
            )

        return classify_magic(
            value = parameter['Value'],
            var_type = parameter['Value']['Type'],
            ask_each_time = self.ask_each_time,
            UUID_glyphs = UUID_glyphs,
            key=self.key,
        )


    def blank(self):
        return value_dct(
            self.blank_text, 
            key=self.key,
            css_class=copy.deepcopy(self.__class__.css_cls),
            empty=True,
        )