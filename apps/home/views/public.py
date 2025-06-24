from django.shortcuts import get_object_or_404, render
from register.models.publics import Public


# News pages
def news_view(request, pk=None):
    if pk:
        item = get_object_or_404(Public, pk=pk, public_type='news')
        similar_items = Public.objects.exclude(pk=item.pk, public_type='news')[:5]
        context = {
            'code': 'news',
            'item': item,
            'similar_items': similar_items
        }
        return render(request, 'src/publics/public_detail.html', context)
    else:
        items = Public.objects.filter(public_type='news')
        context = {
            'code': 'news',
            'items': items
        }
        return render(request, 'src/publics/index.html', context)


# Announcement pages
def announcement_view(request, pk=None):
    if pk:
        item = get_object_or_404(Public, pk=pk, public_type='ann')
        similar_items = Public.objects.exclude(pk=item.pk, public_type='ann')[:5]
        context = {
            'code': 'announcement',
            'item': item,
            'similar_items': similar_items
        }
        return render(request, 'src/publics/public_detail.html', context)
    else:
        items = Public.objects.filter(public_type='ann')
        context = {
            'code': 'announcement',
            'items': items
        }
        return render(request, 'src/publics/index.html', context)
