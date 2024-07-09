from rest_framework import serializers
from main.models import Category, Topic, Chapter, Content


# Context API
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_kk', 'name_ru', 'name_en', 'index', 'src', 'dropdown', )


class TopicListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'category', 'name_kk', 'name_ru', 'name_en', 'index', 'src', )


# Topic API
class TopicCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_kk', 'name_ru', 'name_en', )


class TopicSerializer(serializers.ModelSerializer):
    category = TopicCategorySerializer(read_only=True)

    class Meta:
        model = Topic
        exclude = ('name', )


class ChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'name_kk', 'name_ru', 'name_en', 'slug', 'multiple_content', 'index', )


class ContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'title_kk', 'title_ru', 'title_en', 'chapter', 'slug', 'index', )
