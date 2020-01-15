from share.process.components._directory import *
from ..action import *
from ..action import *

class _base(action):
    category = 'CALENDAR'
    glyph = 'Date.svg'

class date(_base):
    name = 'Date'
    category = 'DATE'
    title = [
        choose(
            'WFDateActionMode',
            ask_each_time='Ask Each Time',
            default='Current Date',
            options=[
                'Current Date',
                'Specified Date',
            ],
        ),
        inline(
            'WFDateActionDate',
            blank_text='29 June 2007',
            ask_each_time='Date',
        ),
    ]
    lines = [
        line_choose(
            'Use',
            'WFDateActionMode',
            ask_each_time='Ask Each Time',
            default='Current Date',
            options=[
                'Current Date',
                'Specified Date',
            ],
        ),
    ]
    def modify(self):
        {
            'Current Date': lambda: [
                self.hide_title('WFDateActionDate'),
                self.hide_line('WFDateActionMode'),
            ],
            'Specified Date': lambda: self.hide_line('WFDateActionMode'),
        }.get(
            self.get_title('WFDateActionMode')['value'],
            lambda:[ # magic variable
                self.hide_title('WFDateActionMode'),
                self.hide_title('WFDateActionDate'),
            ],
        )()
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