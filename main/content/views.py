from django.shortcuts import get_object_or_404, render
from rest_framework import views, permissions, status
from rest_framework.response import Response

from .models import Category, Content


# content detail page
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


# ContentDetail
class ContentDetail(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, category_slug, sub_category_slug, section_slug, content_slug):
        category = get_object_or_404(Category, slug=category_slug)
        sub_category = get_object_or_404(Category, parent=category, slug=sub_category_slug)
        section = get_object_or_404(Category, parent=sub_category, slug=section_slug)
        content = get_object_or_404(Content, category=section, slug=content_slug)

        sub_categories = Category.objects.filter(parent=category)
        contents = Content.objects.filter(category__parent__parent=category)

        # serializers
        content = ContentSerializer(content, partial=True, context={'request': request})
        category = GenericCategorySerializer(category, partial=True)
        sub_category = GenericCategorySerializer(sub_category, partial=True)
        section = GenericCategorySerializer(section, partial=True)

        sub_categories = CategoryListSerializer(sub_categories, many=True)
        contents = ContentURLSerializer(contents, many=True)

        context = {
            'content': content.data,
            'category': category.data,
            'sub_category': sub_category.data,
            'section': section.data,

            'sub_categories': sub_categories.data,
            'contents': contents.data,
        }
        return Response(context, status=status.HTTP_200_OK)
