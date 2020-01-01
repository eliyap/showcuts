from copy import deepcopy
from showcuts.local_settings import DEBUG

from ..text import elem as text
from ..magic_helpers import *
from ..base_magic import base_magic

# Inline Field:
# magic field, accepts arbitrary text with magic variables mixed in

def inline_handler(self, parameter:dict, UUID_glyphs):
    inline_dct = parameter['Value']
    inline_element = {'class':deepcopy(self.__class__.css_cls),'value':[]}
    try:
        assert parameter['WFSerializationType'] == 'WFTextTokenString'
        attachments = inline_dct['attachmentsByRange']
        f_string = list(inline_dct['string']) # convert string to list of chars
        
        # replace \uFFFC with variables
        for key, val in attachments.items():
            start, length = eval(key[1:-1]) # cut off the {}
            assert length == 1
            assert f_string[start] == '￼' # '' contains \uFFFC
            f_string[start] = classify_magic(
                val,
                val['Type'],
                ask_each_time='Text',
                UUID_glyphs=UUID_glyphs,
            )

        # process remaining chars into text elems
        charray = '' # char array
        for elem in f_string:
            if isinstance(elem, dict):
                inline_element['value'] += [
                    text(charray).to_html()[0], # need to invoke to_html directly
                    elem,
                ]
                charray = '' # reset
            else:
                charray += elem
        inline_element['value'].append(text(charray).to_html()[0]), # last fragment
        inline_element['value'] = [i for i in inline_element['value'] if i['value']] # remove empty strings (might not be working properly)
        return inline_element
    except:
        if DEBUG: raise
        return error_magic()
    


class inline(base_magic):
    css_cls = ['inline-magic']

    def __init__(
        self, 
        key, 
        blank_text:str,
        ask_each_time = None, # never used
    ):
        super().__init__(key, ask_each_time)
        self.blank_text = blank_text

    def to_html(self, params, UUID_glyphs):
        parameter = params.get(self.key, None)
        if parameter in [None, '']: 
            return [self.blank()]
        if not isinstance(parameter, dict): # non-magic variables
            return [magic_dct(parameter)]
        return [inline_handler(self, parameter, UUID_glyphs)]

    def blank(self):
        return magic_dct(self.blank_text, empty=True)

# returns a list of inline variables
class list_inline(inline):
    css_cls = ['inline-magic']

    def __init__(
        self, 
        key, 
        blank_text:str,
        ask_each_time = None, # never used
    ):
        super().__init__(key, blank_text, ask_each_time)

    def to_html(self, params, UUID_glyphs):
        inline_list = self.list_inline_handler(params,UUID_glyphs)
        inline_list.append(magic_dct('+'))
        return [{
            'class':['list-inline-magic'],
            'value':inline_list,
        }]

    def list_inline_handler(self, params, UUID_glyphs):
        parameter = params.get(self.key, None)
        if parameter in [None, '']: 
            return [self.blank()]
        elif isinstance(parameter, str): # non-magic variables
            return [magic_dct(parameter)]
        elif isinstance(parameter, dict):
            return [inline_handler(self, parameter, UUID_glyphs)]
        elif isinstance(parameter, list):
            return [inline.to_html(
                self,
                {self.key:sub_param}, # wrap param for handler
                UUID_glyphs,
            )[0] for sub_param in parameter]
        else:
            raise ValueError(f'Unexpected type of parameter: {type(parameter)}')
