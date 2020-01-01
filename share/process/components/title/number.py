import re, copy

from ..base_magic import base_magic
from ..magic_helpers import *

class number(base_magic):

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
    pass
    # accepts signed whole numbers