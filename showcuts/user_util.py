## Dependency: sys
import logging, json
from requests import post
from requests.auth import HTTPBasicAuth

## Dependency: boilerplate
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

## local vars
from showcuts.local_settings import REDDIT_CLIENT_ID, REDDIT_SECRET, REDDIT_URI

def del_user(request, user, **kwargs):    
    try:
        u = User.objects.get(username = user.username)
        u.delete()
        logging.error("User deleted")#debug
        #messages.success(request, "The user is deleted")            

    except User.DoesNotExist:
        logging.error("User not exist")#debug
        #messages.error(request, "User does not exist")    
        return redirect('/share/view')
        #return render(request, 'logout')

    except Exception as e: 
        return redirect('/share/view')

        #return render(request, 'logout',{'err':e})

    # TODO: add a message
    return redirect('/share/view')

def request_token(query:dict):
    logging.error(query)
    #TODO: check state to ensure it's legit
    token_req = post(
        url = 'https://www.reddit.com/api/v1/access_token',
        auth = HTTPBasicAuth(REDDIT_CLIENT_ID, REDDIT_SECRET),
        headers = {
                "User-Agent": "Showcuts",
        },
        data = dict(
            grant_type = 'authorization_code',
            redirect_uri = REDDIT_URI,
            code = query['code'],
        ),
    )
    response = json.loads(token_req.content.decode('ASCII'))
    
    if 'error' in response: 
        raise ValueError(response['error'])
    if 'access_token' not in response:
        raise ValueError('Could not log into Reddit')
    return response['access_token']

def post_reddit(token:str, subreddit:str, url:str, title:str):
    logging.error(url)
    reddit_post = post(
        url='https://oauth.reddit.com/api/submit',
        headers = {
            "Authorization": f"bearer {token}", 
            "User-Agent": "Showcuts",
        },
        data = dict(
            sr = subreddit,
            kind = 'link',
            url = url,
            title = title,
        )
    )
    post_response = json.loads(reddit_post.content.decode('ASCII'))
    try:
        reddit_link = post_response['jquery'][16][3][0]
        reddit_link = ('https://www.reddit.com' if 'reddit' not in reddit_link else '') + reddit_link
        return reddit_link
    except IndexError:
        raise
        raise ValueError('Failed to post link (might already be submitted, or account is rate limited)')