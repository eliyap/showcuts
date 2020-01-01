## Dependency: sys
import logging
from urllib.parse import quote

## Dependency: django
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

## Dependency: local
from ..forms import redditForm
from ..process.lookups._directory import *
from showcuts.user_util import post_reddit, request_token
from ..models import Shortcut

def reddit(request, hxid:str):
    shortcut_instance = get_object_or_404(Shortcut, pk=hxid)
    glyph_color = color_codes.get(shortcut_instance.colorID, '(0,0,0)')
    error = None
    
    if request.method == 'POST':
        form = redditForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(api_URL(
                hxid,
                form.cleaned_data['subreddit'],
                form.cleaned_data['title'],
            ))
    else:
        form = redditForm()
        try:
            if request.GET:
                if 'error' in request.GET:
                    raise ValueError(request.GET['error'])
                elif 'code' not in request.GET:
                    raise ValueError('Could not log into Reddit')
                hxid, subreddit, title, uuid = request.GET['state'].split('_')
                token = request_token(request.GET)
                reddit_link = post_reddit(
                    token, 
                    subreddit,
                    f'https://showcuts.app/share/view/{hxid}',
                    title,
                )
                return HttpResponseRedirect(reddit_link)
        except ValueError as e:
            error = e
        
    
    return render(request, 'xpost/reddit.html', context={
        'form': form,
        'color_code':glyph_color,
        'name':shortcut_instance.name,
        'hxid':hxid,
        'error':error,
    })

from showcuts.local_settings import REDDIT_CLIENT_ID, REDDIT_URI
from uuid import uuid4
def api_URL(hxid:str, subreddit:str, title:str):
    state_UUID = uuid4() #TODO: check against this UUID!
    subreddit = quote(subreddit, safe='')
    title = quote(title, safe='')
    return f'https://www.reddit.com/api/v1/authorize?client_id={REDDIT_CLIENT_ID}&response_type=code&state={hxid}_{subreddit}_{title}_{state_UUID}&redirect_uri={REDDIT_URI}&duration=temporary&scope=submit'