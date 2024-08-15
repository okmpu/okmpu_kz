from django.urls import path
from main.content.views import ContentDetail
from main.views import CategoryListAPIView, HomeAPIView
from main.public import views as main_views
from main.university import views as university_views

urlpatterns = [
    # main app urls...
    path('', HomeAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),

    # content app urls...
    path('content/<category_slug>/<sub_category_slug>/<section_slug>/<content_slug>/', ContentDetail.as_view()),

    # university apps urls...
    path('university/faculties/', university_views.FacultiesAPIView.as_view()),
    path('university/faculties/<slug>/', university_views.FacultyDetailAPIView.as_view()),
    path('university/faculties/<slug>/programs/', university_views.ProgramsFacultyAPIView.as_view()),

    # public app urls...
    path('public/news/', main_views.NewsAPIView.as_view()),
    path('public/news/<pk>/', main_views.NewsDetailAPIView.as_view()),
    path('public/announcements/', main_views.AnnouncementsAPIView.as_view()),
    path('public/announcements/<pk>/', main_views.AnnouncementDetailAPIView.as_view()),
    path('public/events/', main_views.EventsAPIView.as_view()),
    path('public/events/<pk>/', main_views.EventDetailAPIView.as_view()),
]
