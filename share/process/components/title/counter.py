from ..magic_helpers import *
from ..base_magic import base_magic

# Magic Variables
# the basic magic variable field can hold:
#  - results from other actions
#  - "global" variables (Clipboard, Current Date, Shortcut Input)
#  - blanks

class counter(base_magic):
    def __init__(
        self, 
        key,
        item:str,
        ask_each_time, 
        default:int,
        *_,
        **__,
    ):
        super().__init__(key, ask_each_time)
        self.default = default
        self.item = item
    
    def to_html(self, params, UUID_glyphs:dict):
        magic_elem = super().to_html(params, UUID_glyphs)
        return counter_handler(magic_elem, self.item)
    
    def blank(self):
        return magic_dct(self.default, empty=False)

def counter_handler(magic_elem, item:str):
    try: # see if value can be coerced to Int
        count = int(float(magic_elem[0]['value']))
        magic_elem[0]['value'] = f'{count} {item}{"" if count==1 else "s"}'
    except ValueError:
        pass
    return magic_elem