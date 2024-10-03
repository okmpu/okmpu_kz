from django.shortcuts import get_object_or_404
from rest_framework import views, status, permissions
from rest_framework.response import Response
from django.db.models import Q

from main.public.models import News, Event, Announcement
from main.university.models import Faculty, Project, Department, Personal, FacultyProgram, Success
from main.university.serializers import FacultySerializer, DepartmentSerializer, ProjectSerializer, \
    PersonalSerializer, NewsSerializer, EventsSerializer, FacultyProgramSerializer, AboutFacultySerializer, \
    AboutDepartmentSerializer, SuccessSerializer


# Faculties API
class FacultiesAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        faculties = Faculty.objects.all()
        faculties = FacultySerializer(faculties, many=True, context={'request': request})
        context = {
            'faculties': faculties.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# FacultyDetail API
class FacultyDetailAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        faculty = get_object_or_404(Faculty, slug=slug)
        departments = Department.objects.filter(faculty=faculty)
        projects = Project.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
        achievements = Success.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
        personals = Personal.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
        news = News.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
        events = Event.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
        announcements = Announcement.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]

        faculty = FacultySerializer(faculty, partial=True, context={'request': request})
        departments = DepartmentSerializer(departments, many=True)
        projects = ProjectSerializer(projects, many=True, context={'request': request})
        achievements = SuccessSerializer(achievements, many=True, context={'request': request})
        personals = PersonalSerializer(personals, many=True, context={'request': request})
        news = NewsSerializer(news, many=True, context={'request': request})
        events = EventsSerializer(events, many=True, context={'request': request})
        announcements = NewsSerializer(announcements, many=True, context={'request': request})

        context = {
            'faculty': faculty.data,
            'departments': departments.data,
            'projects': projects.data,
            'achievements': achievements.data,
            'personals': personals.data,
            'news': news.data,
            'events': events.data,
            'announcements': announcements.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Faculty Programs API
class ProgramsFacultyAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        faculty = get_object_or_404(Faculty, slug=slug)
        departments = Department.objects.filter(faculty=faculty)
        programs = FacultyProgram.objects.filter(department__in=departments)
        programs = FacultyProgramSerializer(programs, many=True)
        context = {
            'programs': programs.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Faculty Projects API
class ProjectsFacultyAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        faculty = get_object_or_404(Faculty, slug=slug)
        departments = Department.objects.filter(faculty=faculty)
        projects = Project.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
        projects = ProjectSerializer(projects, many=True, context={'request': request})
        context = {
            'projects': projects.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Faculty Achievements API
class AchievementsFacultyAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        faculty = get_object_or_404(Faculty, slug=slug)
        departments = Department.objects.filter(faculty=faculty)
        achievements = Success.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
        achievements = ProjectSerializer(achievements, many=True, context={'request': request})
        context = {
            'achievements': achievements.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Faculty Personals API
class PersonalsFacultyAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        faculty = get_object_or_404(Faculty, slug=slug)
        departments = Department.objects.filter(faculty=faculty)
        managements = Personal.objects.filter(department__in=departments, p_type='MANAGEMENT')
        teachers = Personal.objects.filter(department__in=departments, p_type='TEACHER')
        students = Personal.objects.filter(department__in=departments, p_type='STUDENT')
        context = {
            'personals': [
                {
                    'id': 1,
                    'name_kk': 'Кафедра басшылығы',
                    'name_ru': 'Руководство кафедры',
                    'name_en': 'Department management',
                    'type': 'management',
                    'results': PersonalSerializer(managements, many=True, context={'request': request}).data
                },
                {
                    'id': 2,
                    'name_kk': 'Оқытушылар',
                    'name_ru': 'Преподаватели',
                    'name_en': 'Teachers',
                    'type': 'teachers',
                    'results': PersonalSerializer(teachers, many=True, context={'request': request}).data
                },
                {
                    'id': 3,
                    'name_kk': 'Студенттер',
                    'name_ru': 'Студенты',
                    'name_en': 'Students',
                    'type': 'students',
                    'results': PersonalSerializer(students, many=True, context={'request': request}).data
                },
            ]
        }
        return Response(context, status=status.HTTP_200_OK)


# FacultyDetail API
class PublicsFacultyAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        faculty = get_object_or_404(Faculty, slug=slug)
        departments = Department.objects.filter(faculty=faculty)
        news = News.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
        events = Event.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
        announcements = Announcement.objects.filter(Q(faculty=faculty) | Q(department__in=departments))

        news = NewsSerializer(news, many=True, context={'request': request})
        events = EventsSerializer(events, many=True, context={'request': request})
        announcements = NewsSerializer(announcements, many=True, context={'request': request})

        context = {
            'news': news.data,
            'events': events.data,
            'announcements': announcements.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# AboutFaculty API
class AboutFacultyAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        faculty = get_object_or_404(Faculty, slug=slug)
        about_faculty = AboutFacultySerializer(faculty, partial=True, context={'request': request})

        context = {
            'about': about_faculty.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# ----------------------------------------------------------------------------------------------------------------------
# DepartmentDetail API
class DepartmentDetailAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        department = get_object_or_404(Department, slug=slug)
        projects = Project.objects.filter(department=department)[:3]
        personals = Personal.objects.filter(department=department)[:3]
        news = News.objects.filter(department=department)[:3]
        events = Event.objects.filter(department=department)[:3]
        announcements = Announcement.objects.filter(department=department)[:3]

        department = DepartmentSerializer(department, partial=True, context={'request': request})
        projects = ProjectSerializer(projects, many=True, context={'request': request})
        personals = PersonalSerializer(personals, many=True, context={'request': request})
        news = NewsSerializer(news, many=True, context={'request': request})
        events = EventsSerializer(events, many=True, context={'request': request})
        announcements = NewsSerializer(announcements, many=True, context={'request': request})

        context = {
            'department': department.data,
            'projects': projects.data,
            'personals': personals.data,
            'news': news.data,
            'events': events.data,
            'announcements': announcements.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# DepartmentPrograms  API
class DepartmentProgramsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        department = get_object_or_404(Department, slug=slug)
        programs = FacultyProgram.objects.filter(department=department)
        programs = FacultyProgramSerializer(programs, many=True)
        context = {
            'programs': programs.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# DepartmentProjects API
class DepartmentProjectsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        department = get_object_or_404(Department, slug=slug)
        projects = Project.objects.filter(department=department)
        projects = ProjectSerializer(projects, many=True, context={'request': request})
        context = {
            'projects': projects.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Department Achievements API
class DepartmentAchievementsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        faculty = get_object_or_404(Faculty, slug=slug)
        departments = Department.objects.filter(faculty=faculty)
        achievements = Success.objects.filter(department__in=departments)
        achievements = ProjectSerializer(achievements, many=True, context={'request': request})
        context = {
            'achievements': achievements.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# DepartmentPersonals API
class DepartmentPersonalsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        department = get_object_or_404(Department, slug=slug)
        managements = Personal.objects.filter(department=department, p_type='MANAGEMENT')
        teachers = Personal.objects.filter(department=department, p_type='TEACHER')
        students = Personal.objects.filter(department=department, p_type='STUDENT')
        context = {
            'personals': [
                {
                    'id': 1,
                    'name_kk': 'Кафедра басшылығы',
                    'name_ru': 'Руководство кафедры',
                    'name_en': 'Department management',
                    'type': 'management',
                    'results': PersonalSerializer(managements, many=True, context={'request': request}).data
                },
                {
                    'id': 2,
                    'name_kk': 'Оқытушылар',
                    'name_ru': 'Преподаватели',
                    'name_en': 'Teachers',
                    'type': 'teachers',
                    'results': PersonalSerializer(teachers, many=True, context={'request': request}).data
                },
                {
                    'id': 3,
                    'name_kk': 'Студенттер',
                    'name_ru': 'Студенты',
                    'name_en': 'Students',
                    'type': 'students',
                    'results': PersonalSerializer(students, many=True, context={'request': request}).data
                },
            ]
        }
        return Response(context, status=status.HTTP_200_OK)


# DepartmentPublics API
class DepartmentPublicsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        department = get_object_or_404(Department, slug=slug)
        news = News.objects.filter(department=department)
        events = Event.objects.filter(department=department)
        announcements = Announcement.objects.filter(department=department)

        news = NewsSerializer(news, many=True, context={'request': request})
        events = EventsSerializer(events, many=True, context={'request': request})
        announcements = NewsSerializer(announcements, many=True, context={'request': request})

        context = {
            'news': news.data,
            'events': events.data,
            'announcements': announcements.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# AboutFaculty API
class DepartmentAboutAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        department = get_object_or_404(Department, slug=slug)

        about_department = AboutDepartmentSerializer(department, partial=True, context={'request': request})

        context = {
            'about': about_department.data,
        }
        return Response(context, status=status.HTTP_200_OK)
