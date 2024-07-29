from rest_framework import serializers
from .models import Category, Content, TextContent, PopupContent, FileContent


class CategoryListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    app_name = serializers.SerializerMethodField()

    class Meta:
        model = Category
        exclude = ('name', 'parent', 'index',)

    def get_children(self, obj):
        children_qs = Category.objects.filter(parent=obj)
        children_serializer = CategoryListSerializer(children_qs, many=True, context=self.context)
        return children_serializer.data

    def get_app_name(self, obj):
        return obj.app_name


class ContentURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'title_kk', 'title_ru', 'title_en', 'category', 'slug', )


# ContentDetail API serializers
# ----------------------------------------------------------------------------------------------------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_kk', 'name_ru', 'name_en', 'slug', 'multiple', )


class GenericCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_kk', 'name_ru', 'name_en', 'slug', )


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        exclude = ('title', 'description', 'category', )


class TextContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        exclude = ('description', )


class PopupContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopupContent
        exclude = ('trigger', 'description', )


class FileContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileContent
        exclude = ('caption', )
