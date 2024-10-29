from django.shortcuts import get_object_or_404, render
from main.public.models import News, Announcement, Event


# News pages
def news_view(request, pk=None):
    if pk:
        item = get_object_or_404(News, pk=pk)
        return render(request, 'src/publics/public_detail.html', {'item': item})
    else:
        items = News.objects.all()
        context = {
            'code': 'news',
            'items': items
        }
        return render(request, 'src/publics/index.html', context)


# Announcement pages
def announcement_view(request, pk=None):
    if pk:
        item = get_object_or_404(Announcement, pk=pk)
        return render(request, 'src/publics/public_detail.html', {'item': item})
    else:
        items = Announcement.objects.all()
        context = {
            'code': 'announcement',
            'items': items
        }
        return render(request, 'src/publics/index.html', context)


# Event pages
def event_view(request, pk=None):
    if pk:
        item = get_object_or_404(Event, pk=pk)
        return render(request, 'src/publics/public_detail.html', {'item': item})
    else:
        items = Event.objects.all()
        context = {
            'code': 'event',
            'items': items
        }
        return render(request, 'src/publics/index.html', context)
