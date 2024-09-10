from django.urls import path
from main.content.views import ContentDetail
from main.views import CategoryListAPIView, HomeAPIView, ProgramAPIView
from main.public import views as main_views
from main.university import views as university_views

urlpatterns = [
    # main app urls...
    path('', HomeAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('program/<slug>/', ProgramAPIView.as_view()),

    # content app urls...
    path('content/<category_slug>/<sub_category_slug>/<section_slug>/<content_slug>/', ContentDetail.as_view()),

    # university apps urls...
    path('university/faculties/', university_views.FacultiesAPIView.as_view()),
    path('university/faculties/<slug>/', university_views.FacultyDetailAPIView.as_view()),
    path('university/faculties/<slug>/programs/', university_views.ProgramsFacultyAPIView.as_view()),
    path('university/faculties/<slug>/projects/', university_views.ProjectsFacultyAPIView.as_view()),
    path('university/faculties/<slug>/personals/', university_views.PersonalsFacultyAPIView.as_view()),
    path('university/faculties/<slug>/publics/', university_views.PublicsFacultyAPIView.as_view()),
    path('university/faculties/<slug>/about/', university_views.AboutFacultyAPIView.as_view()),

    path('university/departments/<slug>/', university_views.DepartmentDetailAPIView.as_view()),
    path('university/departments/<slug>/programs/', university_views.DepartmentProgramsAPIView.as_view()),
    path('university/departments/<slug>/projects/', university_views.DepartmentProjectsAPIView.as_view()),
    path('university/departments/<slug>/personals/', university_views.DepartmentPersonalsAPIView.as_view()),
    path('university/departments/<slug>/publics/', university_views.DepartmentPublicsAPIView.as_view()),
    path('university/departments/<slug>/about/', university_views.DepartmentAboutAPIView.as_view()),

    # public app urls...
    path('public/news/', main_views.NewsAPIView.as_view()),
    path('public/news/<pk>/', main_views.NewsDetailAPIView.as_view()),
    path('public/announcements/', main_views.AnnouncementsAPIView.as_view()),
    path('public/announcements/<pk>/', main_views.AnnouncementDetailAPIView.as_view()),
    path('public/events/', main_views.EventsAPIView.as_view()),
    path('public/events/<pk>/', main_views.EventDetailAPIView.as_view()),
]
