from rest_framework import views, status, permissions
from rest_framework.response import Response

from main.content.models import Category
from main.content.serializers import CategoryListSerializer
from main.public.models import Headliner, News, Announcement, Event
from main.serializers import HeadlinerSerializer, NewsListSerializer, AnnouncementListSerializer, \
    ProgramListSerializer, FacultyListSerializer, EventListSerializer
from main.university.models import Program, Faculty


# Context API
# ----------------------------------------------------------------------------------------------------------------------
class CategoryListAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        categories = Category.objects.filter(parent=None)
        academics = Faculty.objects.all()[:6]

        categories = CategoryListSerializer(categories, many=True)
        academics = FacultyListSerializer(academics, many=True, context={'request': request})
        context = {
            'categories': categories.data,
            'academics': academics.data
        }
        return Response(context, status=status.HTTP_200_OK)


# Home API View
# ----------------------------------------------------------------------------------------------------------------------
class HomeAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        headliners = Headliner.objects.filter()[:3]
        programs = Program.objects.all()
        # public
        news = News.objects.filter()[:6]
        announcements = Announcement.objects.filter()[:6]
        events = Event.objects.filter()[:4]
        academics = Faculty.objects.all()[:6]

        # serializers
        headliners = HeadlinerSerializer(headliners, many=True, context={'request': request})
        programs = ProgramListSerializer(programs, many=True)
        news = NewsListSerializer(news, many=True, context={'request': request})
        announcements = AnnouncementListSerializer(announcements, many=True)
        events = EventListSerializer(events, many=True, context={'request': request})
        academics = FacultyListSerializer(academics, many=True, context={'request': request})

        context = {
            'headliners': headliners.data,
            'programs': programs.data,
            'news': news.data,
            'announcements': announcements.data,
            'events': events.data,
            'academics': academics.data,
        }
        return Response(context, status=status.HTTP_200_OK)
