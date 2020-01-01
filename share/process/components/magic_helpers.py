def value_dct(
    value: str,
    css_class: [str] = [],
    empty: bool = False,
):
    if empty: css_class.append('empty')
    return {
        'class':css_class,
        'value':value
    }

def magic_dct(
    value: str, 
    empty: bool = False, 
    glyph:str = '', 
    UUID:str = None
) -> dict:
    return {
        'class': ['magic'] + (['empty'] if empty else []),
        'value': value,
        'glyph': f'assets/cat/{glyph}' if glyph else '',
        'UUID' : UUID,
    }

def error_magic():
    return magic_dct(value='<error>', empty=True)

def classify_magic(
    value: dict, 
    var_type: str, 
    ask_each_time: str = 'Ask Each Time',
    UUID_glyphs:dict = {},
) -> dict:
    return {
        'Clipboard'     : lambda x: magic_dct('Clipboard', glyph='Clipboard.svg'),
        'Ask'           : lambda x: magic_dct(ask_each_time, glyph='Ask.svg'),
        'CurrentDate'   : lambda x: magic_dct('Current Date', glyph='Date.svg'),
        'ExtensionInput': lambda x: magic_dct('Shortcut Input', glyph='Input.svg'),
        'ActionOutput'  : lambda x: ActionOutput(value, UUID_glyphs),
        'Variable'      : lambda x: magic_dct(value['VariableName'], glyph='Variable.svg'),
    }.get(var_type,       
        lambda x: magic_dct('Could Not Load Parameter', empty=True)
    )(value)
        
    
def ActionOutput(
    value:dict, 
    UUID_glyphs:dict = {},
):
    try:
        aggr0 = value['Aggrandizements'][0]
        return magic_dct(
            aggr0['DictionaryKey'], 
            glyph = UUID_glyphs.get(value['OutputUUID'],''),
            UUID = value['OutputUUID'],
        )
    except (KeyError, IndexError):
        return magic_dct(
            value['OutputName'], 
            glyph = UUID_glyphs.get(value['OutputUUID'],''),
            UUID = value['OutputUUID']
        )

