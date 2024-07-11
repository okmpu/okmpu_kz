from rest_framework import serializers
from main.models import Category, Topic, Chapter, Content


# Content API
# ----------------------------------------------------------------------------------------------------------------------
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


# Content
class ContentSerializer(serializers.ModelSerializer):
    chapter = ContentChapterSerializer(read_only=True)

    class Meta:
        model = Content
        exclude = ('title', )
