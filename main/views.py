from rest_framework import views, status, permissions
from rest_framework.response import Response

from main.content.models import Category, Content
from main.content.serializers import CategoryListSerializer, ContentURLSerializer
from main.public.models import Headliner, News, Announcement, Vacancy
from main.serializers import HeadlinerSerializer, NewsSerializer, AnnouncementSerializer, VacancySerializer, \
    ProgramListSerializer, FacultyListSerializer
from main.university.models import Program, Faculty


# Context API
class CategoryListAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        categories = Category.objects.filter(parent=None)
        contents = Content.objects.all()

        categories = CategoryListSerializer(categories, many=True)
        contents = ContentURLSerializer(contents, many=True)
        context = {
            'categories': categories.data,
            'contents': contents.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Home API View
class HomeAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        headliners = Headliner.objects.filter()[:3]
        programs = Program.objects.all()
        academics = Faculty.objects.all()[:8]
        # public
        news = News.objects.filter()[:3]
        announcements = Announcement.objects.filter()[:3]
        vacancies = Vacancy.objects.filter()[:3]

        # serializers
        headliners = HeadlinerSerializer(headliners, many=True, context={'request': request})
        programs = ProgramListSerializer(programs, many=True)
        academics = FacultyListSerializer(academics, many=True, context={'request': request})
        news = NewsSerializer(news, many=True, context={'request': request})
        announcements = AnnouncementSerializer(announcements, many=True, context={'request': request})
        vacancies = VacancySerializer(vacancies, many=True, context={'request': request})

        context = {
            'headliners': headliners.data,
            'programs': programs.data,
            'academics': academics.data,
            'news': news.data,
            'announcements': announcements.data,
            'vacancies': vacancies.data,
        }
        return Response(context, status=status.HTTP_200_OK)
