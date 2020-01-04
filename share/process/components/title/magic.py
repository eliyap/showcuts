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
        super().__init__(key, ask_each_time)
        self.blank_text = blank_text

    def blank(self):
        return magic_dct(
            self.blank_text, 
            key=self.key,
            empty=True
        )

    