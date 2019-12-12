## Dependency: django
from django.shortcuts import render

def error(request): # possible unncessary
    return render(request, '500.html')

def wallpaper(request):
    return render(request, 'wallpaper.html')

def wallpaper_huge(request):
    return render(request, 'wallpaper_huge.html')

def about(request):
    return render(request, 'about.html')