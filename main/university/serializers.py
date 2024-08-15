from django.contrib.auth.models import User
from rest_framework import serializers

from main.public.models import News, Event
from main.university.models import Faculty, Department, Project, Personal, FacultySpecialty, FacultyProgram


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        exclude = ('name', 'about', )


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        exclude = ('name', 'about', 'faculty', )


# Programs
class FacultySpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultySpecialty
        exclude = ('name', )


class FacultyProgramSerializer(serializers.ModelSerializer):
    program_items = FacultySpecialtySerializer(many=True)

    class Meta:
        model = FacultyProgram
        exclude = ('name', 'department', )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('name', 'author', 'department', )


# Personal
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email' )


class PersonalSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Personal
        exclude = ('department', 'profession', 'about', )


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        exclude = ('title', 'description', 'department', 'user', )


class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        exclude = ('title', 'description', 'department', 'user', )
