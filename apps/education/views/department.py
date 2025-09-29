from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from register.models.publics import Public
from register.models.university import Faculty, Project, Department, Personal, Program, Success, Specialty, \
    Material, Document


# Departments page
# ----------------------------------------------------------------------------------------------------------------------
def department_detail_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    department_manage = Personal.objects.filter(faculty=department.faculty, department=department, p_type='department_manage')
    personals = Personal.objects.filter(
        faculty=department.faculty, department=department
    ).exclude(Q(p_type='deans_office') | Q(p_type='department_manage')).order_by('order')[:3]

    # documents and more...
    projects = Project.objects.filter(faculty=department.faculty, department=department)[:3]
    materials = Material.objects.filter(faculty=department.faculty, department=department)[:3]
    achievements = Success.objects.filter(faculty=department.faculty, department=department)[:3]

    # publications
    news = Public.objects.filter(public_type='news', department=department)[:3]
    events = Public.objects.filter(public_type='events', department=department)[:3]
    announcements = Public.objects.filter(public_type='ann', department=department)[:3]

    context = {
        'department': department,
        'department_manage': department_manage,
        'personals': personals,
        'projects': projects,
        'materials': materials,
        'achievements': achievements,
        'news': news,
        'events': events,
        'announcements': announcements,
    }
    return render(request, 'app/university/department/index.html', context)


# Department programs
def department_programs_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    programs = Program.objects.all()
    specialities = Specialty.objects.filter(department=department)

    context = {
        'department': department,
        'programs': programs,
        'specialities': specialities,
    }
    return render(request, 'app/university/department/programs.html', context)


# Department personals
def department_personals_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    managements = Personal.objects.filter(faculty=department.faculty, department=department, p_type='department_manage')
    teachers = Personal.objects.filter(faculty=department.faculty, department=department, p_type='teacher')
    students = Personal.objects.filter(faculty=department.faculty, department=department, p_type='student')
    context = {
        'department': department,
        'personals': [
            {
                'id': 1,
                'name_kk': 'Кафедра басшылығы',
                'name_ru': 'Руководство кафедры',
                'name_en': 'Department management',
                'type': 'management',
                'results': managements
            },
            {
                'id': 2,
                'name_kk': 'Оқытушылар',
                'name_ru': 'Преподаватели',
                'name_en': 'Teachers',
                'type': 'teachers',
                'results': teachers
            },
            {
                'id': 3,
                'name_kk': 'Белсенді студенттер',
                'name_ru': 'Активные студенты',
                'name_en': 'Active students',
                'type': 'students',
                'results': students
            },
        ]
    }
    return render(request, 'app/university/department/personals/index.html', context)


def department_documents_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    documents = Document.objects.filter(department=department)

    context = {
        'department': department,
        'documents': documents,
    }
    return render(request, 'app/university/department/documents.html', context)


def department_materials_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    materials = Material.objects.filter(department=department)

    context = {
        'department': department,
        'materials': materials,
    }
    return render(request, 'app/university/department/materials.html', context)


def department_projects_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    projects = Project.objects.filter(department=department)

    context = {
        'department': department,
        'projects': projects,
    }
    return render(request, 'app/university/department/projects.html', context)


def department_achievements_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    achievements = Success.objects.filter(department=department)

    context = {
        'department': department,
        'achievements': achievements,
    }
    return render(request, 'app/university/department/achievements.html', context)


def department_publics_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    news = Public.objects.filter(public_type='news', department=department)
    events = Public.objects.filter(public_type='events', department=department)
    announcements = Public.objects.filter(public_type='ann', department=department)

    context = {
        'department': department,
        'news': news,
        'events': events,
        'announcements': announcements,
    }
    return render(request, 'app/university/department/publics.html', context)


# Department about
def department_about_view(request, slug):
    department = get_object_or_404(Department, slug=slug)

    context = {
        'department': department,
    }
    return render(request, 'app/university/department/about.html', context)


# Personal detail
def personal_detail_view(request, personal_pk):
    personal = get_object_or_404(Personal, pk=personal_pk)
    faculty = personal.faculty
    department = personal.department
    materials = personal.author_materials.all()

    context = {
        'faculty': faculty,
        'department': department,
        'personal': personal,
        'materials': materials
    }
    return render(request, 'app/university/department/personals/detail.html', context)
