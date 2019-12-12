
## Dependency: django
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

## Dependency: local
from ..process.pieces import *
from ..models import Shortcut

## Dependency: config setting
from showcuts.settings import WORKFLOW_MINIMUM_VERSION

@xframe_options_exempt
def show_shortcut(request, hxid:str):
    shortcut_instance = get_object_or_404(Shortcut, pk=hxid)
    # should only receive GET calls
    actions_blocks, UUID_glyphs = shortcut_instance.action_blocks['blocks'], shortcut_instance.UUID_glyphs
    glyph_color = color_codes.get(shortcut_instance.colorID, '(0,0,0)')
    glyph_icon = icon_codes.get(shortcut_instance.glyphID, 'skull.svg')
    types = shortcut_instance.shortcut_types.split(',')
    if 'ActionExtension' in types:
        _ = shortcut_instance.accepted_types.split(',')
        accepts = ", ".join(_[:-2] + [" and ".join(_[-2:])])
    else:
        accepts = None

    sc_age = reddit_time(timezone.now() - shortcut_instance.created_on)

    context = {
        # Aesthetic Metadata
        'name':shortcut_instance.name,
        'color_code':glyph_color,
        'glyph_icon':f'assets/glyphs/{glyph_icon}',
        'workflow_version':shortcut_instance.workflow_version,
        'min_version':WORKFLOW_MINIMUM_VERSION,
        
        # Core Action Dictionaries
        'action_blocks':actions_blocks,
        'UUID_glyphs': UUID_glyphs,
        
        # Functional Metadata
        'iCloud_link':shortcut_instance.iCloud,
        'accepted_types':accepts,
        'types':types,
        'sc_age':sc_age,
        'hxid':shortcut_instance.iCloudID,
        'likes':shortcut_instance.liked_by.count(),
        
        # user specific
        'owner':shortcut_instance.owner,
        'liked':request.user in shortcut_instance.liked_by.all(),
        'saved':request.user in shortcut_instance.saved_by.all(),
    }
    return render(request, 'show_shortcut.html', context)

def like_shortcut(request):
    if 'GET' == request.method:
        user = request.user
        hxid = request.GET['hxid']
        shortcut_instance = get_object_or_404(Shortcut, pk=hxid)

        if user in shortcut_instance.liked_by.all():
            shortcut_instance.liked_by.remove(user)
        else:
            shortcut_instance.liked_by.add(user)

        return HttpResponse('success')
    else:
        return HttpResponse('fail')

def save_shortcut(request):
    if 'GET' == request.method:
        user = request.user
        hxid = request.GET['hxid']
        shortcut_instance = get_object_or_404(Shortcut, pk=hxid)

        if user in shortcut_instance.saved_by.all():
            shortcut_instance.saved_by.remove(user)
        else:
            shortcut_instance.saved_by.add(user)

        return HttpResponse('success')
    else:
        return HttpResponse('fail')

def reddit_time(delta):
    years = int(delta.days / 365)
    months = int(delta.days / 30.5)
    days = delta.days
    hours = int(delta.seconds / 3600)
    mins = int(delta.seconds / 60)
    seconds = delta.seconds
    if   years:  return (f'{years} years'   if years>1  else 'over a year')
    elif months: return (f'{months} months' if months>1 else 'a month')
    elif days:   return (f'{days} days'     if days>1   else 'a day')
    elif hours:  return (f'{hours} hours'   if hours>1  else 'an hour')
    elif mins:   return (f'{mins} mins'     if mins>1   else 'just one minute')
    else: return 'mere seconds'