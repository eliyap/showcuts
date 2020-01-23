from ..base_magic import base_magic
from ..magic_helpers import *
from .number import number
from .choose import choose

class quantity_magnitude(number):
    '''Field representing a quantity or measurement's magnitude.

    Data stored with sister variable `quantity_unit`.

    In Shortcuts, this field accepts:
       * a magnitude, similar to the ``number`` class
    '''

    def __init__(
        self, 
        key:str,
        default:str,
        blank_text:str,
        ask_each_time:str,
    ):
        super().__init__(key,default,blank_text,ask_each_time)
    
    @AddField('measurement')
    def to_html(self, params, UUID_glyphs):
        parameter = params.get(self.key, None)
        if parameter in [None, '']: 
            return self.blank() # NOTE: blank returns a list of 2 vars, unlike other actions

        if not isinstance(parameter, dict): # non-magic variables
            return [magic_dct(parameter, attrs=self.attrs)]

        return [classify_magic(
            value = parameter['Value'],
            var_type = parameter['Value']['Type'],
            ask_each_time = self.ask_each_time,
            UUID_glyphs = UUID_glyphs,
            attrs=self.attrs,
        )]

    def blank(self):
        return super().blank()

class quantity_unit(base_magic):
    '''Field representing a quantity or measurement's unit.

    In Shortcuts, this field accepts:
       * a unit, similar to the ``choose`` class

    Data stored with sister variable `quantity_magnitude`.

    The unit offered in the ``choose`` menu 
    and the abbreviation shown in the ``unit`` field
    differ significantly and often.
    '''

    def __init__(
        self, 
        key:str, 
        ask_each_time:str, # usually None?
        default
    ):
        super().__init__(key, ask_each_time, attrs=dict(
            key=key,
            ask_each_time=ask_each_time,
            blank_text=blank_text,
        ))
        self.blank_text = blank_text
    
    @AddField('measurement')
    def to_html(self, params, UUID_glyphs):
        parameter = params.get(self.key, None)
        if parameter in [None, '']: 
            return self.blank() # NOTE: blank returns a list of 2 vars, unlike other actions

        if not isinstance(parameter, dict): # non-magic variables
            return [magic_dct(parameter, attrs=self.attrs)]

        return [classify_magic(
            value = parameter['Value'],
            var_type = parameter['Value']['Type'],
            ask_each_time = self.ask_each_time,
            UUID_glyphs = UUID_glyphs,
            attrs=self.attrs,
        )]

    def blank(self):
        return super().blank()