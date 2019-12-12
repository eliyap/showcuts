## Dependency: django
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

## Dependency: local
from ..models import Shortcut
from .display import shortcut_details

def gallery(request):
    sc_list = Shortcut.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(sc_list, 20)
    try:
        shortcuts = paginator.page(page)
    except PageNotAnInteger:
        shortcuts = paginator.page(1)
    except EmptyPage:
        shortcuts = paginator.page(paginator.num_pages)

    for shortcut_instance in shortcuts:
        setattr(shortcut_instance, 'context', shortcut_details(request, shortcut_instance))
        # shortcut_instance.context['action_blocks'] = shortcut_instance.context['action_blocks'][:3]
    return render(request, 'gallery.html', { 'shortcuts': shortcuts })
