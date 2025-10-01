from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from register.models.publics import Public


# news page
# ----------------------------------------------------------------------------------------------------------------------
def news_view(request, pk=None):
    if pk:
        item = get_object_or_404(Public, pk=pk, public_type='news')
        similar_items = Public.objects.exclude(pk=item.pk, public_type='news')[:10]
        context = {
            'code': 'news',
            'item': item,
            'similar_items': similar_items
        }
        return render(request, 'app/publics/public/page.html', context)
    else:
        items = Public.objects.filter(public_type='news')
        paginator = Paginator(items, 100)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'code': 'news',
            'page_obj': page_obj
        }
        return render(request, 'app/publics/page.html', context)


# announcement page
# ----------------------------------------------------------------------------------------------------------------------
def announcement_view(request, pk=None):
    if pk:
        item = get_object_or_404(Public, pk=pk, public_type='ann')
        similar_items = Public.objects.exclude(pk=item.pk, public_type='ann')[:10]
        context = {
            'code': 'announcement',
            'item': item,
            'similar_items': similar_items
        }
        return render(request, 'app/publics/public/page.html', context)
    else:
        items = Public.objects.filter(public_type='ann')
        paginator = Paginator(items, 100)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'code': 'announcement',
            'page_obj': page_obj
        }
        return render(request, 'app/publics/page.html', context)
