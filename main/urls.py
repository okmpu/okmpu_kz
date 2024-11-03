from django.urls import path
from main.content.views import ContentDetail, content_detail
from main import views
from main.public import views as main_views
from main.university import views as university_views

urlpatterns = [
    path('', views.home, name='home'),
    path('programs/<slug>/', views.program_detail, name='program_detail'),

    # public app urls...
    path('publics/news/', main_views.news_view, name='news'),
    path('publics/news/<pk>/', main_views.news_view, name='news_detail'),
    path('publics/announcements/', main_views.announcement_view, name='announcements'),
    path('publics/announcements/<pk>/', main_views.announcement_view, name='announcement'),
    path('publics/events/', main_views.event_view, name='events'),
    path('publics/events/<pk>/', main_views.event_view, name='event_detail'),

    # content urls
    path('content/<category_slug>/<sub_category_slug>/<section_slug>/<content_slug>/', content_detail, name='content_detail'),

    # university apps urls...
    path('university/faculties/', university_views.faculties_view, name='faculties'),
    path('university/faculties/<slug>/', university_views.faculty_detail_view, name='faculty_detail'),
    path('university/faculties/<slug>/programs/', university_views.faculty_programs_view, name='faculty_programs'),
    path('university/faculties/<slug>/projects/', university_views.faculty_projects_view, name='faculty_projects'),
    path('university/faculties/<slug>/achievements/', university_views.faculty_achievements_view, name='faculty_achievements'),
    path('university/faculties/<slug>/personals/', university_views.faculty_personals_view, name='faculty_personals'),
    path('university/faculties/<slug>/publics/', university_views.faculty_publics_view, name='faculty_publics'),
    path('university/faculties/<slug>/about/', university_views.faculty_about_view, name='faculty_about'),

    # API
    # ------------------------------------------------------------------------------------------------------------------
    # university apps urls...
    path('api/main/university/departments/<slug>/', university_views.DepartmentDetailAPIView.as_view()),
    path('api/main/university/departments/<slug>/programs/', university_views.DepartmentProgramsAPIView.as_view()),
    path('api/main/university/departments/<slug>/projects/', university_views.DepartmentProjectsAPIView.as_view()),
    path('api/main/university/departments/<slug>/achievements/', university_views.DepartmentAchievementsAPIView.as_view()),
    path('api/main/university/departments/<slug>/personals/', university_views.DepartmentPersonalsAPIView.as_view()),
    path('api/main/university/departments/<slug>/publics/', university_views.DepartmentPublicsAPIView.as_view()),
    path('api/main/university/departments/<slug>/about/', university_views.DepartmentAboutAPIView.as_view()),
]
