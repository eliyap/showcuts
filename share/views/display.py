## Dependency: sys
import logging

## Dependency: django
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.models import Group

## Dependency: local
from ..process.lookups._directory import *
from ..models import Shortcut
from ..process.sc_action.action import action

## Dependency: config setting
from showcuts.settings import WORKFLOW_MINIMUM_VERSION

def shortcut_details(request, shortcut_instance):
    types = shortcut_instance.shortcut_types.split(',')
    if 'ActionExtension' in types:
        _ = shortcut_instance.accepted_types.split(',')
        accepts = ", ".join(_[:-2] + [" and ".join(_[-2:])])
    else:
        accepts = None

    # premium status granted if viewer or submitter is premium
    premium_status = False
    if request.user.groups.filter(name = 'Premium'): premium_status = True
    if shortcut_instance.owner and shortcut_instance.owner.groups.filter(name = 'Premium'): premium_status = True

    #debug
    logging.error(shortcut_instance.action_blocks['blocks'][0].__dict__)
    return {
        # Aesthetic Metadata
        'name':shortcut_instance.name,
        'color_code':color_codes.get(shortcut_instance.colorID, '(0,0,0)'),
        'glyph_icon':'assets/glyphs/' + icon_codes.get(shortcut_instance.glyphID, 'skull.svg'),
        'workflow_version':shortcut_instance.workflow_version,
        'min_version':WORKFLOW_MINIMUM_VERSION,
        
        # Core Action Dictionaries
        'action_blocks':shortcut_instance.action_blocks['blocks'],
        'UUID_glyphs': shortcut_instance.UUID_glyphs,
        
        # Functional Metadata
        'iCloud_link':f'https://www.icloud.com/shortcuts/{shortcut_instance.iCloudID}',
        'accepted_types':accepts,
        'types':types,
        'sc_age':reddit_time(timezone.now() - shortcut_instance.created_on),
        'hxid':shortcut_instance.iCloudID,
        'likes':shortcut_instance.liked_by.count(),
        
        # user specific
        'owner':shortcut_instance.owner,
        'liked':request.user in shortcut_instance.liked_by.all(),
        'saved':request.user in shortcut_instance.saved_by.all(),
        'premium':premium_status,
    }

@xframe_options_exempt
def show_shortcut(request, hxid:str):
    return render(
        request, 
        'show_shortcut.html', 
        context=shortcut_details(
            request, 
            shortcut_instance=get_object_or_404(Shortcut, pk=hxid),
        )
    )

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

def grant_premium(request):
    if 'GET' == request.method:
        premium = Group.objects.get(name='Premium') 
        premium.user_set.add(request.user)
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