from django.contrib.auth.models import User
from rest_framework import serializers
from main.public.models import News, Announcement, Event, Program, Specialty, NewsFile, AnnouncementFile, EventFile


# Author
# ----------------------------------------------------------------------------------------------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', )


# News
# ----------------------------------------------------------------------------------------------------------------------
class NewFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsFile
        fields = ('id', 'title', 'file', )


class NewsDetailSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only=True)
    news_files = NewFileSerializer(many=True)
    description_en = serializers.SerializerMethodField()
    description_ru = serializers.SerializerMethodField()
    description_kk = serializers.SerializerMethodField()

    class Meta:
        model = News
        exclude = ('title', 'description', 'department', )

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


# Announcement
# ----------------------------------------------------------------------------------------------------------------------
class AnnouncementFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnouncementFile
        fields = ('id', 'title', 'file', )


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only=True)
    announcement_files = AnnouncementFileSerializer(many=True)
    description_en = serializers.SerializerMethodField()
    description_ru = serializers.SerializerMethodField()
    description_kk = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        exclude = ('title', 'description', 'department',)

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


# Events
# ----------------------------------------------------------------------------------------------------------------------
class EventFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventFile
        fields = ('id', 'title', 'file', )


class EventDetailSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only=True)
    event_files = EventFileSerializer(many=True)
    description_en = serializers.SerializerMethodField()
    description_ru = serializers.SerializerMethodField()
    description_kk = serializers.SerializerMethodField()

    class Meta:
        model = Event
        exclude = ('title', 'description', 'department',)

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


# Program
# ----------------------------------------------------------------------------------------------------------------------
class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        exclude = ('name', )


class ProgramSerializer(serializers.ModelSerializer):
    program_items = SpecialtySerializer(many=True)

    class Meta:
        model = Program
        exclude = ('name', )
