from ..base_magic import base_magic
from ..magic_helpers import *

class quantity(base_magic):

    def __init__(
        self, 
        key:str, 
        ask_each_time:str, # magnitude's Ask Each Time
        blank_text:str, # magnitude's blank
    ):
        super().__init__(key, ask_each_time)
        self.blank_text = blank_text

    def to_html(self, params, UUID_glyphs):
        parameter = params.get(self.key, None)
        if parameter in [None, '']: 
            return self.blank() # NOTE: blank returns a list of 2 vars, unlike other actions

        if not isinstance(parameter, dict): # non-magic variables
            return [magic_dct(parameter)]

        return [classify_magic(
            value = parameter['Value'],
            var_type = parameter['Value']['Type'],
            ask_each_time = self.ask_each_time,
            UUID_glyphs = UUID_glyphs,
        )]

    def blank(self):
        return super().blank()