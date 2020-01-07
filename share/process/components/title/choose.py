from ..magic_helpers import *
from ..base_magic import base_magic

class choose(base_magic):
    '''Field that offers a list of valid choices, with a default pre-selected.

    In Shortcuts, this field accepts:
       * one of the offered ``options``.
       * a magic variable, and Ask Each Time, may or may not be valid
    
    Some fields simply prompt the user to "Choose a variable..." with no other options.

    :TODO: account for "Choose a variable..." case.

    '''

    def __init__(
        self, 
        key, 
        ask_each_time, 
        default:str,
        options:[str],
        *_,
        **__,
    ):
        super().__init__(key, ask_each_time, attrs=dict(
            key=key,
            ask_each_time=ask_each_time,
            default=default,
            options=options,
        ))
        self.default = default
        self.options = options

    @AddField('choose')
    def to_html(self, params, UUID_glyphs):
        return super().to_html(params, UUID_glyphs)

    def blank(self):
        return magic_dct(
            self.default,
            attrs=self.attrs, 
            empty=False,
        )