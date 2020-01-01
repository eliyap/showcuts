from .magic_helpers import *
from .base_magic import base_magic

# Magic Variables
# the basic magic variable field can hold:
#  - results from other actions
#  - "global" variables (Clipboard, Current Date, Shortcut Input)
#  - blanks

class magic(base_magic):
    def __init__(
        self, 
        key:str, 
        blank_text:str, # lighter text when the variable is cleared
        ask_each_time:str, 
    ):
        super().__init__(key, ask_each_time)
        self.blank_text = blank_text

    def blank(self):
        return magic_dct(self.blank_text, empty=True)

    