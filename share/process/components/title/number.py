import re, copy

from ..base_magic import base_magic
from ..magic_helpers import *

class number(base_magic):
    '''Field that accepts numbers.

    In Shortcuts, this accepts:

       * signed floats and integers
       * a single magic variable (no inline expressions)
       * blank (nothing)
    
    '''

    def __init__(
        self, 
        key:str,
        blank_text:str,
        ask_each_time:str,
    ) -> dict:
        self.blank_text = blank_text
        base_magic.__init__(self, key, ask_each_time)

    def blank(self):
        return magic_dct(
            self.blank_text, 
            empty=True,
        )

class whole_number(number):
    '''Field that accepts only whole numbers.

    In Shortcuts, this is identical to ``number``, 
    except the decimal point is not available.
    '''
    pass
    # accepts signed whole numbers