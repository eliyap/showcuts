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
    title = [
        choose(
            'WFAdjustOperation',
            ask_each_time=None,
            default='Add',
            options=[
                'Add',
                'Subtract',
                'Get Start of Minute',
                'Get Start of Hour',
                'Get Start of Day',
                'Get Start of Week',
                'Get Start of Month',
                'Get Start of Year',
            ],
        ),
        # quantity(
        #     'WFDuration',
        #     ask_each_time='Ask Each Time',
        #     blank_text='0',
        # ),
        text('to'),
        inline(
            'WFDate',
            blank_text='Date',
            ask_each_time='Date',
        ),
    ]
    result = 'Adjusted Date'

class detect_date(_base):
    name = 'Get Dates from Input'
    result = 'Dates'

class gettimebetweendates(_base):
    name = 'Get Time Between Dates'
    title = [
        text('Get time between'),
        inline(
            'WFTimeUntilFromDate',
            blank_text='First Date',
            ask_each_time='Date',
        ), # has a default value of current date!
        text('and'),
        inline(
            'WFInput',
            blank_text='Second Date',
            ask_each_time='Date',
        ),
        text('in'),
        choose(
            'WFTimeUntilUnit',
            ask_each_time='In',
            default='Minutes',
            options=[
                'Total Time',
                'Seconds',
                'Minutes',
                'Hours',
                'Days',
                'Weeks',
                'Months',
                'Years',
            ],
        ),
    ]
    result = 'Time Between Dates'