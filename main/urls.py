from django.urls import path
from main.content.views import ContentDetail
from main.views import CategoryListAPIView, HomeAPIView
from main.public.views import NewsAPIView, NewsDetailAPIView, AnnouncementsAPIView, AnnouncementDetailAPIView, \
    EventsAPIView, EventDetailAPIView

urlpatterns = [
    # main app urls...
    path('', HomeAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),

    # content app urls...
    path('content/<category_slug>/<sub_category_slug>/<section_slug>/<content_slug>/', ContentDetail.as_view()),

    # public app urls...
    path('public/news/', NewsAPIView.as_view()),
    path('public/news/<pk>/', NewsDetailAPIView.as_view()),
    path('public/announcements/', AnnouncementsAPIView.as_view()),
    path('public/announcements/<pk>/', AnnouncementDetailAPIView.as_view()),
    path('public/events/', EventsAPIView.as_view()),
    path('public/events/<pk>/', EventDetailAPIView.as_view()),
]
