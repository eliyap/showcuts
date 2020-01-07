from ..magic_helpers import *
from ..base_magic import base_magic




class magic(base_magic):
    '''Basic Magic Variable Field.

    In Shortcuts, this simplest of fields can accept:

       * results from other actions
       * "global" variables such as Clipboard, Current Date, Shortcut Input
       * blank (nothing)
    
    '''

    def __init__(
        self, 
        key:str, 
        blank_text:str, # lighter text when the variable is cleared
        ask_each_time:str, 
    ):
        super().__init__(key, ask_each_time, attrs=dict(
            key=key,
            ask_each_time=ask_each_time,
            blank_text=blank_text,
        ))
        self.blank_text = blank_text

    @AddField('magic')
    def to_html(self, params, UUID_glyphs):
        return super().to_html(params, UUID_glyphs)

    def blank(self):
        return magic_dct(
            self.blank_text, 
            attrs=self.attrs,
            empty=True
        )

    