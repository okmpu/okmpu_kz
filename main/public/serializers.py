from rest_framework import serializers

from main.public.models import Headliner, News, Announcement, Vacancy


class HeadlinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headliner
        exclude = ('title', 'about', )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ('title', 'description', )


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        exclude = ('title', 'description', )


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ('title', 'description', )
        