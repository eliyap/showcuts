def value_dct(
    value: str,
    key:str,
    css_class: [str] = [],
    empty: bool = False,
):
    '''Wraps a given ``value`` in a dict for the django templater.
    
    :param css_class: list of CSS classes to be applied to the variable.

    :param empty: determines whether CSS class ``empty`` should be applied. ``empty`` greys out the value, indicating that it was left blank.
    '''
    if empty: css_class.append('empty')
    return {
        'class':css_class,
        'key':key,
        'value':value,
    }

def magic_dct(
    value: str, 
    key:str,
    empty: bool = False, 
    glyph:str = '', 
    UUID:str = None,
) -> dict:
    '''Wraps a given ``value`` in a magic-var dict for the django templater.
    
    :param glyph: icon to be displayed to the left of magic variables.

    :param UUID: UUID of the action that supplied the magic variable, if any.

    :param empty: determines whether CSS class ``empty`` should be applied. ``empty`` greys out the value, indicating that it was left blank.
    '''
    return {
        'class': ['magic'] + (['empty'] if empty else []),
        'value': value,
        'key':key,
        'glyph': f'assets/cat/{glyph}' if glyph else '',
        'UUID' : UUID,
    }

def error_magic():
    return magic_dct(value='<error>', empty=True, key='None')

def classify_magic(
    value: dict, 
    var_type: str, 
    key:str,
    ask_each_time: str = 'Ask Each Time',
    UUID_glyphs:dict = {},
) -> dict:
    '''Returns an appropriate magic variable dict.
    
    :param value: dict of information about the variable
    
    :param var_type: "Type" entry in ``value``, indicating whether the variable is:

       * Clipboard
       * Ask Each Time
       * Current Date
       * Shortcut Input (from Share sheet)
       * Output from other actions
       * A named variable (from `Set Variable` or `Add to Variable` actions)

    :param ask_each_time: The text used when `Ask Each Time` is selected as an option. 

    :param UUID_glyphs: Maps actions' output UUIDs to their glyphs.

    *Side Note*: function contains a Python implementation of JavaScript's switch-case structure that I am quite proud of :).
    The ``lambda`` stop Python from evaluating every possible outcome beforehand.
    '''
    return {
        'Clipboard'     : lambda x: magic_dct('Clipboard', key=key, glyph='Clipboard.svg'),
        'Ask'           : lambda x: magic_dct(ask_each_time, key=key, glyph='Ask.svg'),
        'CurrentDate'   : lambda x: magic_dct('Current Date', key=key, glyph='Date.svg'),
        'ExtensionInput': lambda x: magic_dct('Shortcut Input', key=key, glyph='Input.svg'),
        'ActionOutput'  : lambda x: ActionOutput(value, key, UUID_glyphs),
        'Variable'      : lambda x: magic_dct(value['VariableName'], key=key, glyph='Variable.svg'),
    }.get(var_type,       
        lambda x: magic_dct('Could Not Load Parameter', key=key, empty=True)
    )(value)
        
    
def ActionOutput(
    value:dict, 
    key:str,
    UUID_glyphs:dict = {},
):
    '''Returns a magic variable representing output from a previous action.

    Handles both normal outputs and lookups of dictionary values.
    '''
    try:
        aggr0 = value['Aggrandizements'][0]
        return magic_dct(
            aggr0['DictionaryKey'], 
            key=key,
            glyph = UUID_glyphs.get(value['OutputUUID'],''),
            UUID = value['OutputUUID'],
        )
    except (KeyError, IndexError):
        return magic_dct(
            value['OutputName'], 
            key=key,
            glyph = UUID_glyphs.get(value['OutputUUID'],''),
            UUID = value['OutputUUID'],
        )

class AddField:
    '''Decorator. Adds a ``field`` entry to every parameter dictionary in ``to_html`` results.

    As opposed to ``class`` and ``css_class`` (which provide styling information),
    ``field`` will specify the type of editing interface
    when editing is implemented.
    '''
    def __init__(self, name:str):
        self.name = name

    def __call__(self, func, *args, **kwargs):
        def field_func(*args, **kwargs):
            result = func(*args, **kwargs)
            [dct.update({'field':self.name}) for dct in result]
            return result
        return field_func