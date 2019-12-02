## Dependency: sys
import json, re, logging, datetime
from django.utils import timezone

## Dependency: django boilerplate
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
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

## Dependency: debug settings
from showcuts.local_settings import LIVE_RELOADING, DEBUG

def submit_iCloud(request):
    from django.http import Http404
    if request.method == 'POST':
        form = iCloudForm(request.POST)
        if form.is_valid():
            iCloudLink = form.cleaned_data['iCloudLink']
            _id = re.findall(r'/([0-9a-f]{32})$',iCloudLink)[0]
        
            if Shortcut.objects.filter(iCloudID__iexact=_id):
                
                if LIVE_RELOADING:
                    shortcut_instance = get_object_or_404(Shortcut, pk=_id)
                    shortcut_instance.delete()
                    add_shortcut(iCloudLink, request.user) # DEBUG: ALLOWs LIVE RELOADING OF SHORTCUTS

                return HttpResponseRedirect(reverse('view',kwargs={'hxid':_id}))
                # duplicate detected, direct to the existing record with some extra indicator?
                # TODO: known issue: if bad data is saved to this link, resubmitting it will not help (need to delete the shortcut). see if this affects users in production
            try:
                add_shortcut(iCloudLink, request.user)
            except noActionsError:
                if DEBUG:
                    raise # debug
                messages.error(request, 'Could not get actions from Shortcut file')
                return HttpResponseRedirect(reverse('error'))
            except:
                if DEBUG:
                    raise # debug
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

    sc_age = reddit_time(timezone.now() - shortcut_instance.created_on)

    context = {
        'name':shortcut_instance.name,
        'action_blocks':actions_blocks,
        'UUID_glyphs': UUID_glyphs,
        'color_code':glyph_color,
        'iCloud_link':shortcut_instance.iCloud,
        'accepted_types':accepts,
        'types':types,
        'owner':shortcut_instance.owner,
        'sc_age':sc_age,
        'hxid':shortcut_instance.iCloudID,
        'likes':shortcut_instance.liked_by.count(),
        'liked':request.user in shortcut_instance.liked_by.all(),
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

def error(request): # possible unncessary
    return render(request, '500.html')

class users_submitted(LoginRequiredMixin, ListView):
    model = Shortcut
    template_name = 'user/submitted.html'
    paginate_by = 20

    def get_queryset(self):
        return Shortcut.objects.filter(owner=self.request.user)
        # TODO: add sorting options?

class users_saved(LoginRequiredMixin, ListView):
    model = Shortcut
    template_name = 'user/saved.html'
    paginate_by = 20

    def get_queryset(self):
        return self.request.user.liked.all()
        # TODO: add sorting options? default: date submitted

class users_liked(LoginRequiredMixin, ListView):
    model = Shortcut
    template_name = 'user/liked.html'
    paginate_by = 20

    def get_queryset(self):
        return self.request.user.saved.all()
        # TODO: add sorting options? default: date saved

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

def wallpaper_huge(request):
    return render(request, 'wallpaper_huge.html')

def reddit_time(delta):
    years = int(delta.days / 365)
    months = int(delta.days / 30.5)
    days = delta.days
    hours = int(delta.seconds / 3600)
    minutes = int(delta.seconds / 60)
    seconds = delta.seconds
    if years > 1:
        return f'{years} years'
    elif years ==1:
        return r'over a year'
    if months > 1:
        return f'{months} years'
    elif months ==1:
        return r'a month'
    elif days > 1:
        return f'{days} days'
    elif days == 1:
        return f'a day'
    elif hours > 1:
        return f'{hours} hours'
    elif hours == 1:
        return f'an hour'
    elif minutes > 1:
        return f'{minutes} minutes'
    elif minutes == 1:
        return 'just one minute'
    else: return 'mere seconds'