from django.shortcuts import get_object_or_404
from rest_framework import status, views, permissions
from rest_framework.response import Response
from django.db.models import Q
from main.public.models import News, Announcement, Event
from main.public.serializers import NewsDetailSerializer, AnnouncementDetailSerializer, EventDetailSerializer
from main.serializers import NewsListSerializer, AnnouncementListSerializer, EventListSerializer


# News API
# ----------------------------------------------------------------------------------------------------------------------
class NewsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        search_query = request.query_params.get('search', None)
        if search_query:
            news = News.objects.filter(
                Q(title_en__icontains=search_query) | Q(title_ru__icontains=search_query) |
                Q(title_kk__icontains=search_query)
            )
        else:
            news = News.objects.all()
        news = NewsListSerializer(news, many=True, context={'request': request})
        context = {
            'code': 'news',
            'news': news.data
        }
        return Response(context, status=status.HTTP_200_OK)


class NewsDetailAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        similar_news = News.objects.exclude(pk=news.id).filter(user=news.user)[:8]
        news = NewsDetailSerializer(news, partial=True, context={'request': request})
        similar_news = NewsListSerializer(similar_news, many=True, context={'request': request})

        context = {
            'news': news.data,
            'code': 'news',
            'similar_news': similar_news.data
        }
        return Response(context, status=status.HTTP_200_OK)


# Announcement API
# ----------------------------------------------------------------------------------------------------------------------
class AnnouncementsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        search_query = request.query_params.get('search', None)
        if search_query:
            announcements = Announcement.objects.filter(
                Q(title_en__icontains=search_query) | Q(title_ru__icontains=search_query) |
                Q(title_kk__icontains=search_query)
            )
        else:
            announcements = Announcement.objects.all()
        announcements = AnnouncementListSerializer(announcements, many=True, context={'request': request})
        context = {
            'code': 'announcements',
            'announcements': announcements.data
        }
        return Response(context, status=status.HTTP_200_OK)


class AnnouncementDetailAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        announcement = get_object_or_404(Announcement, pk=pk)
        announcements = Announcement.objects.exclude(pk=announcement.id).filter(user=announcement.user)

        announcement = AnnouncementDetailSerializer(announcement, partial=True, context={'request': request})
        announcements = AnnouncementListSerializer(announcements, many=True, context={'request': request})
        context = {
            'announcement': announcement.data,
            'code': 'announcements',
            'announcements': announcements.data
        }
        return Response(context, status=status.HTTP_200_OK)


# Events API
# ----------------------------------------------------------------------------------------------------------------------
class EventsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        search_query = request.query_params.get('search', None)
        if search_query:
            events = Event.objects.filter(
                Q(title_en__icontains=search_query) | Q(title_ru__icontains=search_query) |
                Q(title_kk__icontains=search_query)
            )
        else:
            events = Event.objects.all()
        events = EventListSerializer(events, many=True, context={'request': request})
        context = {
            'code': 'events',
            'events': events.data
        }
        return Response(context, status=status.HTTP_200_OK)


class EventDetailAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        events = Event.objects.exclude(pk=event.id).filter(user=event.user)
        event = EventDetailSerializer(event, partial=True, context={'request': request})
        events = EventListSerializer(events, many=True, context={'request': request})

        context = {
            'event': event.data,
            'code': 'all-events',
            'events': events.data
        }
        return Response(context, status=status.HTTP_200_OK)
