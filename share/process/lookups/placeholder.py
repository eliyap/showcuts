infoless = {'glyph': 'Missing.svg', 'category': 'MISSING'}

def error_action():
    return {
        'title': [{'value':'Error Loading Action','class':'error'}],
        'line': [],
        'glyph': '',#deliberately blank
        'category': '',
        'indent': '',
    }

def not_implemented_action(category:str = '', indent_level:int = 0, sub_name:str = 'Action', glyph:str = ''):
    return {
        'title': [{'value':f'{sub_name} Under Construction','class':'not-implemented'}],
        'line': [],
        'glyph': f'assets/cat/{glyph}',
        'category': category,
        'indent': indent_level if indent_level else '',
        'result':None,
    }

def not_implemented_options():
    return {
        'label':'',
        'class':'not-implemented',
        'value':'Options Under Construction',
    }