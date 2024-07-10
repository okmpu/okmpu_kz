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
        fields = ('id', 'name_kk', 'name_ru', 'name_en', 'slug', )


class ChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'name_kk', 'name_ru', 'name_en', 'slug', 'multiple_content', 'index', )


class ContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'title_kk', 'title_ru', 'title_en', 'chapter', 'slug', 'index', )


class TopicSerializer(serializers.ModelSerializer):
    category = TopicCategorySerializer(read_only=True)

    class Meta:
        model = Topic
        exclude = ('name', )


# Content API
class ContentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_kk', 'name_ru', 'name_en', 'slug', )


class ContentTopicSerializer(serializers.ModelSerializer):
    category = ContentCategorySerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'name_kk', 'name_ru', 'name_en', 'category', 'slug', )


class ContentChapterSerializer(serializers.ModelSerializer):
    topic = ContentTopicSerializer(read_only=True)

    class Meta:
        model = Chapter
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    chapter = ContentChapterSerializer(read_only=True)

    class Meta:
        model = Content
        exclude = ('title', )
