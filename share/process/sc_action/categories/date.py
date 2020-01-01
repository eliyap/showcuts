from ..action import *

class _base(action):
    category = 'CALENDAR'
    glyph = 'Date.svg'

class date(_base):
    category = 'DATE'
    result = 'Date'

class format_date(_base):
    result = 'Formatted Date'

class adjustdate(_base):
    result = 'Adjusted Date'

class detect_date(_base):
    result = 'Dates'

class gettimebetweendates(_base):
    result = 'Time Between Dates'