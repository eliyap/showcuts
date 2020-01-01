from .magic_helpers import *

class base_magic:
    def __init__(
        self,
        key:str, # parameter's name in .plist file
        ask_each_time:str, # 'Ask Each Time' custom label
    ):
        self.key = key
        self.ask_each_time = ask_each_time

    def to_html(self, params, UUID_glyphs:dict):
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
        return {} # to be overridden!

    
    # def control_flow(self) -> (str, int):
    #     return (
    #         self.parameters['GroupingIdentifier'], 
    #         self.parameters['WFControlFlowMode'],
    #     )
