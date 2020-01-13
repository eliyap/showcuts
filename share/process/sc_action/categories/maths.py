from share.process.components._directory import *
from ..action import *
from share.process.lookups._directory import measurement_units
'''
# A Note on the Tree
- longer (more specifc labels must go first)
- in particular, '' MUST go last
'''


class _base(action):
    category = 'MATHS'
    glyph = 'Math.svg'

class number_(_base):
    name = 'number'
    category = 'NUMBER'
    title = [
        number(
            'WFNumberActionNumber',
            default=None,
            blank_text='42',
            ask_each_time='Number',
        ),
    ]
    result = 'Number'

class random(_base):
    name = 'Random Number'
    title = [
        text('Random number between'),
        number(
            'WFRandomNumberMinimum',
            default=None,
            blank_text='Minimum',
            ask_each_time='Minimum',
        ),
        text('and'),
        number(
            'WFRandomNumberMaximum',
            default=None,
            blank_text='Maximum',
            ask_each_time='Maximum',
        ),
    ]
    result = 'Random Number'

class math(_base):
    name = 'Calculate'
    result = 'Calculation Result'

class statistics(_base):
    name = 'Calculate Statistics'
    title = [
        text('Calculate the'),
        choose(
            'WFStatisticsOperation',
            ask_each_time='Operation',
            default='Average',
            options=[
                'Average',
                'Minimum',
                'Maximum',
                'Sum',
                'Median',
                'Mode',
                'Range',
                'Standard Deviation',
            ],
        ),
        text('of'),
        magic(
            'Input',
            blank_text='Input',
            ask_each_time=None,
        ),
    ]
    result = '___' #placeholder
    def modify(self): # set the output to the correct statistic
        self.result = self.get_title('WFStatisticsOperation')['value']

class round_(_base):
    name = 'Round Number'
    title = [
        text('Round'),
        number(
            'WFInput',
            default=None,
            blank_text='Number',
            ask_each_time='Number',
        ),
        text('to'),
        choose(
            'WFRoundTo',
            ask_each_time='Value',
            default='Ones Place',
            options=[
                'Millions',
                'Hundred Thousands',
                'Ten Thousands',
                'Thousands',
                'Hundreds Place',
                'Tens Place',
                'Ones Place',
                'Tenths',
                'Hundreths',
                'Thousandths',
                'Ten Thousandths',
                'Hundred Thousandths',
                'Millionths',
                'Ten Millionths',
                'Hundred Millionths',
                'Billionths',
                '10 ^',
            ],
        ),
        whole_number(
            'TenToThePowerOf',
            default='0',
            blank_text='', # truly blank
            ask_each_time='Ask Each Time',
        ),
    ]
    lines = [
        line_choose(
            'Mode',
            'WFRoundMode',
            ask_each_time='Ask Each Time',
            default='Normal',
            options=[
                'Normal',
                'Always Round Up',
                'Always Round Down',
            ],
        ),
    ]

    def modify(self):
        if self.title[3]['value'] != '10 ^':
            self.hide_title('TenToThePowerOf')
    result = 'Rounded Number'

class format_filesize(_base):
    name = 'Format File Size'
    title = [
        text('Format'),
        whole_number(
            'WFFileSize',
            default=None,
            blank_text='File Size',
            ask_each_time='File Size',
        ),
        text('into'),
        choose(
            'WFFileSizeFormat',
            ask_each_time='Format',
            default='Closest Unit',
            options=[
                'Closest Unit',
                'Bytes',
                'Kilobytes',
                'Megabytes',
                'Gigabytes',
                'Terabytes',
                'Petabytes',
                'Exabytes',
                'Zettabytes',
                'Yottabytes',
            ],
        ),
    ]
    lines = [
        line_toggle(
            'Include Units',
            'WFFileSizeIncludeUnits',
            default=True,
            ask_each_time='Ask Each Time',
        )
    ]
    result = 'Formatted File Size'

    def modify(self):
        if self.title[3]['value'] != 'Closest Unit':
            self.hide_line('Include Units')

class format_number(_base):
    name = 'Format Number'
    title = [
        text('Format'),
        number(
            'WFNumber',
            default=None,
            blank_text='Number',
            ask_each_time='Number',
        ),
        text('to'),
        counter(
            'WFNumberFormatDecimalPlaces',
            item='decimal place',
            ask_each_time='Decimal Places',
            default=2,
        ),
    ]
    result = 'Formatted Number'

class measurement_convert(_base):
    name = 'Convert Measurement'
    category = 'MEASUREMENT'
    title = [
        text('Convert'),
        magic(
            'WFInput',
            blank_text='Measurement',
            ask_each_time=None,
        ),
        text('into'),
        choose(
            'WFMeasurementUnitType',
            ask_each_time='Type',
            default='Length',
            options=list(measurement_units.keys())
        ),
        text('in'),
        long_unit(
            'WFMeasurementUnit',
            ask_each_time='Unit',
            default='___',
            options=[],
        )
    ]
    def modify(self):
        '''Fix unit inconsistency.
        If unit is missing / inconsistent with selected measurement, force consistency.
        Then re-to_html.
        '''
        unit_type = self.get_title(key='WFMeasurementUnitType')['value']
        unit_dct = self.parameters.get('WFMeasurementUnit',{})
        if 'WFSerializationType' in unit_dct: # classic magic var
            if self.get_title('WFMeasurementUnitType')['value'] == 'Type':
                self.hide_text('in')
                self.hide_title('WFMeasurementUnit')
            return


        #: if not a classic magic var, check if the units line up
        #: if the units do not line up, override.
        if unit_type != self.parameters.get('WFMeasurementUnit',{}).get('WFNSUnitType',None):
            self.parameters['WFMeasurementUnit'] = {
                "WFNSUnitSymbol":measurement_units.get(unit_type,{}).get('default',''),
                "WFNSUnitType": unit_type,
            }
        self.title[5] = long_unit(
            'WFMeasurementUnit',
            ask_each_time='Unit',
            default='___',
            options=[],
        ).to_html(self.parameters, UUID_glyphs={})[0]

    result = 'Converted Measurement'

class measurement_create(_base):
    name = 'Measurement'

    category = 'MEASUREMENT'
    title = [
        choose(
            'WFMeasurementUnitType',
            ask_each_time='Type',
            default='Length',
            options=measurement_units.keys(),
        ),
        
    ]
    result = 'Measurement'
