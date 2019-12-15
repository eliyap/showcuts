## Dependency: sys
import logging
import re

from share.process.pieces import time_codes


def make_specify(parameters: dict, key: str, default: str, align_left: bool = False) -> dict:
    val = parameters.get(key, None)
    if not val:
        elem = {'value': default, 'class': 'specify empty', }
    else:
        elem = make_magic(parameters, key, default, force_magic=False)
        elem['class'] += ' specify'
    if align_left:
        elem['class'] += ' leftify'
    return elem


def make_choose(parameters: dict, key: str, default: str) -> dict:
    val = parameters.get(key, None)
    if not val:
        return{'value': default, 'class': 'choose-var', }

    elem = make_magic(parameters, key, default, default_blank=False, force_magic=False)
    elem['class'] += ' choose-var'
    return elem

# Function: returns an appropriate magic variable, whether or not it's a magic var


def make_magic(
    parameters: dict,
    key: str,
    default: str = 'Input',
    subtype: str = 'Type',  # for edge cases
    # determines whether the return has 'empty' as a CSS class
    default_blank: bool = True,
    # other fn.s piggy backing off the detection here may not want magic for text, etc.
    force_magic: bool = True,
    ask_text: str = 'Ask Each Time',
) -> dict:
    val = parameters.get(key, None)
    if val == None or val == '':  # do NOT use falsy values here, as 0 is sometimes passed
        if force_magic:
            return magic(default, default_blank)
        return{
            'value': default,
            'class': 'empty' if default_blank else '',
        }

    if not isinstance(val, dict):  # non magic variable
        if force_magic:
            return magic(val)
        return{
            'value': val,
            'class': '',
        }

    # for non-action magic vars
    if val.get('Type', None) == 'Variable':
        val = val['Variable']

    val = val['Value']
    if 'string' in val and 'attachmentsByRange' in val:
        return get_inline(val, magic_wrapper=force_magic, ask_text='Text')
    var_type = val[subtype]
    new_magic = classify_magic(val, var_type, ask_text=ask_text)
    if new_magic:
        return new_magic
    # TODO: test handling of inline magic vars (e.g. "Today's date is [DATE]")
    # also test Current Date, Shortcut Input
    return magic(f'{key}?', True)
    #raise ValueError(f'No magic var {key}!',val)


def make_location(parameters: dict, key: str, default: str, default_blank: bool = True, ask_text:str='Ask Each Time'):
    val = parameters.get(key, None)
    if not val:
        return{'value': default, 'class': 'magic' + (' empty' if default_blank else ''), }

    # under construction, need to see what ways to get location names
    try:  # there are surely more ways to get a location name than this
        location = parameters[key]['placemark']['addressDictionary']
        location_name = location.get('Name', None)
        if not location_name:
            location_name = location.get('Street', None)
        if not location_name:
            location_name = location.get('City', None)
        if not location_name:
            location_name = location.get('State', None)
        if not location_name:
            location_name = location.get('Country', None)
        if not location_name:
            raise KeyError  # pass it off to magic var
        location_elem = magic(location_name)
    except KeyError:
        if 'isCurrentLocation' in parameters[key] and parameters[key]['isCurrentLocation'] == True:
            return magic('Current Location')
        location_elem = make_magic(parameters, key, default, default_blank=default_blank, force_magic=True, ask_text=ask_text)
    return location_elem


def get_inline(val: dict, magic_wrapper=True, ask_text: str = 'Ask Each Time') -> list:
    title_elems, attached_magic = [], []
    try:
        line = val['string']
        attached = list(val['attachmentsByRange'].values())
        for attachment in attached:
            var_type = attachment.get('Type', '')
            logging.error(attachment)
            new_magic = classify_magic(attachment, var_type, ask_text=ask_text)
            if not new_magic:
                new_magic = magic('VAR')
            attached_magic.append(new_magic)
        elems = line.split('￼')  # '' contains \uFFFC!
        for i in range(0, len(attached)):
            title_elems.append(text_elem(elems[i]))
            title_elems.append(attached_magic[i])
        title_elems.append(text_elem(elems[-1:][0]))  # attach trailing item
    except (KeyError, IndexError) as e:
        logging.exception("Exception occurred")
        import json
        logging.error(json.dumps(val))
        return magic('<inline variable>')
    title_elems = [i for i in title_elems if i['value']] # purge empty elements
    return {
        'class': 'inline' + (' magic' if magic_wrapper else ''),
        'value': title_elems,
    }


