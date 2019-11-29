from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.submit_iCloud, name='submit'),
    path('submit/', views.submit_iCloud, name='submit'),
    path('view',views.submit_iCloud, name='submit'),# could later become a browsing page
    path('view/<str:hxid>',views.show_shortcut, name='view'),
    path('submitted/', views.users_submitted.as_view(), name='user-submitted'),
    path('liked/', views.users_liked.as_view(), name='user-liked'),
    path('saved/', views.users_saved.as_view(), name='user-saved'),
    path('show-me-an-error/', views.error, name='error'),
    path('like/',views.like_shortcut, name='like-shortcut'),
    path('save/',views.save_shortcut, name='save-shortcut'),
]