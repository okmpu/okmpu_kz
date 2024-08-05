from django.shortcuts import get_object_or_404
from rest_framework import status, views, permissions
from rest_framework.response import Response

from main.public.models import News, Announcement, Event
from main.public.serializers import NewsDetailSerializer, AnnouncementDetailSerializer, EventDetailSerializer
from main.serializers import NewsListSerializer, AnnouncementListSerializer, EventListSerializer


# News API
# ----------------------------------------------------------------------------------------------------------------------
class NewsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        news = News.objects.all()
        news = NewsListSerializer(news, many=True, context={'request': request})
        context = {
            'news': news.data
        }
        return Response(context, status=status.HTTP_200_OK)


class NewsDetailAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        news = get_object_or_404(News, pk=pk)
        similar_news = News.objects.filter(user=news.user)[:8]
        news = NewsDetailSerializer(news, partial=True, context={'request': request})
        similar_news = NewsListSerializer(similar_news, many=True)

        context = {
            'news': news.data,
            'similar_news': similar_news.data
        }
        return Response(context, status=status.HTTP_200_OK)


# Announcement API
# ----------------------------------------------------------------------------------------------------------------------
class AnnouncementsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        announcements = Announcement.objects.all()
        announcements = AnnouncementListSerializer(announcements, many=True, context={'request': request})
        context = {
            'announcements': announcements.data
        }
        return Response(context, status=status.HTTP_200_OK)


class AnnouncementDetailAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        announcement = get_object_or_404(Announcement, pk=pk)
        announcement = AnnouncementDetailSerializer(announcement, partial=True, context={'request': request})
        return Response(announcement.data, status=status.HTTP_200_OK)


# News API
# ----------------------------------------------------------------------------------------------------------------------
class EventsAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        events = Event.objects.all()
        events = EventListSerializer(events, many=True, context={'request': request})
        context = {
            'events': events.data
        }
        return Response(context, status=status.HTTP_200_OK)


class EventDetailAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        event = EventDetailSerializer(event, partial=True, context={'request': request})
        context = {
            'event': event.data
        }
        return Response(context, status=status.HTTP_200_OK)