def classify_magic(val: dict, var_type: str, ask_text: str = 'Ask Each Time') -> dict:
    if 'Clipboard' == var_type:
        return magic('Clipboard', False, glyph='Clipboard.svg')
    elif 'Ask' == var_type:
        return magic(ask_text, False, glyph='Ask.svg')
    elif 'CurrentDate' == var_type:
        return magic('Current Date', False, glyph='Date.svg')
    elif 'ExtensionInput' == var_type:
        return magic('Shortcut Input', False, glyph='Input.svg')
    elif 'ActionOutput' == var_type:
        logging.error(val) # debug
        try:
            # assert 'Dictionary' == val['OutputName']
            aggr0 = val['Aggrandizements'][0]
            # assert aggr0['Type'] == 'WFDictionaryValueVariableAggrandizement'
            return magic(aggr0['DictionaryKey'], False, UUID=val['OutputUUID'])
        except:
            return magic(val['OutputName'], False, UUID=val['OutputUUID'])
    elif 'Variable' == var_type:
        return magic(val['VariableName'], False, glyph='Variable.svg')


def make_line(label: str, var_elem: dict) -> dict:
    dct = {'label': label, }
    dct.update(var_elem)
    return dct


def make_toggle(parameters: dict, key: str = 'WFSomething', default: bool = False) -> dict:
    toggle_state = parameters.get(key, default)
    if toggle_state == True:
        return toggle('on')
    elif toggle_state == False:
        return toggle('off')
    else:
        return make_magic(parameters, key, force_magic=True)


def toggle(state: str = 'on') -> dict:
    return {
        'class': 'toggle '+state,
        'value': '',
    }


def magic(var_name: str = 'DEFAULT?', blank: bool = False, glyph: str = '', UUID: str = ''):
    return {
        'class': 'magic' + (' empty' if blank else ''),
        'value': var_name,
        'glyph': f'assets/cat/{glyph}' if glyph else '',
        'UUID': UUID,
    }


def image_crop(parameters) -> [dict]:
    position_elem = make_magic(
        parameters, 'WFImageCropPosition', 'Bottom Right', default_blank=False)
    coord_elems = []
    if position_elem['value'] in ['Centre', 'Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']:
        position_elem['class'] = 'choose-var'
    elif position_elem['value'] == 'Custom':
        position_elem['class'] = 'choose-var'
        coord_elems = [
            make_line('X Coordinate', make_specify(
                parameters, 'WFImageCropX', '0')),
            make_line('Y Coordinate', make_specify(
                parameters, 'WFImageCropY', '0')),
        ]
    line_elems = [
        make_line('Position', position_elem)
    ] + coord_elems + [
        make_line('Width', make_specify(
            parameters, 'WFImageCropWidth', '100')),
        make_line('Height', make_specify(
            parameters, 'WFImageCropHeight', '100')),
    ]
    return line_elems


def on_off(parameters) -> dict:
    on_elem = make_magic(parameters, 'OnValue', 1)
    on_elem['value'] = {1: 'On', 0: 'Off'}.get(
        on_elem['value'], on_elem['value'])
    return on_elem


def replace_ask(magic: dict, default: str) -> dict:
    magic['value'] = {'Ask Each Time': default}.get(
        magic['value'], magic['value'])
    return magic


def product_details(parameters) -> [dict]:
    search_elem = make_magic(parameters, 'WFAttribute',
                             'All', default_blank=False)
    search_elem['class'] = 'choose-var'
    line_elems = [make_line('Search By', search_elem)]

    if search_elem['value'] != 'Product ID':
        results_elem = make_magic(
            parameters, 'WFEntity', 'Songs', default_blank=False)
        results_elem['class'] = 'choose-var'
        line_elems += [make_line('Results', results_elem)]
    # default region depends on user's location
    region_elem = make_magic(parameters, 'WFCountry', 'Region')
    region_elem['class'] = 'choose-var'
    line_elems += [make_line('Region', region_elem)]
    if search_elem['value'] != 'Product ID':
        pass  # TODO: add item counter here!
    return line_elems


def get_list(parameters) -> [dict]:

    default = [
        list_elem('One'),
        list_elem('Two'),
    ]
    elems = []
    try:
        items = parameters['WFItems']
    except KeyError:
        return default
    for item in items:
        if isinstance(item, str):
            elems.append({'value': item, 'class': 'text'})
        else:
            elems.append(get_inline(
                item['WFValue']['Value'], magic_wrapper=False))
    return elems


def list_elem(value: str) -> dict:
    return {
        'value': value,
        'class': 'dict-key',  # for the CSS
    }


def get_dict(parameters: dict) -> [(str, dict)]:
    default = [{'kind': '', 'key': '', 'value': ''}]
    elems = []
    try:
        items = parameters['WFItems']['Value']['WFDictionaryFieldValueItems']
    except KeyError:
        return default
    for item in items:
        elems.append(make_dict_elem(item))
    return elems


