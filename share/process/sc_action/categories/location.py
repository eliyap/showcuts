from ..action import *

class _base(action):
    category = 'LOCATION'
    glyph = 'Location.svg'

class getcurrentlocation(_base):
    result = 'Current Location'

class location(_base):
    result = 'Location'

class _weather_base(action):
    category = 'LOCATION'
    glyph = 'system/Weather.png'

class weather_currentconditions(_weather_base):
    result = '___'

class weather_forecast(_weather_base):
    result = '___'