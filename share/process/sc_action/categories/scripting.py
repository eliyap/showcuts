from ..action import action, control
from share.process.components._directory import *

class _base(action):
    category = 'SCRIPTING'
    glyph = 'Settings.svg'

class exit_(_base): # exit is a protected word
    title = [
        text('Exit shortcut with'),
        magic(
            'WFResult',
            blank_text='Result',
            ask_each_time=None,
        ),
    ]

class openapp(_base):
    glyph = 'App.svg'

class conditional(_base):
    result = 'If Result'

class choosefrommenu(_base):
    result = 'Menu Result'

class repeat_count(_base, control):
    def inherit(self): # hijack inherit() to set the instance title
        super().inherit()
        self.title = {
            0: [
                text('Repeat'),
                counter(
                    'WFRepeatCount',
                    item='time',
                    ask_each_time='Repetitions',
                    default=1,
                ),
            ],
            2: [
                text('End Repeat'),
            ],
        }[super().flow_mode()]
    
    result = 'Repeat Results'

    def modify(self):
        super().mod_indent()
        

class repeat_each(_base):
    result = 'Repeat Results'
    
    def modify(self):
        super().mod_indent()

class delay(_base):
    pass

class waittoreturn(_base):
    pass

class getbatterylevel(_base):
    glyph = 'Battery.svg'
    result = 'Battery Level'

class gettypeaction(_base):
    result = 'File of Type'

class getdevicedetails(_base):
    result = 'Device Name'

class setbrightness(_base):
    glyph = 'Brightness.svg'

class flashlight(_base):
    glyph = 'Flashlight.svg'

class dictionary(_base):
    category = 'DICTIONARY'
    result = 'Dictionary'

class detect_dictionary(_base):
    result = 'Dictionary'

class detect_number(_base):
    glyph = 'Math.svg'
    result = 'Numbers'

class getitemname(_base):
    result = 'Name'

class setitemname(_base):
    result = 'Renamed Item'

class getitemtype(_base):
    result = 'Type'

class getvalueforkey(_base):
    result = 'Dictionary Value'

class setvalueforkey(_base):
    result = 'Dictionary'

class base64encode(_base):
    result = 'Base64 Encoded'

class hash_(_base): # hash is a protected word
    result = 'Hash'

class choosefromlist(_base):
    result = 'Chosen Item'

class getitemfromlist(_base):
    result = 'Item from List'

class list(_base):
    category = 'LIST'
    result = 'List'

class getipaddress(_base):
    glyph = 'Web.svg'
    result = 'Current IP Address'

class getwifi(_base):
    glyph = 'Web.svg'
    result = 'Network Details'

class dnd_set(_base):
    glyph = 'DND.svg'

class airplanemode_set(_base):
    glyph = 'Airplane.svg'

class bluetooth_set(_base):
    glyph = 'Bluetooth.svg'

class cellulardata_set(_base):
    glyph = 'Mobile.svg'

class wifi_set(_base):
    glyph = 'WiFi.svg'
    category = 'WI-FI'

class lowpowermode_set(_base):
    glyph = 'Battery.svg'

class nothing(_base):
    category = 'NOTHING'

class count(_base):
    glyph = 'Math.svg'
    title = [
        text('Count'),
        choose(
            'WFCountType', 
            options = ['Items','Characters','Words','Sentences','Lines'],
            default = 'Lines',
            ask_each_time = 'Type',
        ),
        text('in'),
        magic('Input', blank_text='Input', ask_each_time = None),
    ]
    result = 'Count'

class ask(_base):
    title = [
        text('Ask'),
        inline('WFAskActionPrompt', blank_text = 'Question')
    ]
    lines = [
        line_choose(
            label='Input Type',
            key='WFInputType',
            options=['Text','Number','URL','Date','Time','Date and Time'],
            default='Text',
            ask_each_time=None,
        ),
        line_inline(
            label='Default Answer',
            key='WFAskActionDefaultAnswerNumber',
            blank_text='', # depends on input type!
        ),
    ]
    
    def modify(self): # set empty var to correct text
        default_answer = self.lines[1]
        if 'empty' in default_answer['class']:
            default_answer['value'][0]['value'] = self.lines[0]['value']
        
    result = 'Provided Input'

class playsound(_base):
    glyph = 'Volume.svg'

class alert(_base):
    pass

class showresult(_base):
    pass

class vibrate(_base):
    glyph = 'Notification.svg'

class runsshscript(_base):
    result = 'Shell Script Result'

class openxcallbackurl(_base):
    glyph = 'Link.svg'
    result = 'X-Callback Result'

class urlencode(_base):
    glyph = 'Link.svg'
    result = 'URL Encoded Text'

class handoff(_base):
    glyph = 'Handoff.svg'

class viewresult(_base):
    glyph = '__.svg' # CONTENT GRAPH SVG
