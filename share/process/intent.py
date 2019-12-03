## Dependency: sys
import re, logging
from os import system
from os.path import expanduser
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError
from base64 import b64decode, binascii

## Dependency: local
from share.process.pieces import app_categorize
from showcuts.local_settings import sys_os
from share.process.pieces import infoless

## Function: extract glyph and stuff from Siri Intent
temp_plist_path = '/temporary.plist'

def decode_bplist(pbytes:bytes):
    with open(expanduser('~') + temp_plist_path,'wb') as f:
        f.write(pbytes)
        f.close()
    if 'macOS' == sys_os:
        system('plutil -convert xml1 ~' + temp_plist_path)
    elif 'ubuntu' == sys_os:
        system(f'plistutil -i ~{temp_plist_path} -o ~{temp_plist_path}') # TODO: test this in staging first!
    ptree = ET.parse(expanduser('~') + temp_plist_path)
    data = ptree.getroot().findall('.//data')
    return [i.text for i in data]

def decode_parameters(parameters:dict, key:str):
    data_text = decode_bplist(parameters[key])
    data_text = sorted(data_text, key=lambda x: len(x))
    decoded = [b64decode(i) for i in data_text]
    return decoded

def get_intent(parameters:dict) -> dict:
    data_text = decode_parameters(parameters, 'IntentData')
    intent_str = clean_bytes(data_text[0][:100])
    
    matching_apps = [app for app in app_categorize if app in intent_str]
    if not matching_apps:
        return infoless
    else:
        if len(matching_apps) > 1:
            logging.error('More than 1 app found!', matching_apps)
        match = app_categorize[matching_apps[0]]
        match['remainder'] = get_remainder(intent_str, matching_apps[0], app_categorize[matching_apps[0]]['name'])
        return match

def get_useractivity(parameters:dict) -> dict:
    data_text = decode_parameters(parameters, 'UserActivityData')
    return 'Open '+clean_bytes(data_text[0])
    

def cat_intent(remainder:str):
    pass


shards = [
    r'^MP',
    r'Xb',
    r'\\(n|t|r)',
    r'^\d',
    r'^(,|:|\.|,|\(|\?|\/)',
]
def clean_bytes(byts:bytes)->str:
    # removes the b'' wrapper, and any \x** strings
    _ = re.sub(r'\\x[0-9a-f]{2}', '', str(byts)[2:-1])
    for i in shards:
        _ = re.sub(i,'',_)
    for i in shards:
        _ = re.sub(i,'',_)
    return _

def get_remainder(_:str, url:str,name:str) -> str:
    _ = re.sub(url,'',_)
    _ = re.sub(name,'',_)
    _ = re.sub('Xb','',_)
    _ = re.sub('x$','',_) # there are trailing x's in words, but this should be net positive
    return _