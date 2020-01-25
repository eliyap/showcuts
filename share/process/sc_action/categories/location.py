from share.process.components._directory import *
from ..action import *

class _base(action):
    category = 'LOCATION'
    glyph = 'Location.svg'

# below this line NOT DOCUMENTED

class getcurrentlocation(_base):
    name = 'Get Current Location'
    title = [
        text('Get current location'),
    ]
    result = 'Current Location'

class _location(_base): # location is a component name
    name = 'Location'
    title = [
        location(
            'WFLocation',
            blank_text='Location',
            ask_each_time='Ask Each Time',
            default=None,
        ),
    ]
    result = 'Location'

class _weather_base(action):
    category = 'LOCATION'
    glyph = 'system/Weather.png'

class weather_currentconditions(_weather_base):
    name = 'Get Current Weather'
    result = '___'

class weather_forecast(_weather_base):
    name = 'Get Weather Forecast'
    result = '___'