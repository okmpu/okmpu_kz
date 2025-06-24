from django.urls import path
from main.university import views as university_views


urlpatterns = [
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
    path('university/departments/<slug>/documents/', university_views.department_documents_view, name='department_documents'),
    path('university/departments/<slug>/about/', university_views.department_about_view, name='department_about'),

    path('university/personals/<personal_pk>/', university_views.personal_detail_view, name='personal_detail')
]
