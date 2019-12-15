## Dependency: sys
import re, requests, json, logging
from json import JSONDecodeError
import plistlib

## Dependency: local
from share.models import Shortcut
from share.process.action_html import make_html
from share.process.pieces import extension_lookup

## Dependency: user
from django.contrib.auth.models import User, AnonymousUser


class noActionsError(ValueError):
    pass

def make_record(url:str, user:User):
    try:
        _id = re.findall(r'[0-9a-f]{32}',url)[0]
    except IndexError:
        raise ValueError('Link doesn\'t contain a valid Shortcut ID')
    
    dct = request_details(_id)

    action_file = requests.get(url=dct.get('download_link')).content
    WFdct = plistlib.loads(action_file)
    
    try:
        raw_actions = WFdct['WFWorkflowActions']
    except KeyError:
        logging.error(WFdct.keys())
        raise noActionsError('Could not get actions from Shortcut file!')
    
    action_blocks, UUID_glyphs = make_html(raw_actions)
    # byte_catcher(action_blocks) # clean VCard bytes # obsolete method
    wrapped_blocks = {'blocks':action_blocks} # JSONField doesn't accept list of dict
    
    shortcut_types = ','.join(WFdct.get('WFWorkflowTypes',[]))
    type_list = WFdct.get('WFWorkflowInputContentItemClasses',[])
    accepted_types = ','.join([extension_lookup.get(i,i) for i in type_list])

    # anon user
    if isinstance(user, AnonymousUser): user = None

    record = Shortcut(
        iCloud=url,
        iCloudID=_id,
        download_link=dct['download_link'],
        action_blocks=wrapped_blocks, 
        UUID_glyphs=UUID_glyphs,
        #TODO accept categories later
        #TODO accept tags later
        name=dct['name'],
        glyphID=dct['glyphID'],
        workflow_version = int(float(WFdct['WFWorkflowClientVersion'])),
        colorID=dct['colorID'],
        shortcut_types=shortcut_types,
        accepted_types=accepted_types,
        owner=user,
    )
    return record

def add_shortcut(url:str, user:User):
    record = make_record(url, user)
    try:
        record.save()
    except TypeError:
        logging.exception('Type Error!')
        raise
    

def components(url) -> dict:
    # validate URL
    url_re = re.compile(r'(https://)?(www\.)?icloud\.com/shortcuts/[a-z0-9]+')
    if not re.fullmatch(url_re,url):
        raise ValueError(f'malformed shortcut link: {url}')
    id_re = re.compile(r'.*?/shortcuts/(.+)')
    _id = re.match(id_re, url)[1]

    # query API for details
    details = request_details(_id)

    # download, load file
    sc_file = requests.get(url=details.get('downloadURL')).content
    dct = plistlib.loads(sc_file)
    return dct

def request_details(_id:str) -> dict:
    data = api_request(u'https://www.icloud.com/shortcuts/api/records/' + _id)
    download_link = data['fields']['shortcut']['value']['downloadURL']
    download_link = re.sub(r'\$\{f\}', _id, download_link)
    dct = {
        'name':data['fields']['name']['value'],
        'colorID':data['fields']['icon_color']['value'],
        'glyphID':data['fields']['icon_glyph']['value'],
        'download_link':download_link,
    }
    return dct

def api_request(url:str) -> dict:
    r = requests.get(
        url = url, 
        params = {'address':'Singapore'}
    )
    try:
        return r.json()
    except JSONDecodeError:
        with open('JSONDecodeError.txt','w') as file:
            file.write(r.text)
            file.close()
        raise JSONDecodeError()

# OBSOLETE, can be deleted if nothing breaks
def byte_catcher(actions:(dict,list)):
    if isinstance(actions, dict):
        for key in actions:
            if isinstance(actions[key], (dict,list)):
                actions[key] = byte_catcher(actions[key])
            else:
                try:
                    json.dumps(actions[key])
                except TypeError:
                    actions[key] = actions[key].decode('UTF-8')
    elif isinstance(actions, list):
        for val in actions:
            if isinstance(val, (dict,list)):
                val = byte_catcher(val)
            else:
                try:
                    json.dumps(val)
                except TypeError:
                    val = val.decode('UTF-8')
    return actions