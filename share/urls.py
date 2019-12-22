from django.urls import path
from share.views import submit, misc, display, user, xpost, collections

urlpatterns = [
    # aliases for home view
    path('', submit.submit_iCloud, name='submit'),
    path('submit/', submit.submit_iCloud, name='submit'),
    path('view', submit.submit_iCloud, name='submit'),# could later become a browsing page
    path('view/<str:hxid>',display.show_shortcut, name='view'),
    
    # for logged in users
    path('submitted/', user.users_submitted.as_view(), name='user-submitted'),
    path('liked/', user.users_liked.as_view(), name='user-liked'),
    path('saved/', user.users_saved.as_view(), name='user-saved'),
    
    # gallery views
    path('gallery/', collections.gallery, name='coll-gallery'),
    # post links
    path('reddit/<str:hxid>', xpost.reddit, name = 'reddit'),

    # misc paths
    path('error/', misc.error, name='error'),

    # AJAX paths
    path('like/', display.like_shortcut, name='like-shortcut'),
    path('save/', display.save_shortcut, name='save-shortcut'),
    path('premium/', display.grant_premium, name='grant-premium'),
]