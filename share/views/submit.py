## Dependency: sys
import re

## Dependency: django
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

## Dependency: local
from ..forms import iCloudForm
from ..models import Shortcut
from ..process.entry import add_shortcut, noActionsError

## Local variables
from showcuts.local_settings import LIVE_RELOADING, DEBUG
from showcuts.user_util import post_reddit

def submit_iCloud(request):
    from django.http import Http404
    if request.method == 'POST':
        form = iCloudForm(request.POST)
        if form.is_valid():
            return direct_to_display(request, form)
    else:
        form = iCloudForm()
        
    return render(request, 'submit_iCloud.html', context={'form': form})

def direct_to_display(request, form):
    iCloudLink = form.cleaned_data['iCloudLink']
    _id = re.findall(r'/([0-9a-f]{32})$',iCloudLink)[0]

    if Shortcut.objects.filter(iCloudID__iexact=_id):
        
        if LIVE_RELOADING:
            get_object_or_404(Shortcut, pk=_id).delete()
            
            add_shortcut(iCloudLink, request.user) # DEBUG: ALLOWs LIVE RELOADING OF SHORTCUTS

        return HttpResponseRedirect(reverse('view',kwargs={'hxid':_id}))
    try:
        add_shortcut(iCloudLink, request.user)
    except noActionsError:
        if DEBUG: raise # debug
        messages.error(request, 'Could not get actions from Shortcut file')
        return HttpResponseRedirect(reverse('error'))
    except:
        if DEBUG: raise # debug
        return HttpResponseRedirect(reverse('error'))
    return HttpResponseRedirect(reverse('view',kwargs={'hxid':_id}))