import re
from copy import deepcopy

from .inline import line_inline, inline_html, inline_handler
from ..base_line import line
from ..magic_helpers import *
from .._directory import text

class line_notes(line_inline):
    css_cls = ['notes']

    def __init__(
        self, 
        key:str,
        default:str,
        blank_text:str, 
    ):
        super().__init__(
            label='',
            key=key,
            blank_text=blank_text,
            leftify=True,
        )
        self.default = default
        self.attrs.update(dict(default=default))

    @AddField('notes')
    def to_html(self, params, UUID_glyphs):
        return [{
            **line.to_html(self),
            **self.inline_html(params, UUID_glyphs),
        }]

    def inline_html(self, params, UUID_glyphs):
        parameter = params.get(self.key, None)
        import logging
        logging.error('flag!')
        if parameter == None: 
            return value_dct(
                text(self.default).to_html(), #wrap as an inline var
                attrs=self.attrs,
                css_class=deepcopy(self.__class__.css_cls),
            ) 

        elif parameter == '':
            return self.blank()

        elif not isinstance(parameter, dict): # non-magic variables
            return value_dct(
                text(parameter).to_html(), #wrap as an inline var
                attrs=self.attrs,
                css_class=deepcopy(self.__class__.css_cls),
            )
        return inline_handler(self, parameter, UUID_glyphs)

    def blank(self):
        return value_dct(
            text(self.blank_text).to_html(), #wrap as an inline var
            attrs=self.attrs,
            css_class=deepcopy(self.__class__.css_cls),
            empty=True,
        )

class line_code(line_notes):
    css_cls = ['notes','code']


    