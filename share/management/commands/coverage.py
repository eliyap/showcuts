## Dependency: boilerplate
from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404

## Dependency: sys
import logging

## Dependency: local
from share.models import Shortcut

class Command(BaseCommand):
    help = 'Searches database for Shortcuts with error / uncovered actions'
    def handle(self, *args, **kwargs):
        [action_coverage(i.iCloudID) for i in Shortcut.objects.all()]
        logging.error('Coverage Report Complete!')

def action_coverage(hxid:str):

    # tell me how many error actions & how many under construction actions there are
    # tell me the indices of these actions
    # also look for line elems that are not covered
    shortcut_instance = get_object_or_404(Shortcut, pk=hxid)
    blocks = shortcut_instance.action_blocks['blocks']
    for idx, block in enumerate(blocks):
        try:
            title = block['title'][0]
            if ('Error Loading Action','error') == (title['value'], title['class']):
                show_error(hxid,idx,'Error Loading Action')
            elif 'not-implemented' == title['class']:
                pass # log
                show_error(hxid,idx,title['value'])
        except IndexError: pass

from showcuts.local_settings import DEBUG
def show_error(hxid:str, idx:int, problem:str):
    print(
        f'{"http://127.0.0.1:8000" if DEBUG else"https://showcuts.app"}/share/view/{hxid}',
        f'Action {idx + 1}',
        problem
    )
