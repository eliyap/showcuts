## Dependency: sys
import json, re, logging

## Dependency: django boilerplate
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, render_to_response
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

## Dependency: local
from .models import Shortcut
from .forms import iCloudForm
from .process.entry import add_shortcut, noActionsError
from .process.pieces import color_dict
from django.template import RequestContext

## Dependency: social auth
from social_django.models import UserSocialAuth

def submit_iCloud(request):
    from django.http import Http404
    if request.method == 'POST':
        form = iCloudForm(request.POST)
        if form.is_valid():
            iCloudLink = form.cleaned_data['iCloudLink']
            _id = re.findall(r'/([0-9a-f]{32})$',iCloudLink)[0]
        
            if Shortcut.objects.filter(iCloudID__iexact=_id):
                
                add_shortcut(iCloudLink, request.user) # DEBUG: ALLOWs LIVE RELOADING OF SHORTCUTS

                return HttpResponseRedirect(reverse('view',kwargs={'hxid':_id}))
                # duplicate detected, direct to the existing record with some extra indicator?
                # TODO: known issue: if bad data is saved to this link, resubmitting it will not help (need to delete the shortcut). see if this affects users in production
            try:
                add_shortcut(iCloudLink, request.user)
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
        'types':types,
        'owner':shortcut_instance.owner,
    }
    return render(request, 'show_shortcut.html', context)

def error(request): # possible unncessary
    return render(request, '404.html')

class users_submitted(LoginRequiredMixin, ListView):
    model = Shortcut
    template_name = 'user/submitted.html'
    paginate_by = 20

    def get_queryset(self):
        return Shortcut.objects.filter(owner=self.request.user)
        # TODO: add sorting options? default: date submitted

@login_required
def users_settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        google_login = user.social_auth.get(provider='google-oauth2')
    except UserSocialAuth.DoesNotExist:
        google_login = None

    return render(request, 'user/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'google_login': google_login,
    })

def wallpaper(request):
    return render(request, 'wallpaper.html')