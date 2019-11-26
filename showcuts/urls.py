from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf.urls import url

from django.contrib.auth import views as auth_views
# import keys
from .local_settings import SOCIAL_AUTH_GITHUB_KEY, SOCIAL_AUTH_GITHUB_SECRET, SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$', 
        auth_views.LoginView.as_view(),
        {'template_name': "registration/login.html"}, 
        name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('share/', include('share.urls')),
    path('', RedirectView.as_view(url='share/', permanent=True)),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# social auth
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
