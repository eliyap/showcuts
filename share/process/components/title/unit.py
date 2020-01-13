from ..magic_helpers import *
from .choose import choose
from share.process.lookups._directory import measurement_units

class unit(choose):
    '''Field that offers a list of valid units, with a default pre-selected.

    In Shortcuts, this field accepts:
       * one of the offered ``options``.
       * a magic variable, and Ask Each Time, may or may not be valid
    '''

    def __init__(
        self, 
        key, 
        ask_each_time, 
        default:str,
        options:[str],
    ):
        super().__init__(
            key=key,
            ask_each_time=ask_each_time,
            default=default,
            options=options,
        )
        

    @AddField('unit')
    def to_html(self, params, UUID_glyphs):
        # try to get default and options
        try:
            unit_type = params[self.key]['WFNSUnitType']
            self.default = measurement_units[unit_type]['default']
            self.options = measurement_units[unit_type]['units']
            self.attrs.update(dict(default=self.default, options=self.options))
        except KeyError:
            pass

        parameter = params.get(self.key, None)
        if parameter == '' or parameter == None: 
            return [self.blank()]
        elif not isinstance(parameter, dict): # non-magic variables
            return [magic_dct(parameter, attrs=self.attrs)]
        else:
            if 'WFSerializationType' in parameter: # classic magic var
                return [classify_magic(
                    value = parameter['Value'],
                    var_type = parameter['Value']['Type'],
                    ask_each_time = self.ask_each_time,
                    UUID_glyphs = UUID_glyphs,
                    attrs=self.attrs,
                )]
            elif 'WFNSUnitType' in parameter: # unit magic var
                return self.unit_magic(parameter)
            else:
                raise ValueError(f'Unexpected parameter {parameter}')
    
    def unit_magic(self, parameter:dict):
        return [magic_dct(parameter['WFNSUnitSymbol'], attrs=self.attrs)]

class long_unit(unit):
    def unit_magic(self, parameter):
        _type = parameter['WFNSUnitType']
        _symbol = parameter['WFNSUnitSymbol']
        if _type == 'Type': # Ask Each Time:
            return [magic_dct('Unit', attrs=self.attrs)] # placeholder
        return [magic_dct(measurement_units[_type]['units'][_symbol], attrs=self.attrs)]