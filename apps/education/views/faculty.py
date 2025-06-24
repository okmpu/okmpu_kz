from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from register.models.publics import Public
from register.models.university import Faculty, Project, Department, Personal, Program, Success, Specialty, \
    Material, Document


# Faculties page
# ----------------------------------------------------------------------------------------------------------------------
def faculties_view(request):
    faculties = Faculty.objects.all()
    context = {
        'faculties': faculties
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
        news = Public.objects.filter(public_type='news').filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
        events = Public.objects.filter(public_type='events').filter(Q(faculty=faculty) | Q(department__in=departments))[:3]
        announcements = Public.objects.filter(public_type='ann').filter(Q(faculty=faculty) | Q(department__in=departments))[:3]

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
        news = Public.objects.filter(faculty=faculty, public_type='news')[:3]
        events = Public.objects.filter(faculty=faculty, public_type='events')[:3]
        announcements = Public.objects.filter(faculty=faculty, public_type='ann')[:3]

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
    elif faculty.faculty_type == 'institute' or faculty.faculty_type == 'college':
        personals = Personal.objects.filter(faculty=faculty).exclude(p_type='deans_office').order_by('order')
        context['personals'] = personals

    return render(request, 'src/university/faculty/personals.html', context)


# Faculty programs
def faculty_programs_view(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    context = {
        'faculty': faculty,
    }
    if faculty.faculty_type == 'faculty':
        programs = Program.objects.all()
        specialities = Specialty.objects.filter(faculty=faculty)
        context['programs'] = programs
        context['specialities'] = specialities
    elif faculty.faculty_type == 'institute':
        context['programs'] = Program.objects.exclude(slug='bachelor')

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
        news = Public.objects.filter(public_type='news').filter(Q(faculty=faculty) | Q(department__in=departments))
        events = Public.objects.filter(public_type='events').filter(Q(faculty=faculty) | Q(department__in=departments))
        announcements = Public.objects.filter(public_type='ann').filter(Q(faculty=faculty) | Q(department__in=departments))
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