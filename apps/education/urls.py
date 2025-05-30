from django.urls import path
from .views import faculty, department

urlpatterns = [
    path('faculties/', faculty.faculties_view, name='faculties'),
    path('faculties/<slug>/', faculty.faculty_detail_view, name='faculty_detail'),
    path('faculties/<slug>/programs/', faculty.faculty_programs_view, name='faculty_programs'),
    path('faculties/<slug>/materials/', faculty.faculty_materials_view, name='faculty_materials'),
    path('faculties/<slug>/projects/', faculty.faculty_projects_view, name='faculty_projects'),
    path('faculties/<slug>/achievements/', faculty.faculty_achievements_view, name='faculty_achievements'),
    path('faculties/<slug>/personals/', faculty.faculty_personals_view, name='faculty_personals'),
    path('faculties/<slug>/publics/', faculty.faculty_publics_view, name='faculty_publics'),
    path('faculties/<slug>/documents/', faculty.faculty_documents_view, name='faculty_documents'),
    path('faculties/<slug>/about/', faculty.faculty_about_view, name='faculty_about'),

    path('departments/<slug>/', department.department_detail_view, name='department_detail'),
    path('departments/<slug>/programs/', department.department_programs_view, name='department_programs'),
    path('departments/<slug>/materials/', department.department_materials_view, name='department_materials'),
    path('departments/<slug>/projects/', department.department_projects_view, name='department_projects'),
    path('departments/<slug>/achievements/', department.department_achievements_view, name='department_achievements'),
    path('departments/<slug>/personals/', department.department_personals_view, name='department_personals'),
    path('departments/<slug>/publics/', department.department_publics_view, name='department_publics'),
    path('departments/<slug>/documents/', department.department_documents_view, name='department_documents'),
    path('departments/<slug>/about/', department.department_about_view, name='department_about'),

    path('personals/<personal_pk>/', department.personal_detail_view, name='personal_detail')
]
