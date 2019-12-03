## Dependency: boilerplate
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf.urls import url

# import keys
from showcuts.local_settings import SOCIAL_AUTH_GITHUB_KEY, SOCIAL_AUTH_GITHUB_SECRET, SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET, SOCIAL_AUTH_GOOGLE_OAUTH2_KEY, SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

from django.contrib.auth import views as auth_views

# user settings
from share.views import users_settings, wallpaper, wallpaper_huge

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$', 
        auth_views.LoginView.as_view(),
        name='login'),
    url(r'^logout/$',
        auth_views.LogoutView.as_view(), 
        name='logout'),
    path('settings/', users_settings, name='user-settings'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('share/', include('share.urls')),
    path('wallpaper/', wallpaper, name='wallpaper'),
    path('wallpaper/huge', wallpaper_huge, name='wallpaper'),
    path('', RedirectView.as_view(url='share/', permanent=True)),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# social auth
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
