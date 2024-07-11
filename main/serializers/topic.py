from rest_framework import serializers
from main.models import Category, Topic, Chapter, Content


# Topic API
# ----------------------------------------------------------------------------------------------------------------------
class TopicExtendCategorySerializer(serializers.ModelSerializer):
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


# Topic
class TopicSerializer(serializers.ModelSerializer):
    category = TopicExtendCategorySerializer(read_only=True)

    class Meta:
        model = Topic
        exclude = ('name', 'description', 'src', )
