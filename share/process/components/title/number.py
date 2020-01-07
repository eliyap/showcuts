import re, copy

from ..base_magic import base_magic, html_slot
from ..magic_helpers import *

class number(base_magic):
    '''Field that accepts numbers.

    In Shortcuts, this accepts:

       * signed floats and integers
       * a single magic variable (no inline expressions)
       * blank (nothing)
    
    :NOTE: ``number`` may accept a ``default`` value. If the default
    state is blank, simply self ``default=None``.
    '''

    def __init__(
        self, 
        key:str,
        default:str,
        blank_text:str,
        ask_each_time:str,
    ) -> dict:
        self.default = default
        self.blank_text = blank_text
        base_magic.__init__(self, key, ask_each_time, attrs=dict(
            key=key,
            default=default,
            ask_each_time=ask_each_time,
            blank_text=blank_text,
        ))

    def blank(self):
        return magic_dct(
            self.blank_text, 
            attrs=self.attrs,
            empty=True,
        )

    @AddField('number')
    def to_html(self, params, UUID_glyphs):
        missing = lambda self: [magic_dct(self.default, attrs=self.attrs)]
        blank = lambda self: [magic_dct(self.blank_text, attrs=self.attrs, empty=True)]
        non_magic = lambda self, parameter: [magic_dct(parameter, attrs=self.attrs)]
        
        # If no default argument is provided, fall back on the blank_text
        if self.default == None:
            missing = blank

        return html_slot(
            missing,
            blank,
            non_magic,
        )(self, params, UUID_glyphs)

class whole_number(number):
    '''Field that accepts only whole numbers.

    In Shortcuts, this is identical to ``number``, 
    except the decimal point is not available.
    '''
    # accepts signed whole numbers
    @AddField('wholenumber')
    def to_html(self, params, UUID_glyphs):
        return super().to_html(params, UUID_glyphs)