
## Dependency: boilerplate
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render

def del_user(request, user, **kwargs):    
    try:
        u = User.objects.get(username = user.username)
        u.delete()
        messages.success(request, "The user is deleted")            

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return render(request, 'submit')

    except Exception as e: 
        return render(request, 'submit',{'err':e})

    return render(request, 'submit') 