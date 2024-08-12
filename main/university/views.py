from django.shortcuts import get_object_or_404
from rest_framework import views, status, permissions
from rest_framework.response import Response

from main.public.models import News
from main.university.models import Faculty, Program, Project, Department, Personal
from main.university.serializers import FacultySerializer, ProgramSerializer, DepartmentSerializer, ProjectSerializer, \
    PersonalSerializer, NewsSerializer


class FacultiesAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        faculties = Faculty.objects.all()
        faculties = FacultySerializer(faculties, many=True, context={'request': request})
        context = {
            'faculties': faculties.data,
        }
        return Response(context, status=status.HTTP_200_OK)


class FacultyDetailAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        faculty = get_object_or_404(Faculty, slug=slug)
        programs = Program.objects.all()
        departments = Department.objects.filter(faculty=faculty)
        projects = Project.objects.filter(department__in=departments)
        personals = Personal.objects.filter(department__in=departments)
        news = News.objects.filter(department__in=departments)

        faculty = FacultySerializer(faculty, partial=True, context={'request': request})
        programs = ProgramSerializer(programs, many=True)
        departments = DepartmentSerializer(departments, many=True)
        projects = ProjectSerializer(projects, many=True, context={'request': request})
        personals = PersonalSerializer(personals, many=True, context={'request': request})
        news = NewsSerializer(news, many=True, context={'request': request})

        context = {
            'faculty': faculty.data,
            'programs': programs.data,
            'departments': departments.data,
            'projects': projects.data,
            'personals': personals.data,
            'news': news.data,
        }
        return Response(context, status=status.HTTP_200_OK)
