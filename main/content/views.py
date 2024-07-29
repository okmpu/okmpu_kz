from django.shortcuts import get_object_or_404
from rest_framework import views, permissions, status
from rest_framework.response import Response

from .models import Category, Content, TextContent, PopupContent, FileContent
from .serializers import CategoryListSerializer, ContentURLSerializer, ContentSerializer, GenericCategorySerializer, \
    TextContentSerializer, PopupContentSerializer, FileContentSerializer


# ContentDetail
class ContentDetail(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, category_slug, sub_category_slug, section_slug, content_slug):
        category = get_object_or_404(Category, slug=category_slug)
        sub_category = get_object_or_404(Category, slug=sub_category_slug)
        section = get_object_or_404(Category, slug=section_slug)

        # Sidebar
        sub_categories = Category.objects.filter(parent=category)
        contents = Content.objects.all()

        # Content
        content = get_object_or_404(Content, slug=content_slug)
        text_contents = TextContent.objects.filter(content=content)
        popup_contents = PopupContent.objects.filter(content=content)
        file_contents = FileContent.objects.filter(content=content)

        # Serializers
        # --------------------------------------------------------------------------------------------------------------
        category = GenericCategorySerializer(category, partial=True)
        sub_category = GenericCategorySerializer(sub_category, partial=True)
        section = GenericCategorySerializer(section, partial=True)

        # Sidebar
        sub_categories = CategoryListSerializer(sub_categories, many=True)
        contents = ContentURLSerializer(contents, many=True)

        # Content
        content = ContentSerializer(content, partial=True)
        text_contents = TextContentSerializer(text_contents, many=True)
        popup_contents = PopupContentSerializer(popup_contents, many=True)
        file_contents = FileContentSerializer(file_contents, many=True, context={'request': request})

        context = {
            # Sidebar
            'sub_categories': sub_categories.data,
            'contents': contents.data,

            'category': category.data,
            'sub_category': sub_category.data,
            'section': section.data,
            # Content
            'content': content.data,
            'text_contents': text_contents.data,
            'popup_contents': popup_contents.data,
            'file_contents': file_contents.data,

        }
        return Response(context, status=status.HTTP_200_OK)
