from django.shortcuts import get_object_or_404, render
from register.models.content import Category, Content
from register.models.publics import Public
from register.models.university import Division


# Content detail
# ----------------------------------------------------------------------------------------------------------------------
def content_detail(request, category_slug, sub_category_slug, section_slug, content_slug):
    category = get_object_or_404(Category, slug=category_slug)
    sub_category = get_object_or_404(Category, parent=category, slug=sub_category_slug)
    section = get_object_or_404(Category, parent=sub_category, slug=section_slug)
    content = get_object_or_404(Content, category=section, slug=content_slug)

    sub_categories = Category.objects.filter(parent=category)
    contents = Content.objects.filter(category__parent__parent=category)

    # accordion-да ашық тұру керек бөлімнің id-сін береміз
    open_section_ids = {section.id}

    context = {
        'content': content,
        'category': category,
        'sub_category': sub_category,
        'section': section,

        'sub_categories': sub_categories,
        'contents': contents,
        'open_section_ids': open_section_ids,
    }

    return render(request, 'src/content/index.html', context)


# Division detail
# ----------------------------------------------------------------------------------------------------------------------
def division_detail(request, slug):
    item = get_object_or_404(Division, slug=slug)
    departments = item.children.filter(div_type='department')
    divisions = item.children.filter(div_type='div')
    news = Public.objects.filter(public_type='news', division=item)
    events = Public.objects.filter(public_type='news', division=item)
    announcements = Public.objects.filter(public_type='ann', division=item)

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
