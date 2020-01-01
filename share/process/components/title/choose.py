from ..magic_helpers import *
from ..base_magic import base_magic

# Magic Variables
# the basic magic variable field can hold:
#  - results from other actions
#  - "global" variables (Clipboard, Current Date, Shortcut Input)
#  - blanks

class choose(base_magic):
    def __init__(
        self, 
        key, 
        ask_each_time, 
        default:str,
        options:[str],
        *_,
        **__,
    ):
        super().__init__(key, ask_each_time)
        self.default = default
        self.options = options

    def blank(self):
        return magic_dct(self.default, empty=False)