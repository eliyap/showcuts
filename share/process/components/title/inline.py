from copy import deepcopy
from showcuts.local_settings import DEBUG

from .._directory import text
from ..magic_helpers import *
from ..base_magic import base_magic

# Inline Field:
# magic field, accepts arbitrary text with magic variables mixed in

def inline_handler(
    self, 
    parameter:dict, 
    UUID_glyphs,
    ask_each_time:str='Text',
) -> dict:
    '''Decomposes inline variables into text and magic variables, wrapped in an appropriate class.

    When represented as JSON, inline variable strings have the following structure:

       * a ``string`` value
          This is the string as shown in Shortcuts, 
          with the variables replaced by ``\\uFFFC``, 
          the `Unicode OBJECT REPLACEMENT CHARACTER <https://www.fileformat.info/info/unicode/char/fffc/index.htm>`_.
       * a mapping from magic variables' ``{position, length}`` to their value, in ``attachmentsByRange``
          * e.g. ``'{0,1}: <magic variable>`` represents a magic variable at the start of the string, i.e. position 0 and length 1.
          * all magic variables (that I have seen) have length 1, but the method allows for longer objects.
       
    **Side Note**: the recorded data type(`WFSerializationType`) is `WFTextTokenString`.
    '''

    inline_dct = parameter['Value']
    inline_element = {
        'class':deepcopy(self.__class__.css_cls),
        'value':[],
        'attrs':self.attrs,
    }
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
                ask_each_time=ask_each_time,
                UUID_glyphs=UUID_glyphs,
                attrs={},
            )

        # process remaining chars into text elems
        charray = '' # char array
        for elem in f_string:
            if isinstance(elem, dict):
                inline_element['value'] += [
                    text(charray).to_html()[0], # invoke to_html to get dict
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
    '''Field that accepts text mixed with magic variables.

    In Shortcuts, this accepts:

       * text with no newlines
       * magic variables mixed into text (like Python f-strings)
       * there may only be 1 "Ask Each Time" variable
    
    '''
    
    #: List of CSS classes to style the element.
    css_cls = ['inline-magic']

    def __init__(
        self, 
        key, 
        blank_text:str,
        ask_each_time = None, # never used
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
        if not isinstance(parameter, dict): # non-magic variables
            return [magic_dct(parameter, attrs=self.attrs)]
        return [inline_handler(
            self, 
            parameter, 
            UUID_glyphs, 
            ask_each_time=self.ask_each_time
        )]

    def blank(self):
        return magic_dct(
            self.blank_text,
            attrs=self.attrs, 
            empty=True
        )

# returns a list of inline variables
class list_inline(inline):
    '''Field that accepts a number of inline variables.

    In Shortcuts, this accepts a list of inline variables, not just one.

    This field is particular to Safari actions such as `Reading List`, as far as I know.
    '''
    
    #: List of CSS classes to style the element.
    css_cls = ['inline-magic']

    def __init__(
        self, 
        key, 
        blank_text:str,
        ask_each_time = None, # never used
    ):
        super().__init__(key, blank_text, ask_each_time)

    @AddField('inline')
    def to_html(self, params, UUID_glyphs):
        inline_list = self.list_inline_handler(params,UUID_glyphs)
        inline_list.append(magic_dct('+',attrs={}))
        return [{
            'class':['list-inline-magic'],
            'value':inline_list,
        }]

    def list_inline_handler(self, params, UUID_glyphs):
        '''Decomposes one (or more) inline variables into magic dicts.'''

        parameter = params.get(self.key, None)
        if parameter in [None, '']: 
            return [self.blank()]
        elif isinstance(parameter, str): # non-magic variables
            return [magic_dct(parameter, attrs=self.attrs)]
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
