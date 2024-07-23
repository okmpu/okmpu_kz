from rest_framework import views, status, permissions
from rest_framework.response import Response

from main.public.models import Headliner, News, Announcement, Vacancy
from main.public.serializers import HeadlinerSerializer, NewsSerializer, AnnouncementSerializer, VacancySerializer


class HomeAPIView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        headliners = Headliner.objects.filter()[:3]
        news = News.objects.filter()[:3]
        announcements = Announcement.objects.filter()[:3]
        vacancies = Vacancy.objects.filter()[:3]

        # data
        headliners = HeadlinerSerializer(headliners, many=True, context={'request': request})
        news = NewsSerializer(news, many=True, context={'request': request})
        announcements = AnnouncementSerializer(announcements, many=True, context={'request': request})
        vacancies = VacancySerializer(vacancies, many=True, context={'request': request})

        context = {
            'headliners': headliners.data,
            'news': news.data,
            'announcements': announcements.data,
            'vacancies': vacancies.data,
        }
        return Response(context, status=status.HTTP_200_OK)
