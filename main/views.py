from django.shortcuts import get_object_or_404
from rest_framework import views, permissions, status
from rest_framework.response import Response

from main.models import Category, Topic, Chapter, Content
from main.serializers.generics import CategorySerializer, TopicSerializer, TopicListSerializer, ChapterListSerializer, \
    ContentListSerializer, ContentSerializer


# Generic context API
class ContextAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        categories = Category.objects.all()
        topics = Topic.objects.all()

        categories = CategorySerializer(categories, many=True)
        topics = TopicListSerializer(topics, many=True)

        context = {
            'categories': categories.data,
            'topics': topics.data
        }
        return Response(context, status=status.HTTP_200_OK)


# Topic API
class TopicAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug, topic_slug):
        category = get_object_or_404(Category, slug=slug)
        topic = get_object_or_404(Topic, slug=topic_slug)
        chapters = Chapter.objects.filter(topic=topic)
        contents = Content.objects.filter(chapter__in=chapters)

        topic = TopicSerializer(topic, partial=True)
        chapters = ChapterListSerializer(chapters, many=True)
        contents = ContentListSerializer(contents, many=True)

        context = {
            'topic': topic.data,
            'chapters': chapters.data,
            'contents': contents.data
        }
        return Response(context, status=status.HTTP_200_OK)


# Content API
class ContentAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug, topic_slug, chapter_slug, content_slug):
        category = get_object_or_404(Category, slug=slug)
        topic = get_object_or_404(Topic, slug=topic_slug)
        chapter = get_object_or_404(Chapter, slug=chapter_slug)
        content = get_object_or_404(Content, slug=content_slug)

        chapters = Chapter.objects.filter(topic=topic)
        contents = Content.objects.filter(chapter__in=chapters)

        content = ContentSerializer(content, partial=True)
        chapters = ChapterListSerializer(chapters, many=True)
        contents = ContentListSerializer(contents, many=True)

        context = {
            'content': content.data,

            'chapters': chapters.data,
            'contents': contents.data
        }
        return Response(context, status=status.HTTP_200_OK)
