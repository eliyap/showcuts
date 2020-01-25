from ..action import action, control
from share.process.components._directory import *

class _base(action):
    category = 'WEB'
    glyph = 'link.svg'

class openxcallbackurl(_base):
    name = 'Open X-Callback URL'
    category = 'SCRIPTING'
    result = 'X-Callback Result'

class urlencode(_base):
    name = 'URL Encode'
    category = 'SCRIPTING'
    result = 'URL Encoded Text'

class url_expand(_base):
    name = 'Expand URL'
    title = [
        text('Expand'),
        inline(
            'URL',
            blank_text='URL',
            ask_each_time='Ask Each Time',
        ),
    ]
    result = 'Expanded URL'

class geturlcomponent(_base):
    name = 'Get Component of URL'
    category = 'URL'
    title_elem = [
        text('Get'),
        choose(
            'WFURLComponents',
            ask_each_time='Ask Each Time',
            default='Scheme',
            options=[
                #?
            ],
        ),
        text('from'),
        inline(
            'URL',
            blank_text='WFURL',
            ask_each_time='Ask Each Time',
        ),
    ]
    result = 'Component of URL'

class detect_link(_base):
    name = 'Get URLs from Input'
    result = 'URLs'

class url(_base):
    name = 'URL'
    category = 'URL'
    title = [
        inline(
            'WFURLActionURL',
            blank_text='apple.com',
            ask_each_time='Ask Each Time',
        ),
    ]
    result = 'URL'

# below not DOCUMENTED
