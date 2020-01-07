import re
from copy import deepcopy

from ..base_line import line
from ..title.inline import inline, inline_handler
from ..magic_helpers import *

def inline_html(self, params, UUID_glyphs):
    parameter = params.get(self.key, None)
    if parameter in [None, '']: 
        return self.blank()

    if not isinstance(parameter, dict): # non-magic variables
        return value_dct(
            [value_dct(parameter, attrs={})], #wrap as an inline var
            attrs=self.attrs,
            css_class=deepcopy(self.__class__.css_cls),
        )
    return inline_handler(self, parameter, UUID_glyphs)

class line_inline(line, inline):
    css_cls = ['inline-line']

    def __init__(
        self, 
        label:str, 
        key:str,
        blank_text:str, 
        leftify=False,
    ):
        line.__init__(self, label, leftify)
        inline.__init__(self, key, blank_text=blank_text)

    @AddField('inline')
    def to_html(self, params, UUID_glyphs):
        elem = {
            **line.to_html(self),
            **inline_html(self, params, UUID_glyphs),
        }
        return [elem]

    def blank(self):
        return value_dct(
            [value_dct(self.blank_text, attrs={})], #wrap as an inline var
            attrs=self.attrs,
            css_class=deepcopy(self.__class__.css_cls),
            empty=True,
        )