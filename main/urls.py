from django.urls import path
from main.content.views import ContentDetail, content_detail
from main import views
from main.public import views as main_views
from main.university import views as university_views

urlpatterns = [
    path('', views.home, name='home'),

    # content urls
    path('content/<category_slug>/<sub_category_slug>/<section_slug>/<content_slug>/', content_detail, name='content_detail'),


    # API
    # ------------------------------------------------------------------------------------------------------------------
    # main app urls...
    path('api/main/', views.HomeAPIView.as_view()),
    path('api/main/categories/', views.CategoryListAPIView.as_view()),
    path('api/main/program/<slug>/', views.ProgramAPIView.as_view()),

    # content app urls...

    path('api/main/content/<category_slug>/<sub_category_slug>/<section_slug>/<content_slug>/', ContentDetail.as_view()),

    # university apps urls...
    path('api/main/university/faculties/', university_views.FacultiesAPIView.as_view()),
    path('api/main/university/faculties/<slug>/', university_views.FacultyDetailAPIView.as_view()),
    path('api/main/university/faculties/<slug>/programs/', university_views.ProgramsFacultyAPIView.as_view()),
    path('api/main/university/faculties/<slug>/projects/', university_views.ProjectsFacultyAPIView.as_view()),
    path('api/main/university/faculties/<slug>/achievements/', university_views.AchievementsFacultyAPIView.as_view()),
    path('api/main/university/faculties/<slug>/personals/', university_views.PersonalsFacultyAPIView.as_view()),
    path('api/main/university/faculties/<slug>/publics/', university_views.PublicsFacultyAPIView.as_view()),
    path('api/main/university/faculties/<slug>/about/', university_views.AboutFacultyAPIView.as_view()),

    path('api/main/university/departments/<slug>/', university_views.DepartmentDetailAPIView.as_view()),
    path('api/main/university/departments/<slug>/programs/', university_views.DepartmentProgramsAPIView.as_view()),
    path('api/main/university/departments/<slug>/projects/', university_views.DepartmentProjectsAPIView.as_view()),
    path('api/main/university/departments/<slug>/achievements/', university_views.DepartmentAchievementsAPIView.as_view()),
    path('api/main/university/departments/<slug>/personals/', university_views.DepartmentPersonalsAPIView.as_view()),
    path('api/main/university/departments/<slug>/publics/', university_views.DepartmentPublicsAPIView.as_view()),
    path('api/main/university/departments/<slug>/about/', university_views.DepartmentAboutAPIView.as_view()),

    # public app urls...
    path('api/main/public/news/', main_views.NewsAPIView.as_view()),
    path('api/main/public/news/<pk>/', main_views.NewsDetailAPIView.as_view()),
    path('api/main/public/announcements/', main_views.AnnouncementsAPIView.as_view()),
    path('api/main/public/announcements/<pk>/', main_views.AnnouncementDetailAPIView.as_view()),
    path('api/main/public/events/', main_views.EventsAPIView.as_view()),
    path('api/main/public/events/<pk>/', main_views.EventDetailAPIView.as_view()),
]
