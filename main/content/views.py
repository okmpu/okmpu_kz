from django.shortcuts import get_object_or_404
from rest_framework import views, permissions, status
from rest_framework.response import Response

from .models import Category, Content, TextContent
from .serializers import CategoryListSerializer, ContentURLSerializer, ContentSerializer, GenericCategorySerializer, \
    TextContentSerializer


class CategoryListAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        categories = Category.objects.filter(parent=None)
        contents = Content.objects.all()

        categories = CategoryListSerializer(categories, many=True)
        contents = ContentURLSerializer(contents, many=True)
        context = {
            'categories': categories.data,
            'contents': contents.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# ContentDetail
class ContentDetail(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, category_slug, sub_category_slug, section_slug, content_slug):
        category = get_object_or_404(Category, slug=category_slug)
        sub_category = get_object_or_404(Category, slug=sub_category_slug)
        section = get_object_or_404(Category, slug=section_slug)
        content = get_object_or_404(Content, slug=content_slug)
        text_contents = TextContent.objects.filter(content=content)

        # navigation
        sub_categories = Category.objects.filter(parent=category)
        contents = Content.objects.all()

        category = GenericCategorySerializer(category, partial=True)
        sub_category = GenericCategorySerializer(sub_category, partial=True)
        section = GenericCategorySerializer(section, partial=True)
        content = ContentSerializer(content, partial=True)
        text_contents = TextContentSerializer(text_contents, many=True)

        sub_categories = CategoryListSerializer(sub_categories, many=True)
        contents = ContentURLSerializer(contents, many=True)

        context = {
            'category': category.data,
            'sub_category': sub_category.data,
            'section': section.data,
            'content': content.data,
            'text_contents': text_contents.data,

            'sub_categories': sub_categories.data,
            'contents': contents.data,
        }
        return Response(context, status=status.HTTP_200_OK)
