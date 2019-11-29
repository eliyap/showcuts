import logging
## Dependency: boilerplate
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

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