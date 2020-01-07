from ..action import *

class _base(action):
    category = 'CALENDAR'
    glyph = 'Date.svg'

class date(_base):
    name = 'Date'
    category = 'DATE'
    result = 'Date'

class format_date(_base):
    name = 'Format Date'
    result = 'Formatted Date'

class adjustdate(_base):
    name = 'Adjust Date'
    result = 'Adjusted Date'

class detect_date(_base):
    name = 'Get Dates from Input'
    result = 'Dates'

class gettimebetweendates(_base):
    name = 'Get Time Between Dates'
    result = 'Time Between Dates'