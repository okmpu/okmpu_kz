from rest_framework import serializers

from main.models import Category, Topic


# Context API
# ----------------------------------------------------------------------------------------------------------------------
# Category
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('name', 'index', 'slug', )


# Topic
class TopicExtendCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('name', 'index', 'slug', 'dropdown', )


class TopicListSerializer(serializers.ModelSerializer):
    category = TopicExtendCategorySerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'name_kk', 'name_ru', 'name_en', 'category', 'src', )
