from rest_framework import serializers
from main.public.models import Headliner, News, Announcement, Vacancy, Event
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
    description_en = serializers.SerializerMethodField()
    description_ru = serializers.SerializerMethodField()
    description_kk = serializers.SerializerMethodField()

    class Meta:
        model = News
        exclude = ('title', 'description', )

    def get_description_en(self, obj):
        request = self.context.get('request')
        description = obj.description_en
        if request:
            description = description.replace('/media/', request.build_absolute_uri('/media/'))
        return description

    def get_description_ru(self, obj):
        request = self.context.get('request')
        description = obj.description_ru
        if request:
            description = description.replace('/media/', request.build_absolute_uri('/media/'))
        return description

    def get_description_kk(self, obj):
        request = self.context.get('request')
        description = obj.description_kk
        if request:
            description = description.replace('/media/', request.build_absolute_uri('/media/'))
        return description


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        exclude = ('title', 'description',)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ('title', 'description',)


class VacancySerializer(serializers.ModelSerializer):
    description_en = serializers.SerializerMethodField()
    description_ru = serializers.SerializerMethodField()
    description_kk = serializers.SerializerMethodField()

    class Meta:
        model = Vacancy
        exclude = ('title', 'description', )

    def get_description_en(self, obj):
        request = self.context.get('request')
        description = obj.description_en
        if request:
            description = description.replace('/media/', request.build_absolute_uri('/media/'))
        return description

    def get_description_ru(self, obj):
        request = self.context.get('request')
        description = obj.description_ru
        if request:
            description = description.replace('/media/', request.build_absolute_uri('/media/'))
        return description

    def get_description_kk(self, obj):
        request = self.context.get('request')
        description = obj.description_kk
        if request:
            description = description.replace('/media/', request.build_absolute_uri('/media/'))
        return description
