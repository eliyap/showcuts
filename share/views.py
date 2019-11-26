## Dependency: sys
import json, re, logging

## Dependency: django boilerplate
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, render_to_response
from django.contrib import messages

## Dependency: local
from .models import Shortcut
from .forms import iCloudForm
from .process.entry import add_shortcut, noActionsError
from .process.pieces import color_dict
from django.template import RequestContext

def submit_iCloud(request):
    from django.http import Http404
    if request.method == 'POST':
        form = iCloudForm(request.POST)
        if form.is_valid():
            iCloudLink = form.cleaned_data['iCloudLink']
            _id = re.findall(r'/([0-9a-f]{32})$',iCloudLink)[0]
        
            if Shortcut.objects.filter(iCloudID__iexact=_id):
                
                #add_shortcut(iCloudLink) # DEBUG: ALLOWs LIVE RELOADING OF SHORTCUTS

                return HttpResponseRedirect(reverse('view',kwargs={'hxid':_id}))
                # duplicate detected, direct to the existing record with some extra indicator?
                # TODO: known issue: if bad data is saved to this link, resubmitting it will not help (need to delete the shortcut). see if this affects users in production
            try:
                add_shortcut(iCloudLink)
            except noActionsError:
                #raise # debug
                messages.error(request, 'Could not get actions from Shortcut file')
                return HttpResponseRedirect(reverse('error'))
            except:
                #raise # debug
                # generic error
                return HttpResponseRedirect(reverse('error'))
            return HttpResponseRedirect(reverse('view',kwargs={'hxid':_id}))
    else:
        form = iCloudForm()

    context = {
        'form': form,
    }

    return render(request, 'submit_iCloud.html', context)

def show_shortcut(request, hxid:str):
    shortcut_instance = get_object_or_404(Shortcut, pk=hxid)
    # should only receive GET calls
    actions_blocks, UUID_glyphs = shortcut_instance.action_blocks['blocks'], shortcut_instance.UUID_glyphs
    glyph_color = color_dict.get(shortcut_instance.colorID, '(0,0,0)')
    types = shortcut_instance.shortcut_types.split(',')
    if 'ActionExtension' in types:
        _ = shortcut_instance.accepted_types.split(',')
        accepts = ", ".join(_[:-2] + [" and ".join(_[-2:])])
    else:
        accepts = None
    context = {
        'name':shortcut_instance.name,
        'action_blocks':actions_blocks,
        'UUID_glyphs': UUID_glyphs,
        'color_code':glyph_color,
        'iCloud_link':shortcut_instance.iCloud,
        'download_link':shortcut_instance.download_link,
        'accepted_types':accepts,
        'types':types
    }
    return render(request, 'show_shortcut.html', context)

def index(request):
    return render(request, 'index.html')

def error(request):
    return render(request, 'error.html')
    