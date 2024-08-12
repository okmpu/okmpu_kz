from rest_framework import serializers
from main.public.models import News, Announcement, Event


# News
# ----------------------------------------------------------------------------------------------------------------------
class NewsDetailSerializer(serializers.ModelSerializer):
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
class AnnouncementDetailSerializer(serializers.ModelSerializer):
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
class EventDetailSerializer(serializers.ModelSerializer):
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
