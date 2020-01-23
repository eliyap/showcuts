from ..magic_helpers import *
from ..base_magic import base_magic

class location(base_magic):
    '''Location Field.

    In Shortcuts, this can accept:

       * Current Location
       * specified Maps location
       * results from other actions
       * blank (nothing)
       * Ask Each Time
    
    '''

    def __init__(
        self, 
        key:str, 
        blank_text:str, # lighter text when the variable is cleared
        ask_each_time:str, 
        default:str, # can default to a preset location (usually implies blank not allowed)
    ):
        super().__init__(key, ask_each_time, attrs=dict(
            key=key,
            ask_each_time=ask_each_time,
            blank_text=blank_text,
            default=default,
        ))
        self.blank_text = blank_text
        self.default = default


    @AddField('location')
    def to_html(self, params, UUID_glyphs):
        parameter = params.get(self.key, None)
        if parameter == None or parameter == '':
            return [self.blank()]
        # no non-magic variables, I think?
        #TODO: check for other ways of specifying location?
        try:
            address_dict = parameter['placemark']['addressDictionary']
            for k in ['Name','Street','City','State','Country']:
                if k in address_dict:
                    return [magic_dct(value=address_dict[k], attrs=self.attrs, empty=False)]
        except KeyError:
            pass
        
        try:
            if parameter['isCurrentLocation'] == True:
                return [magic_dct(value='Current Location', attrs=self.attrs, empty=False)]
        except KeyError:
            pass
        
        return [classify_magic(
            value = parameter['Value'],
            var_type = parameter['Value']['Type'],
            ask_each_time = self.ask_each_time,
            UUID_glyphs = UUID_glyphs,
            attrs=self.attrs,
        )]

    def blank(self):
        if self.default:
            return magic_dct(
                self.default, 
                attrs=self.attrs,
                empty=False,
            )
        return magic_dct(
            self.blank_text, 
            attrs=self.attrs,
            empty=True,
        )

    