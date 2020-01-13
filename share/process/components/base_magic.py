from .magic_helpers import *
from typing import Callable

class base_magic:
    '''Base class for magic variables.'''

    def __init__(
        self,
        key:str, # parameter's name in .plist file
        ask_each_time:str, # 'Ask Each Time' custom label
        attrs:dict,
    ):
        '''
        :param key: Key (in the action's `WFWorkflowActionParameters` dictionary) 
           to the magic variable's value

        :param ask_each_time: The text used when `Ask Each Time` is 
           selected as an option. 
        
        :param attrs: Dict of information to be passed to HTML. 

        :ask_each_time:
        
           * Usually, the text is simply "Ask Each Time". In inline variables, it is usually "Text"
           * If `Ask Each Time` is not offered as an valid input, set this value as ``None``
        '''

        self.key = key
        self.ask_each_time = ask_each_time
        self.attrs = attrs

    def to_html(self, params:dict, UUID_glyphs:dict) -> dict:
        '''
        Invoked by the ``to_django`` method to convert a variable object to a dict describing the contents of the action.

        :param params: The action's `WFWorkflowActionParameters` dict. Contains information on what values were filled into each magic variable.

        :param UUID_glyphs: Previous actions' outputs can be used as magic variable inputs, and are displayed alongside the output-action's glyph. ``UUID Glyphs`` maps actions' output UUIDs to their glyphs.
        '''

        return html_slot(
            missing=lambda self:[self.blank()],
            blank=lambda self:[self.blank()],
            non_magic=lambda self, parameter:[magic_dct(parameter, attrs=self.attrs)]
        )(self, params, UUID_glyphs)


    def blank(self):
        '''Handles output when the variable was left blank.'''
    
        '''
        :NOTE: Variables are sometimes prefilled. 
        If a variable's value is not changed from the default value, 
        their key will be absent from ``params``. 
        **This is different to the variable being blank**. 
        Fields with prefilled values will include a ``default`` field.
        '''
        return {} # to be overridden!

def html_slot(
    missing:Callable,
    blank:Callable,
    non_magic:Callable,
):
    '''Builds a custom func to override to_html().'''
    
    def to_html(
        self, 
        params:dict, 
        UUID_glyphs:dict
    ) -> dict:
        parameter = params.get(self.key, None)
        if parameter == None:
            return missing(self)
        elif parameter == '': 
            return blank(self)
        elif not isinstance(parameter, dict): # non-magic variables
            return non_magic(self, parameter)
        else:
            return [classify_magic(
                value = parameter['Value'],
                var_type = parameter['Value']['Type'],
                ask_each_time = self.ask_each_time,
                UUID_glyphs = UUID_glyphs,
                attrs=self.attrs,
            )]

    return to_html