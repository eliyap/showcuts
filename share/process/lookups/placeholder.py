import share.process.sc_action.action as action
infoless = {'glyph': 'Missing.svg', 'category': 'MISSING'}

def error_action():
    return {
        'title': [{'value':'Error Loading Action','class':'error'}],
        'line': [],
        'glyph': '',#deliberately blank
        'category': '',
        'indent': '',
    }

class NOT_IMPLEMENTED_ACTION(action.action):
    def modify(self):
        self.title = [{
            'value':'Action Under Construction',
            'class':'not-implemented',
            'attrs':{
                'key':None,
            },
        }]
        self.glyph = 'assets/cat/Missing.svg'
        self.category = 'MISSING'

def not_implemented_options():
    return {
        'label':'',
        'class':'not-implemented',
        'value':'Options Under Construction',
    }