from share.process.components._directory import *
from ..action import *
'''
# A Note on the Tree
- longer (more specifc labels must go first)
- in particular, '' MUST go last
'''


class _base(action):
    category = 'MATHS'
    glyph = 'Math.svg'

class number_(_base):
    category = 'NUMBER'
    title = [
        number(
            'WFNumberActionNumber',
            blank_text='42',
            ask_each_time='Number',
        ),
    ]
    result = 'Number'

class random(_base):
    title = [
        text('Random number between'),
        number(
            'WFRandomNumberMinimum',
            blank_text='Minimum',
            ask_each_time='Minimum',
        ),
        text('and'),
        number(
            'WFRandomNumberMaximum',
            blank_text='Maximum',
            ask_each_time='Maximum',
        ),
    ]
    result = 'Random Number'

class math(_base):
    result = 'Calculation Result'

class statistics(_base):
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
        self.result = self.title[1]['value']

class round_(_base):
    title = [
        text('Round'),
        number(
            'WFInput',
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
            self.title[4]['class'].append('hidden')
    result = 'Rounded Number'

class format_filesize(_base):
    title = [
        text('Format'),
        whole_number(
            'WFFileSize',
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
    title = [
        text('Format'),
        number(
            'WFNumber',
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
    category = 'MEASUREMENT'
    result = 'Converted Measurement'

class measurement_create(_base):
    units = {
        'Acceleration':{
            'units':[
                'g-force',
                'm/s²', # metres per second squared (meters?)
            ],
            'default':'m/s²',
        },
        'Angle':{
            'units':[
                'arcmin', # arcminutes
                'arcsec', # arcseconds
                'deg', # degrees
                'grad',
                'rad', # radians
                'rev', # revolution
            ],
            'default':'deg',
        },
        'Area':{
            'units':[
                'a',
                'acre', # acres
                'cm²', # square centimetres
                'ft²', # square feet
                'hectare', # hectares
                'in²', # square inches
                'km²', # square kilometres
                'm²', # square metres, actually displayed as 'metres²'
                'mi²', # square square miles
                'ft²', # square feet
                'Mm²',
                'mm²',
                'nm²',
                'square yards',
                'μm²',
            ],
            'default':'m²',
        },
        'Concentration Mass':{
            'units':[
                'g/L',
                'mg/dl', # milligrams per decilitre
                'μg/m³',
            ],
            'default':'mg/dl',
        },
        'Dispersion':{
            'units':[
                'ppm', # parts per million
            ],
            'default':'ppm',
        },
        'Duration':{
            'units':[
                'hour', # hours
                'min', # minutes
                'msec', # milliseconds
                'ns', # nanoseconds
                'ps',
                'sec', # seconds
                'μsec', # microseconds
            ],
            'default':'min',
        },
        'Electric Charge':{
            'units':[
                'Ah',
                'C',
                'kAh',
                'mAh',
                'MAh',
                'μAh',
            ],
            'default':'Ah',
        },
        'Electric Current':{
            'units':[
                'amp', # amperes,
                'kA',
                'MA',
                'mA', # milliamperes
                'μA',
            ],
            'default':'amp',
        },
        'Electric Potential Difference':{
            'units':[
                'kV',
                'MV',
                'mV',
                'volt', # volts
                'μV',
            ],
            'default':'volt',
        },
        'Electric Resistance':{
            'units':[
                'kΩ',
                'MΩ',
                'mΩ',
                'μΩ',
                'ohm', # ohms
            ],
            'default':'ohm',
        },
        'Energy':{
            'units':[
                'cal', # calories
                'joule', # joules
                'kcal', # kilocalories
                'kJ', # kilojoules
                'kWh', # kilowatt-hours
            ],
            'default':'joule',
        },
        'Frequency':{
            'units':[
                'fps',
                'GHz', # gigahertz
                'Hz', # hertz
                'kHz', # kilohertz
                'mHz',
                'MHz', # megahertz
                'nHz',
                'THz',
                'μHz',
            ],
            'default':'Hz',
        },
        'Fuel Efficiency':{
            'units':[
                'l/100km', # litres per 100 kilometres
                'mpg US', # miles per US gallon
            ],
            'default':'l/100km',
        },
        'Illuminance':{
            'units':[
                'lux',
            ],
            'default':'lux',
        },
        'Information Storage':{
            'units':[
                'bytes',
                'EB',
                'GB',
                'KB',
                'MB',
                'PB',
                'TB',
                'YB',
                'ZB',
            ],
            'default':'MB',
        },
        'Length':{
            'units':[
                'cm', # centimetres
                'dam',
                'dm', # decimetre
                'ft', # feet
                'fathom', # fathoms
                'furlong', # furlongs
                'hm',
                'in', # inches
                'km', # kilometres
                'ly', # light years
                'm', # metres
                'mi', # miles
                'mm', # millimetres
                'Mm',
                'nm', # nanometres
                'nmi', # nautical miles
                'parsec', # parsecs
                'pm', # picometres
                'smi', # mile-scandinavian
                'au', # astronomical units
                'yd', # yards
                'μm', # micrometre
            ],
            'default':'m',
        },
        'Mass':{
            'units':[
                'cg',
                'carat', # carats
                'dg',
                'gram', # grams
                'kg', # kilograms
                'lb', # pounds
                'mg', # milligrams
                'ng',
                'oz', # ounces
                'oz t', # troy ounces
                'pg',
                'slug',
                'stone',
                't', # tonne
                'ton', # tons
                'μg', # micrograms
            ],
            'default':'gram',
        },
        'Power':{
            'units':[
                'fW',
                'GW', # gigawatts
                'hp', # horsepower
                'kW', # kilowatts
                'MW', # megawatts
                'mW', # milliwatts
                'nW',
                'pW',
                'TW',
                'watt', # watts
                'μW',
            ],
            'default':'watt',
        },
        'Pressure':{
            'units':[
                'bar',
                'GPa',
                'hPa', # hectopascals
                'inHg', # shown as '″Hg', 'inches of mercury'
                'kPa',
                'mbar', # millibars
                'mmHg', # millimetres of mercury
                'MPa',
                'N/m²',
            ],
            'default':'mbar',
        },
        'Speed':{
            'units':[
                'km/hr', # kilometres per hour
                'kn', # knots
                'm/s', # metres per second
                'mi/hr', # miles per hour
            ],
            'default':'km/hr',
        },
        'Temperature':{
            'units':[
                '°C', # degrees Celsius
                '°F', # degrees Fahrenheit
                'K', # Kelvin
            ],
            'default':'',
        },
        'Volume':{
            'units':[
                'acre ft', # acre-feet
                'bushel', # bushels
                'cl', # centilitres
                'cm³', # cubic centimetres
                'cup', # cups
                'dl', # decilitres
                'dm³',
                'fl oz', # fluid ounces
                'ft³', # cubic feet
                'gal', # gallons
                'in³', # cubic inches
                'kL',
                'km³', # cubic kilometres
                'litre', # litres
                'm³', # metres
                'mcup', # metric cups
                'mi³', # cubic miles
                'ml', # millilitres
                'Ml', # megalitres
                'mm³',
                'pt', # pints
                'qt', # quarts
                'tbsp', # tablespoons
                'tsp', # teaspoons
                'yd³', # cubic yards
            ],
            'default':'litre',
        },
    }

    category = 'MEASUREMENT'
    title = [
        choose(
            'WFMeasurementUnitType',
            ask_each_time='Type',
            default='Length',
            options=units.keys(),
        ),
        
    ]
    result = 'Measurement'
