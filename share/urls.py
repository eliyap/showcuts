from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.submit_iCloud, name='submit'),
    path('submit/', views.submit_iCloud, name='submit'),
    path('view',views.submit_iCloud, name='submit'),# could later become a browsing page
    path('view/<str:hxid>',views.show_shortcut, name='view'),
    #path('error', views.error, name='error'),
]