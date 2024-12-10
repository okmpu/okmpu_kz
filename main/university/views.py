from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from main.public.models import News, Event, Announcement
from main.university.models import Faculty, Project, Department, Personal, FacultyProgram, Success, FacultySpecialty, \
    Material, Document


# Faculties page
# ----------------------------------------------------------------------------------------------------------------------
def faculties_view(request):
    items = Faculty.objects.all()
    context = {
        'faculties': items
    }
    return render(request, 'src/university/faculties.html', context)


# Faculty detail
def faculty_detail_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    departments = Department.objects.filter(faculty=faculty)

    # personals
    deans_office = Personal.objects.filter(faculty=faculty, p_type='deans_office')
    personals = Personal.objects.filter(
        faculty=faculty
    ).exclude(p_type='deans_office').order_by('order')[:3]

    # documents and more...
    projects = Project.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
    materials = Material.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
    achievements = Success.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]

    # publications
    news = News.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
    events = Event.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
    announcements = Announcement.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]

    context = {
        'faculty': faculty,
        'departments': departments,
        'deans_office': deans_office,
        'personals': personals,
        'projects': projects,
        'materials': materials,
        'achievements': achievements,
        'news': news,
        'events': events,
        'announcements': announcements,
    }
    return render(request, 'src/university/faculty/index.html', context)


# Faculty about
def department_about_view(request, slug):
    department = get_object_or_404(Department, slug=slug)

    context = {
        'department': department,
    }
    return render(request, 'src/university/department/about.html', context)


# Faculty personals
def faculty_personals_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    deans_office = Personal.objects.filter(faculty=faculty, p_type='deans_office')
    teachers = Personal.objects.filter(faculty=faculty).filter(Q(p_type='department_manage') | Q(p_type='teacher'))
    students = Personal.objects.filter(faculty=faculty, p_type='student')
    context = {
        'faculty': faculty,
        'personals': [
            {
                'id': 1,
                'name_kk': 'Деканат',
                'name_ru': 'Деканат',
                'name_en': 'Deans office',
                'type': 'deans_office',
                'results': deans_office
            },
            {
                'id': 2,
                'name_kk': 'Оқытушы/Профессорлар',
                'name_ru': 'Преподаватель/Профессора',
                'name_en': 'Teacher/Professors',
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
    return render(request, 'src/university/faculty/personals.html', context)


def faculty_programs_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    context = {
        'faculty': faculty,
    }
    return render(request, 'src/university/faculty/programs.html', context)


def faculty_materials_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    departments = Department.objects.filter(faculty=faculty)
    materials = Material.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
    context = {
        'faculty': faculty,
        'materials': materials
    }
    return render(request, 'src/university/faculty/materials.html', context)


def faculty_projects_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    departments = Department.objects.filter(faculty=faculty)
    projects = Project.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
    context = {
        'faculty': faculty,
        'projects': projects
    }
    return render(request, 'src/university/faculty/projects.html', context)


def faculty_achievements_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    departments = Department.objects.filter(faculty=faculty)
    achievements = Success.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
    context = {
        'faculty': faculty,
        'achievements': achievements
    }
    return render(request, 'src/university/faculty/achievements.html', context)


def faculty_publics_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    departments = Department.objects.filter(faculty=faculty)
    news = News.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
    events = Event.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
    announcements = Announcement.objects.filter(Q(faculty=faculty) | Q(department__in=departments))

    context = {
        'faculty': faculty,
        'news': news,
        'events': events,
        'announcements': announcements,
    }
    return render(request, 'src/university/faculty/publics.html', context)


def faculty_documents_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    documents = Document.objects.filter(faculty=faculty)

    context = {
        'faculty': faculty,
        'documents': documents,
    }
    return render(request, 'src/university/faculty/documents.html', context)


def faculty_about_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)

    context = {
        'faculty': faculty,
    }
    return render(request, 'src/university/faculty/about.html', context)


# Departments page
# ----------------------------------------------------------------------------------------------------------------------
def department_detail_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    projects = Project.objects.filter(department=department)[:3]
    personals = Personal.objects.filter(department=department)[:3]
    news = News.objects.filter(department=department)[:3]
    events = Event.objects.filter(department=department)[:3]
    announcements = Announcement.objects.filter(department=department)[:3]

    context = {
        'department': department,
        'projects': projects,
        'personals': personals,
        'news': news,
        'events': events,
        'announcements': announcements,
    }
    return render(request, 'src/university/department/index.html', context)


def department_programs_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    programs = FacultyProgram.objects.filter(department=department)

    context = {
        'department': department,
        'programs': programs,
    }
    return render(request, 'src/university/department/programs.html', context)


def department_materials_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    materials = Material.objects.filter(department=department)

    context = {
        'department': department,
        'materials': materials,
    }
    return render(request, 'src/university/department/materials.html', context)


def department_projects_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    projects = Project.objects.filter(department=department)

    context = {
        'department': department,
        'projects': projects,
    }
    return render(request, 'src/university/department/projects.html', context)


def department_achievements_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    achievements = Success.objects.filter(department=department)

    context = {
        'department': department,
        'achievements': achievements,
    }
    return render(request, 'src/university/department/achievements.html', context)


def department_personals_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    managements = Personal.objects.filter(department=department, p_type='MANAGEMENT')
    teachers = Personal.objects.filter(department=department, p_type='TEACHER')
    students = Personal.objects.filter(department=department, p_type='STUDENT')
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
                'name_kk': 'Студенттер',
                'name_ru': 'Студенты',
                'name_en': 'Students',
                'type': 'students',
                'results': students
            },
        ]
    }
    return render(request, 'src/university/department/personals.html', context)


def department_publics_view(request, slug):
    department = get_object_or_404(Department, slug=slug)
    news = News.objects.filter(department=department)
    events = Event.objects.filter(department=department)
    announcements = Announcement.objects.filter(department=department)

    context = {
        'department': department,
        'news': news,
        'events': events,
        'announcements': announcements,
    }
    return render(request, 'src/university/department/publics.html', context)

