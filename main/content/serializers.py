from rest_framework import serializers
from .models import Content, TextContent, FileContent, ImageContent, Category, StaffContent


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
    body_en = serializers.SerializerMethodField()
    body_ru = serializers.SerializerMethodField()
    body_kk = serializers.SerializerMethodField()

    class Meta:
        model = TextContent
        exclude = ('body', 'content', )

    def get_body_en(self, obj):
        request = self.context.get('request')
        body = obj.body_en
        if request and body:
            body = body.replace('/media/', request.build_absolute_uri('/media/'))
        return body

    def get_body_ru(self, obj):
        request = self.context.get('request')
        body = obj.body_ru
        if request and body:
            body = body.replace('/media/', request.build_absolute_uri('/media/'))
        return body

    def get_body_kk(self, obj):
        request = self.context.get('request')
        body = obj.body_kk
        if request and body:
            body = body.replace('/media/', request.build_absolute_uri('/media/'))
        return body


# FileContent
class FileContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileContent
        exclude = ('caption', 'content', )


# ImageContent
class ImageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageContent
        fields = ('id', 'image', )


# StaffContent
class StaffContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffContent
        exclude = ('full_name', 'profession', 'bio', 'content', )


# Content
class ContentSerializer(serializers.ModelSerializer):
    text_contents = TextContentSerializer(many=True)
    file_contents = FileContentSerializer(many=True)
    image_contents = ImageContentSerializer(many=True)
    staff_contents = StaffContentSerializer(many=True)

    class Meta:
        model = Content
        exclude = ('title', 'description', 'category', 'order', )


# Category
class GenericCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name_ru', 'name_en', 'name_kk', 'slug', )
