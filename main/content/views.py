from django.shortcuts import get_object_or_404, render
from .models import Category, Content
from ..public.models import Event, Announcement, News
from ..university.models import Division


# Content detail
# ----------------------------------------------------------------------------------------------------------------------
def content_detail(request, category_slug, sub_category_slug, section_slug, content_slug):
    category = get_object_or_404(Category, slug=category_slug)
    sub_category = get_object_or_404(Category, parent=category, slug=sub_category_slug)
    section = get_object_or_404(Category, parent=sub_category, slug=section_slug)
    content = get_object_or_404(Content, category=section, slug=content_slug)

    sub_categories = Category.objects.filter(parent=category)
    contents = Content.objects.filter(category__parent__parent=category)

    context = {
        'content': content,
        'category': category,
        'sub_category': sub_category,
        'section': section,

        'sub_categories': sub_categories,
        'contents': contents,
    }

    return render(request, 'src/content/index.html', context)


# Division detail
# ----------------------------------------------------------------------------------------------------------------------
def division_detail(request, slug):
    item = get_object_or_404(Division, slug=slug)
    departments = item.children.filter(div_type='department')
    divisions = item.children.filter(div_type='div')
    news = News.objects.filter(division=item)
    events = Event.objects.filter(division=item)
    announcements = Announcement.objects.filter(division=item)

    context = {
        'division': item,
        'departments': departments,
        'divisions': divisions,
        'news': news,
        'events': events,
        'announcements': announcements
    }
    return render(request, 'src/university/division/index.html', context)


# Division about
def division_about(request, slug):
    item = get_object_or_404(Division, slug=slug)
    context = {
        'division': item,
    }
    return render(request, 'src/university/division/about.html', context)