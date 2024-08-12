from rest_framework import serializers

from main.public.models import News
from main.university.models import Faculty, Department, Program, Project, Personal


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        exclude = ('name', 'about',)


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        exclude = ('name', 'departments', )


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        exclude = ('name', 'about', 'faculty', )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('name', 'author', 'department', )


class PersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personal
        exclude = ('department', 'profession', 'about', )


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        exclude = ('title', 'description', 'department', 'user', )