def make_dict_elem(item: dict) -> dict:
    key_param, value_param = item['WFKey']['Value'], item['WFValue']['Value']
    key = get_inline(key_param, magic_wrapper=False)
    kind = {
        0: 'text',
        1: 'dict',
        2: 'array',
        3: 'number',
        4: 'bool',
    }.get(item['WFItemType'], None)

    if 'text' == kind:
        value = get_inline(value_param, magic_wrapper=False)
        if value_param['string'] == '':
            value = [{'value': 'Text', 'class': 'blank'}]
    elif 'number' == kind:
        value = get_inline(value_param, magic_wrapper=False)
        if value_param['string'] == '':
            value = [{'value': 'Number', 'class': 'blank'}]
    elif 'dict' == kind:
        sub_dict_items = value_param['Value']['WFDictionaryFieldValueItems']
        item_count = len(sub_dict_items)
        value = {
            'value': f'{item_count} item'+('' if item_count == 1 else 's'),
            'class': 'choose-var'
        }
    elif 'array' == kind:
        item_count = len(value_param)
        value = {
            'value': f'{item_count} item'+('' if item_count == 1 else 's'),
            'class': 'choose-var'
        }
    elif 'bool' == kind:
        if value_param in [False, True]:
            value_elem = {'value': value_param, 'class': 'choose-var'}
        else:
            value_elem = make_magic({'dummy': value_param}, 'dummy')
        value = value_elem
    else:
        raise ValueError('Unrecognized value in dictionary!')
        logging.exception('Unrecognized value in dictionary!')
    return {
        'kind': kind,
        'key': key,
        'value': value,
    }

# Function: wraps string in a dict with no class, so that it is rendered properly in the template


def text_elem(text: str) -> dict:
    return {'value': text, 'class': 'text'}


def make_pill(parameters: dict, key: str, options: [str], default: str) -> dict:
    selection = parameters.get(key, None)
    if not selection:
        selection = default
    if isinstance(selection, dict):  # I CAST DETECT MAGIC
        return make_magic(parameters, key)
    
    # TODO: replace this duct tape
    selection = selection.title()  # vars are often lowercased
    selection = re.sub('To','to', selection) # 'A to Z' is the exception

    pill_elems = []
    [pill_elems.append({'selected': option == selection, 'value': option, }) for option in options]
    return {'class': 'pill', 'value': pill_elems, }


def make_counter(parameters: dict, key: str, label: str, default: int, magic_label: str) -> dict:
    count = parameters.get(key, None)
    if not count:
        count = default
    if isinstance(count, dict):  # I CAST DETECT MAGIC
        return make_line(magic_label, make_magic(parameters, key))
    try:
        count = str(int(float(count)))
    except ValueError:
        count = '<error>'

    label = re.sub(r'#', count, label)  # sub in the count
    label += ('' if count == '1' else 's')
    return make_line(label, {'class': 'counter', 'value': 'placeholder', })


def get_duration(parameters: dict, default_magnitude: int = 0, default_unit: str = 'minute') -> [dict]:
    try:
        duration = parameters['WFDuration']['Value']
        if isinstance(duration['Magnitude'], dict):
            mag_elem = classify_magic(
                {}, duration['Magnitude']['Type'], ask_text='Duration')
        else:
            magnitude = re.sub(r'\.0', '', str(duration['Magnitude']))
            mag_elem = magic(magnitude)
        duration_elems = [mag_elem, magic(duration['Unit'])]
    except KeyError:
        duration_elems = [
            magic(str(default_magnitude), True), magic(default_unit)]
    # convert time short forms
    duration_elems[1]['value'] = time_codes.get(duration_elems[1]['value'], duration_elems[1]['value'])
    duration_elems[1]['value'] += '' if duration_elems[0]['value'] == '1' else 's'
    # sometimes this results in 'weekss', correct that:
    duration_elems[1]['value'] = re.sub('ss$', 's', duration_elems[1]['value'])
    return duration_elems


def get_podcast(
    parameters: dict,
    key: str,
    default: str = 'Input',
    subtype: str = 'Type',  # for edge cases
    # determines whether the return has 'empty' as a CSS class
    default_blank: bool = True,
    # other fn.s piggy backing off the detection here may not want magic for text, etc.
    force_magic: bool = True,
    ask_text: str = 'Ask Each Time',
) -> dict:
    try:
        podcast_name = parameters[key]['collectionName']
        return magic(podcast_name)
    except KeyError:
        return make_magic(
            parameters,
            key,
            default=default,
            default_blank=default_blank,  # determines whether the return has 'empty' as a CSS class
            ask_text='Podcast',
        )

def iCloud_path(val):
    if isinstance(val, list): # inline shortcut
        val = [text_elem('/Shortcuts/')] + val
    else:
        val = '/Shortcuts/' + val
    return val