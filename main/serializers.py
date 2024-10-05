from django.contrib.auth.models import User
from rest_framework import serializers
from main.public.models import Headliner, News, Announcement, Vacancy, Event, Program, Journal, Partner
from main.university.models import Faculty


# Carousel section
# ----------------------------------------------------------------------------------------------------------------------
class HeadlinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headliner
        exclude = ('title', 'about', )


# Admission section
# ----------------------------------------------------------------------------------------------------------------------
class ProgramListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        exclude = ('name', )


# Public section
# ----------------------------------------------------------------------------------------------------------------------
# Author
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', )


# News
class NewsListSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title_ru', 'title_en', 'title_kk', 'poster', 'user', 'date_created', )


# Announcements
class AnnouncementListSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only=True)

    class Meta:
        model = Announcement
        fields = ('id', 'title_ru', 'title_en', 'title_kk', 'user', 'date_created', )


# Events
class EventListSerializer(serializers.ModelSerializer):
    user = AuthorSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'title_ru', 'title_en', 'title_kk', 'poster', 'user', 'date_created', )


# Journals section
# ----------------------------------------------------------------------------------------------------------------------
class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = ('id', 'title', 'poster', 'file', 'date_created', )


# Partners section
# ----------------------------------------------------------------------------------------------------------------------
class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partner
        fields = ('id', 'name', 'poster', 'url', 'order', )


# Academics section
# ----------------------------------------------------------------------------------------------------------------------
class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'name_ru', 'name_kk', 'name_en', 'slug', 'image',)
