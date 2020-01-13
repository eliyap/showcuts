from copy import deepcopy
from showcuts.local_settings import DEBUG

from ..text import elem as text
from ..magic_helpers import *
from ..base_magic import base_magic

class music(base_magic):
    '''Field that accepts music / radio stations from Apple Music.

    In Shortcuts, this accepts:

       * song from native Music app
       * radio station from native Music app
       * "Ask Each Time"
    
    '''
    
    #: List of CSS classes to style the element.

    def __init__(
        self, 
        key, 
        blank_text:str,
        ask_each_time:str,
    ):
        super().__init__(key, ask_each_time, attrs=dict(
            key=key,
            ask_each_time=ask_each_time,
            blank_text=blank_text,
        ))
        self.blank_text = blank_text

    def to_html(self, params, UUID_glyphs):
        parameter = params.get(self.key, None)
        if parameter in [None, '']: 
            return [self.blank()]
        elif 'itemName' in parameter: # music specified
            return [magic_dct(parameter['itemName'], attrs=self.attrs)]
        elif ('itemName' not in parameter) and ('Value' not in parameter):
            '''encounntered during testing: blank variable had some information,
            none of it useful. I am choosing to label this blank.
            '''
            return [self.blank()]
        return [classify_magic(
            parameter['Value'],
            parameter['Value']['Type'],
            attrs=self.attrs,
            ask_each_time=self.ask_each_time,
            UUID_glyphs=UUID_glyphs,
        )]

    def blank(self):
        return magic_dct(
            self.blank_text,
            attrs=self.attrs, 
            empty=True,
        )