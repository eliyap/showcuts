from ..action import action, control
from share.process.components._directory import *

class _base(action):
    category = 'SCRIPTING'
    glyph = 'Settings.svg'

class exit_(_base): # exit is a protected word
    name = 'Exit Shortcut'
    title = [
        text('Exit shortcut with'),
        magic(
            'WFResult',
            blank_text='Result',
            ask_each_time=None,
        ),
    ]

class openapp(_base):
    name = 'Open App'
    glyph = 'App.svg'

class conditional(_base):
    name = 'If'
    result = 'If Result'

class choosefrommenu(_base):
    name = 'Choose from Menu'
    result = 'Menu Result'

class repeat_count(_base, control):
    name = 'Repeat'
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
    name = 'Repeat with Each'
    result = 'Repeat Results'
    
    def modify(self):
        super().mod_indent()

class delay(_base):
    name = 'Wait'

class waittoreturn(_base):
    name = 'Wait to Return'

class getbatterylevel(_base):
    name = 'Get Battery Level'
    glyph = 'Battery.svg'
    result = 'Battery Level'

class gettypeaction(_base):
    name = '___'
    result = 'File of Type'

class getdevicedetails(_base):
    name = 'Get Device Details'
    result = 'Device Name'

class setbrightness(_base):
    name = 'Set Brightness'
    glyph = 'Brightness.svg'

class flashlight(_base):
    name = 'Set Torch'
    glyph = 'Flashlight.svg'

class dictionary(_base):
    name = 'Dictionary'
    category = 'DICTIONARY'
    result = 'Dictionary'

class detect_dictionary(_base):
    name = 'Get Dictionary from Input'
    result = 'Dictionary'

class detect_number(_base):
    name = '___'
    glyph = 'Math.svg'
    result = 'Numbers'

class getitemname(_base):
    name = '___'
    result = 'Name'

class setitemname(_base):
    name = '___'
    result = 'Renamed Item'

class getitemtype(_base):
    name = '___'
    result = 'Type'

class getvalueforkey(_base):
    name = 'Get Dictionary Value'
    result = 'Dictionary Value'

class setvalueforkey(_base):
    name = 'Set Dictionary Value'
    result = 'Dictionary'

class base64encode(_base):
    name = 'Base64 Encode'
    result = 'Base64 Encoded'

class hash_(_base): # hash is a protected word
    name = 'Generate Hash'
    result = 'Hash'

class choosefromlist(_base):
    name = 'Choose from List'
    result = 'Chosen Item'

class getitemfromlist(_base):
    name = 'Get Item from List'
    result = 'Item from List'

class list_(_base): # list is a protected word
    name = 'List'
    category = 'LIST'
    result = 'List'

class getipaddress(_base):
    name = 'Get Current IP Address'
    glyph = 'Web.svg'
    result = 'Current IP Address'

class getwifi(_base):
    name = 'Get Network Details'
    glyph = 'Web.svg'
    result = 'Network Details'

class dnd_set(_base):
    name = 'Set Do Not Disturb'
    glyph = 'DND.svg'

class airplanemode_set(_base):
    name = 'Set Airplane Mode'
    glyph = 'Airplane.svg'

class bluetooth_set(_base):
    name = 'Set Bluetooth'
    glyph = 'Bluetooth.svg'

class cellulardata_set(_base):
    name = 'Set Mobile Data'
    glyph = 'Mobile.svg'

class wifi_set(_base):
    name = 'Set Wi-Fi'
    glyph = 'WiFi.svg'
    category = 'WI-FI'

class lowpowermode_set(_base):
    name = 'Set Low Power Mode'
    glyph = 'Battery.svg'

class nothing(_base):
    name = 'Nothing'
    category = 'NOTHING'

class count(_base):
    name = 'Count'
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
    name = 'Ask for Input'
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
    name = 'Play Sound'
    glyph = 'Volume.svg'

class alert(_base):
    name = 'Show Alert'

class showresult(_base):
    name = 'Show Result'

class vibrate(_base):
    name = 'Vibrate Device'
    glyph = 'Notification.svg'

class runsshscript(_base):
    name = 'Run Script Over SSH'
    result = 'Shell Script Result'

class handoff(_base):
    name = '___'
    glyph = 'Handoff.svg'

class viewresult(_base):
    name = '___'
    glyph = '__.svg' # CONTENT GRAPH SVG
