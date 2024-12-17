from django.urls import path
from setuptools.extern import names

from main.content import views as content_view
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
    path('content/<category_slug>/<sub_category_slug>/<section_slug>/<content_slug>/', content_view.content_detail, name='content_detail'),
    path('university/division/<slug>/', content_view.division_detail, name='division_detail'),
    path('university/division/<slug>/about', content_view.division_about, name='division_about'),

    # university apps urls...
    path('university/faculties/', university_views.faculties_view, name='faculties'),
    path('university/faculties/<slug>/', university_views.faculty_detail_view, name='faculty_detail'),
    path('university/faculties/<slug>/programs/', university_views.faculty_programs_view, name='faculty_programs'),
    path('university/faculties/<slug>/materials/', university_views.faculty_materials_view, name='faculty_materials'),
    path('university/faculties/<slug>/projects/', university_views.faculty_projects_view, name='faculty_projects'),
    path('university/faculties/<slug>/achievements/', university_views.faculty_achievements_view, name='faculty_achievements'),
    path('university/faculties/<slug>/personals/', university_views.faculty_personals_view, name='faculty_personals'),
    path('university/faculties/<slug>/publics/', university_views.faculty_publics_view, name='faculty_publics'),
    path('university/faculties/<slug>/documents/', university_views.faculty_documents_view, name='faculty_documents'),
    path('university/faculties/<slug>/about/', university_views.faculty_about_view, name='faculty_about'),

    path('university/departments/<slug>/', university_views.department_detail_view, name='department_detail'),
    path('university/departments/<slug>/programs/', university_views.department_programs_view, name='department_programs'),
    path('university/departments/<slug>/materials/', university_views.department_materials_view, name='department_materials'),
    path('university/departments/<slug>/projects/', university_views.department_projects_view, name='department_projects'),
    path('university/departments/<slug>/achievements/', university_views.department_achievements_view, name='department_achievements'),
    path('university/departments/<slug>/personals/', university_views.department_personals_view, name='department_personals'),
    path('university/departments/<slug>/publics/', university_views.department_publics_view, name='department_publics'),
    path('university/departments/<slug>/about/', university_views.department_about_view, name='department_about'),

    path('university/personals/<personal_pk>/', university_views.personal_detail_view, name='personal_detail')
]
