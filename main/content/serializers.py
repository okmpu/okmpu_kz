from rest_framework import serializers
from .models import Content, TextContent, FileContent, ImageContent, ContentItem, Category


# CategoryList serializers
# ----------------------------------------------------------------------------------------------------------------------
class CategoryListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    app_name = serializers.SerializerMethodField()

    class Meta:
        model = Category
        exclude = ('name', 'parent', 'order',)

    def get_children(self, obj):
        children_qs = Category.objects.filter(parent=obj)
        children_serializer = CategoryListSerializer(children_qs, many=True, context=self.context)
        return children_serializer.data

    def get_app_name(self, obj):
        return obj.app_name


# Content list serializers
class ContentURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'title_kk', 'title_ru', 'title_en', 'category', 'slug', )


# ContentDetail serializers
# ----------------------------------------------------------------------------------------------------------------------
# TextContent
class TextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        exclude = ('id', 'body', 'content', )


# FileContent
class FileContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileContent
        exclude = ('caption', 'content', )

    def get_file_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.file.url)
        return obj.file.url


# ImageContent
class ImageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageContent
        fields = ('id', 'image', )

    def get_image_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url


# ContentItem
class ContentItemSerializer(serializers.ModelSerializer):
    content_object = serializers.SerializerMethodField()

    class Meta:
        model = ContentItem
        fields = ('id', 'order', 'content_object', )

    def get_content_object(self, obj):
        context = self.context
        if obj.content_type.model == 'textcontent':
            return {
                'type': 'text_content',
                'content': TextContentSerializer(obj.content_object, context=context).data
            }
        elif obj.content_type.model == 'filecontent':
            return {
                'type': 'file_content',
                'content': FileContentSerializer(obj.content_object, context=context).data
            }
        elif obj.content_type.model == 'imagecontent':

            return {
                'type': 'image_content',
                'content': ImageContentSerializer(obj.content_object, context=context).data
            }


# Content
class ContentSerializer(serializers.ModelSerializer):
    items = ContentItemSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        exclude = ('title', 'description', 'category', 'order', )


# Category
class GenericCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name_ru', 'name_en', 'name_kk', 'slug', )
