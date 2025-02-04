from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from main.public.models import News, Event, Announcement, Program
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
    personals = Personal.objects.filter(faculty=faculty).exclude(p_type='deans_office').order_by('order')[:3]

    context = {
        'faculty': faculty,
        'personals': personals
    }
    if faculty.faculty_type == 'faculty':
        departments = Department.objects.filter(faculty=faculty)
        deans_office = Personal.objects.filter(faculty=faculty, p_type='deans_office')

        # documents and more...
        projects = Project.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
        materials = Material.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
        achievements = Success.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]

        # publications
        news = News.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
        events = Event.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
        announcements = Announcement.objects.filter(Q(faculty=faculty) | Q(department__in=departments))[:3]

        context['departments'] = departments
        context['deans_office'] = deans_office
        context['projects'] = projects
        context['materials'] = materials
        context['achievements'] = achievements
        context['news'] = news
        context['events'] = events
        context['announcements'] = announcements

    elif faculty.faculty_type == 'institute':
        # documents and more...
        projects = Project.objects.filter(faculty=faculty)[:3]
        documents = Document.objects.filter(faculty=faculty)[:3]
        achievements = Success.objects.filter(faculty=faculty)[:3]

        # publications
        news = News.objects.filter(faculty=faculty)[:3]
        events = Event.objects.filter(faculty=faculty)[:3]
        announcements = Announcement.objects.filter(faculty=faculty)[:3]

        context['projects'] = projects
        context['documents'] = documents
        context['achievements'] = achievements
        context['news'] = news
        context['events'] = events
        context['announcements'] = announcements

    return render(request, 'src/university/faculty/index.html', context)


# Faculty personals
def faculty_personals_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)

    context = {
        'faculty': faculty,
    }
    if faculty.faculty_type == 'faculty':
        deans_office = Personal.objects.filter(faculty=faculty, p_type='deans_office')
        teachers = Personal.objects.filter(faculty=faculty).filter(Q(p_type='department_manage') | Q(p_type='teacher'))
        students = Personal.objects.filter(faculty=faculty, p_type='student')
        context['personals'] = [
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
    elif faculty.faculty_type == 'institute':
        personals = Personal.objects.filter(faculty=faculty).exclude(p_type='deans_office').order_by('order')
        context['personals'] = personals

    return render(request, 'src/university/faculty/personals.html', context)


# Faculty programs
def faculty_programs_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    programs = FacultyProgram.objects.all()
    departments = []
    for department in faculty.departments.all():
        item = {
            'department': department,
        }
        for program in programs:
            item['programs'] = []
            ls.append({
                'name': item.name,
                'slug': item.slug,
                'program_items': FacultySpecialty.objects.filter(program=item)
            })
    context = {
        'faculty': faculty,
        'programs': ls
    }

    print(ls)
    return render(request, 'src/university/faculty/programs.html', context)


# Faculty edu materials
def faculty_materials_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    departments = Department.objects.filter(faculty=faculty)
    materials = Material.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
    context = {
        'faculty': faculty,
        'materials': materials
    }
    return render(request, 'src/university/faculty/materials.html', context)


# Faculty projects
def faculty_projects_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    departments = Department.objects.filter(faculty=faculty)
    projects = Project.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
    context = {
        'faculty': faculty,
        'projects': projects
    }
    return render(request, 'src/university/faculty/projects.html', context)


# Faculty documents
def faculty_documents_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    documents = Document.objects.filter(faculty=faculty)

    context = {
        'faculty': faculty,
        'documents': documents,
    }
    return render(request, 'src/university/faculty/documents.html', context)


# Faculty achievements
def faculty_achievements_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    departments = Department.objects.filter(faculty=faculty)
    achievements = Success.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
    context = {
        'faculty': faculty,
        'achievements': achievements
    }
    return render(request, 'src/university/faculty/achievements.html', context)


# Faculty publics
def faculty_publics_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    context = {
        'faculty': faculty,
    }
    if faculty.faculty_type == 'faculty':
        departments = Department.objects.filter(faculty=faculty)
        news = News.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
        events = Event.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
        announcements = Announcement.objects.filter(Q(faculty=faculty) | Q(department__in=departments))
        context['departments'] = departments
        context['news'] = news
        context['events'] = events
        context['announcements'] = announcements

    elif faculty.faculty_type == 'institute':
        pass
    context = {
        'faculty': faculty,
        'news': news,
        'events': events,
        'announcements': announcements,
    }
    return render(request, 'src/university/faculty/publics.html', context)


# Faculty about
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
    department_manage = Personal.objects.filter(faculty=department.faculty, department=department, p_type='department_manage')
    personals = Personal.objects.filter(
        faculty=department.faculty, department=department
    ).exclude(Q(p_type='deans_office') | Q(p_type='department_manage')).order_by('order')[:3]

    # documents and more...
    projects = Project.objects.filter(faculty=department.faculty, department=department)[:3]
    materials = Material.objects.filter(faculty=department.faculty, department=department)[:3]
    achievements = Success.objects.filter(faculty=department.faculty, department=department)[:3]

    # publications
    news = News.objects.filter(department=department)[:3]
    events = Event.objects.filter(department=department)[:3]
    announcements = Announcement.objects.filter(department=department)[:3]

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
    return render(request, 'src/university/department/index.html', context)


# Department programs
def department_programs_view(request, slug):
    department = get_object_or_404(Department, slug=slug)

    programs = FacultySpecialty.objects.filter(department=department)

    context = {
        'department': department,
        'programs': programs,
    }
    return render(request, 'src/university/department/programs.html', context)


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
    return render(request, 'src/university/department/personals/index.html', context)


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


# Department about
def department_about_view(request, slug):
    department = get_object_or_404(Department, slug=slug)

    context = {
        'department': department,
    }
    return render(request, 'src/university/department/about.html', context)


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
    return render(request, 'src/university/department/personals/detail.html', context)