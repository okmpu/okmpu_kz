from django.shortcuts import get_object_or_404, render
from rest_framework import views, status, permissions
from rest_framework.response import Response

from main.content.models import Category
from main.content.serializers import CategoryListSerializer
from main.public.models import Headliner, News, Announcement, Event, Program, Journal, Partner
from main.public.serializers import ProgramSerializer
from main.serializers import HeadlinerSerializer, NewsListSerializer, AnnouncementListSerializer, \
    FacultyListSerializer, EventListSerializer, ProgramListSerializer, JournalSerializer, PartnerSerializer
from main.university.models import Faculty


# Home page
# ----------------------------------------------------------------------------------------------------------------------
def home(request):
    headliners = Headliner.objects.filter()[:5]
    programs = Program.objects.all()
    news = News.objects.filter()[:6]
    announcements = Announcement.objects.filter()[:6]
    events = Event.objects.filter()[:4]
    journals = Journal.objects.filter()[:6]
    academics = Faculty.objects.all()[:6]
    partners = Partner.objects.all()

    context = {
        'headliners': headliners,
        'programs': programs,
        'news': news,
        'announcements': announcements,
        'events': events,
        'journals': journals,
        'academics': academics,
        'partners': partners
    }
    return render(request, 'src/index.html', context)


# Program page
# ----------------------------------------------------------------------------------------------------------------------
def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug)

    context = {
        'program': program
    }
    return render(request, 'src/programs.html', context)


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
        headliners = Headliner.objects.filter()[:5]
        programs = Program.objects.all()
        # public
        news = News.objects.filter()[:6]
        announcements = Announcement.objects.filter()[:6]
        events = Event.objects.filter()[:4]
        journals = Journal.objects.filter()[:6]
        academics = Faculty.objects.all()[:6]
        partners = Partner.objects.all()

        # serializers
        headliners = HeadlinerSerializer(headliners, many=True, context={'request': request})
        programs = ProgramListSerializer(programs, many=True)
        news = NewsListSerializer(news, many=True, context={'request': request})
        announcements = AnnouncementListSerializer(announcements, many=True)
        events = EventListSerializer(events, many=True, context={'request': request})
        journals = JournalSerializer(journals, many=True, context={'request': request})
        academics = FacultyListSerializer(academics, many=True, context={'request': request})
        partners = PartnerSerializer(partners, many=True, context={'request': request})

        context = {
            'headliners': headliners.data,
            'programs': programs.data,
            'news': news.data,
            'announcements': announcements.data,
            'events': events.data,
            'journals': journals.data,
            'academics': academics.data,
            'partners': partners.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Program API View
# ----------------------------------------------------------------------------------------------------------------------
class ProgramAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        program = get_object_or_404(Program, slug=slug)
        program = ProgramSerializer(program, partial=True)

        context = {
            'program': program.data
        }
        return Response(context, status=status.HTTP_200_OK)
