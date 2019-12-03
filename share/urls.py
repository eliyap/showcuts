from django.urls import path
from django.views.generic import RedirectView
from share.views import *

urlpatterns = [
    path('', submit_iCloud, name='submit'),
    path('submit/', submit_iCloud, name='submit'),
    path('view',submit_iCloud, name='submit'),# could later become a browsing page
    path('view/<str:hxid>',show_shortcut, name='view'),
    path('submitted/', users_submitted.as_view(), name='user-submitted'),
    path('liked/', users_liked.as_view(), name='user-liked'),
    path('saved/', users_saved.as_view(), name='user-saved'),
    path('error/', error, name='error'),
    path('like/',like_shortcut, name='like-shortcut'),
    path('save/',save_shortcut, name='save-shortcut'),
]