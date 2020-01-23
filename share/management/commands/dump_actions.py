## Dependency: boilerplate
from django.core.management.base import BaseCommand

## Dependency: sys
import logging, json
from json import JSONEncoder
from collections.abc import KeysView

## Dependency: local
from share.process.sc_action.directory import lookup
from share.process.sc_action.action import action

class key_encoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, KeysView):
            return list(obj)
        return JSONEncoder.default(self, obj)

class Command(BaseCommand):
    help = 'Dumps action information in .json file'

    

    def handle(self, *args, **kwargs):
        listing = dump_lookup()
        with open('SCactions.json','w') as file:
            json.dump(dump_lookup(),file, indent=4, cls=key_encoder)
            file.close()
        logging.error('All Actions Dumped!')

def dump_lookup() -> dict:
    '''
    recursively walks the tree, 
    dumping its complete path and the associated class as a JSON blob
    in ``listing``.

    Allows us to port classes written in Python over to Swift via JSON.
    '''

    def dump_blobs(
        tree:dict, 
        path:str, 
        listing:dict,
    ):
        
        for (k,v) in tree.items():
            _path = path + k
            if isinstance(v,dict):
                dump_blobs(v,_path,listing) # extend the path, keep walking
            else: # an end is reached
                listing[_path] = dump_SCaction(v)
    
    def dump_SCaction(action:action) -> dict:
        return {
            'class':action.__name__,
            'name':action.name,
            'result':action.result,
            'UUID':action.UUID,
            'glyph':action.glyph,
            'category':action.category,
            'title':[{
                **{'class':elem.__class__.__name__},
                **elem.__dict__,
            } for elem in action.title],
            'lines':[{
                **{'class':elem.__class__.__name__},
                **elem.__dict__,
            } for elem in action.lines],
        }
        

    listing = {}
    dump_blobs(
        tree=lookup,
        path='',
        listing=listing,
    )
    return listing
