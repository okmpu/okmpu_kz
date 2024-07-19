from django.shortcuts import get_object_or_404
from rest_framework import views, permissions, status
from rest_framework.response import Response

from main.content.models import Section, Subsection, Chapter, Content
from main.content.serializers import SectionListSerializer, SubsectionListSerializer


# Context API
class ContextAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        sections = Section.objects.all()
        sub_sections = Subsection.objects.all()

        sections = SectionListSerializer(sections, many=True)
        sub_sections = SubsectionListSerializer(sub_sections, many=True)

        context = {
            'sections': sections.data,
            'sub_sections': sub_sections.data
        }
        return Response(context, status=status.HTTP_200_OK)


# Section API
class SubsectionAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug, topic_slug):
        section = get_object_or_404(Section, slug=slug)
        sub_section = get_object_or_404(Subsection, slug=topic_slug)
        chapters = Chapter.objects.filter(section=section, sub_section=sub_section)
        contents = Content.objects.filter(sub_section=sub_section, chapter__in=chapters)

        # topic = TopicSerializer(topic, partial=True, context={'request': request})
        # chapters = ChapterListSerializer(chapters, many=True)
        # contents = ContentListSerializer(contents, many=True)

        context = {
            # 'topic': topic.data,
            # 'chapters': chapters.data,
            # 'contents': contents.data
        }
        return Response(context, status=status.HTTP_200_OK)

