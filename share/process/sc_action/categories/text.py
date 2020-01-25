from share.process.components._directory import *
from ..action import *

class _base(action):
    category = 'TEXT'
    glyph = 'Note.svg'

class gettext(_base):
    name = 'Text'
    result = 'Text'

class text_replace(_base):
    name = 'Replace Text'
    category = 'DOCUMENTS'
    title = [
        text('Replace'),
        inline(
            'WFReplaceTextFind',
            blank_text='Hello',
            ask_each_time='Text',
        ),
        text('with'),
        inline(
            'WFReplaceTextReplace',
            blank_text='World',
            ask_each_time='Text',
        ),
        text('in'),
        inline(
            'WFInput',
            blank_text='Text',
            ask_each_time='Text',
        ),
    ]
    lines = [
        line_toggle(
            'Case Sensitive',
            'WFReplaceTextCaseSensitive',
            default=True,
            ask_each_time='Ask Each Time',
        ),
        line_toggle(
            'Regular Expression',
            'WFReplaceTextRegularExpression',
            default=False,
            ask_each_time='Ask Each Time',
        ),
    ]
    result = 'Updated Text'

class text_combine(_base):
    name = 'Combine Text'
    title = [
        text('Combine'),
        magic(
            'text',
            blank_text='Text List',
            ask_each_time=None,
        ),
        text('with'),
        choose(
            'WFTextSeparator',
            ask_each_time='Separator',
            default='New Lines',
            options=[
                # fill in!
            ]
        ),
        inline(
            'WFTextCustomSeparator',
            blank_text='Text',
            ask_each_time='Text',
        ),
    ]
    result = 'Combined Text'
    def modify(self):
        if self.get_title('WFTextSeparator')['value'] != 'Custom':
            self.hide_title('WFTextCustomSeparator')

class text_split(_base):
    name = 'Split Text'
    title = [
        text('Split'),
        inline(
            'text',
            blank_text='Text',
            ask_each_time='Text',
        ),
        text('by'),
        choose(
            'WFTextSeparator',
            ask_each_time='Separator',
            default='New Lines',
            options=[
                # fill in!
            ]
        ),
        inline(
            'WFTextCustomSeparator',
            blank_text='Text',
            ask_each_time='Text',
        ),
    ]
    def modify(self):
        if self.get_title('WFTextSeparator')['value'] != 'Custom':
            self.hide_title('WFTextCustomSeparator')
    result = 'Split Text'

class text_changecase(_base):
    name = 'Change Case'
    title = [
        text('Change'),
        inline(
            'text',
            blank_text='Text',
            ask_each_time='Text',
        ),
        text('to'),
        choose(
            'WFCaseType',
            ask_each_time='Case',
            default='UPPERCASE',
            options=[
                #! fill in
            ]
        ),
    ]
    result = 'Updated Text'

class text_match(_base):
    name = 'Match Text'
    title = [
        text('Match'),
        inline(
            'WFMatchTextPattern',
            blank_text='Pattern',
            ask_each_time='Text',
        ),
        text('in'),
        inline(
            'text',
            blank_text='Text',
            ask_each_time='Text',
        ),
    ]
    lines = [
        line_toggle(
            'Case Sensitive',
            'WFMatchTextCaseSensitive',
            default=True,
            ask_each_time='Ask Each Time',
        ),
    ]
    result = 'Matches'

class text_match_getgroup(_base):
    name = 'Get Group from Matched Text'
    title = [
        text('Get'),
        choose(
            'WFGetGroupType',
            ask_each_time='Ask Each Time',
            default='Group At Index',
            options=[
                # ?
            ]
        ),
        number(
            'WFGroupIndex',
            default='1',
            blank_text=None,
            ask_each_time='Group Index',
        ),
        text('in'),
        magic(
            'matches',
            blank_text='Matches',
            ask_each_time='Ask Each Time',
        ),
    ]
    result = 'Text'
    def modify(self):
        if True: # fix this
            self.hide_title('WFGroupIndex')