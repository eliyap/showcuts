## Dependency: boilerplate
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.shortcuts import get_object_or_404

## Dependency: sys
import logging

## Dependency: local
from share.process.entry import make_record
from share.models import Shortcut


example_hxid = '7703feadc2c94c578c9932b032498fe4' # DEBUG ONLY

class Command(BaseCommand):
    help = 'Reprocesses Shortcut actions into HTML'

    def handle(self, *args, **kwargs):
        [redo_HTML(i.iCloudID) for i in Shortcut.objects.all()]
        logging.error('All Shortcuts Reconsidered!')

def redo_HTML(hxid:str) -> None:
    shortcut_instance = get_object_or_404(Shortcut, pk=hxid)
    owner, url = shortcut_instance.owner, shortcut_instance.iCloud
    fresh_record = make_record(url, owner)
    shortcut_instance.action_blocks = fresh_record.action_blocks
    shortcut_instance.UUID_glyphs = fresh_record.UUID_glyphs
    shortcut_instance.save()
    logging.error(f'{hxid} reconsidered.')