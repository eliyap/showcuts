## Dependency: system
import requests, plistlib, logging, unittest, re

## Dependency: local
from share.process.entry import request_details, byte_catcher
from share.process.action_html import make_html

error_title = [{'value': 'Error Loading Action', 'class': ['error']}]
    
def actions_from_ID(iCloudID:str):
    dct = request_details(iCloudID)

    action_file = requests.get(url=dct.get('download_link')).content
    WFdct = plistlib.loads(action_file)
    raw_actions = WFdct['WFWorkflowActions']
    
    action_blocks, _ = make_html(raw_actions)
    byte_catcher(action_blocks) # clean VCard bytes
    return action_blocks
    
## Function: check that no action encountered an error
def test_for_errors(self):
    [self.assertNotEqual(action['title'], error_title) for action in self.actions]

## Function: check that no action displays as "Under Construction"
def test_no_not_implemented(self):
    for action in self.actions:
        self.assertNotIn('Under Construction', action['title'][0]['value'])
        self.assertNotEqual('not-implemented', action['title'][0]['class'])

def test_correct_glyph(self, action, glyph_name):
    action_glyph = re.findall('.+/(.+)',action['glyph'])[0]
    self.assertEqual(action_glyph, glyph_name)

def compare_elements(self, key:str, idx:int, expected_elems:[dict]):
    elements = self.actions[idx][key]
    self.assertEqual(len(elements),len(expected_elems))
    for i in list(range(0,len(elements))):
        compare_dicts(self,elements[i],expected_elems[i])

def compare_dicts(self, title_elem, dct):
    for k,v in dct.items():
        self.assertEqual(title_elem[k], v)