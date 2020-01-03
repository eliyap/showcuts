from .magic_helpers import *

class base_magic:
    '''Base class for magic variables.'''

    def __init__(
        self,
        key:str, # parameter's name in .plist file
        ask_each_time:str, # 'Ask Each Time' custom label
    ):
        '''
        :param key: Key (in the action's `WFWorkflowActionParameters` dictionary) to the magic variable's value

        :param ask_each_time: The text used when `Ask Each Time` is selected as an option. 

        :ask_each_time:
        * Usually, the text is simply "Ask Each Time". In inline variables, it is usually "Text"
        * If `Ask Each Time` is not offered as an valid input, set this value as ``None``
        '''

        self.key = key
        self.ask_each_time = ask_each_time

    def to_html(self, params:dict, UUID_glyphs:dict) -> dict:
        '''
        Invoked by the ``to_django`` method to convert a variable object to a dict describing the contents of the action.

        :param params: The action's `WFWorkflowActionParameters` dict. Contains information on what values were filled into each magic variable.

        :param UUID_glyphs: Previous actions' outputs can be used as magic variable inputs, and are displayed alongside the output-action's glyph. ``UUID Glyphs`` maps actions' output UUIDs to their glyphs.
        '''

        parameter = params.get(self.key, None)
        if parameter in [None, '']: 
            return [self.blank()]

        if not isinstance(parameter, dict): # non-magic variables
            return [magic_dct(parameter)]

        return [classify_magic(
            value = parameter['Value'],
            var_type = parameter['Value']['Type'],
            ask_each_time = self.ask_each_time,
            UUID_glyphs = UUID_glyphs,
        )]

    def blank(self):
        '''
        Handles output when the variable was left blank.

        :NOTE: Variables are sometimes prefilled. If a variable's value is not changed from the default value, their key will be absent from ``params``. **This is different to the variable being blank**. Fields with prefilled values will include a ``default`` field.
        '''
        return {} # to be overridden!