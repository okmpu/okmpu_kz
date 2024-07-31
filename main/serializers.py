from rest_framework import serializers
from main.public.models import Headliner, News, Announcement, Vacancy
from main.university.models import Program, Faculty


# Carousel section
class HeadlinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headliner
        exclude = ('title', 'about', )


# Admission section
class ProgramListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        exclude = ('name', 'departments', )


# Academics
class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'name_ru', 'name_kk', 'name_en', 'slug', 'image',)


# Public section
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ('title', 'description',)


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        exclude = ('title', 'description',)


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ('title', 'description',)
