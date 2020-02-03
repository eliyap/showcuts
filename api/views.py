from django.shortcuts import render

from rest_framework import viewsets

from .serializers import ShortcutSerializer
from .models import Shortcut


class ShortcutViewSet(viewsets.ModelViewSet):
    queryset = Shortcut.objects.all().order_by('iCloudID')
    serializer_class = ShortcutSerializer