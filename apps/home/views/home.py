from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from register.models.content import Content
from register.models.university import Program, Faculty, Department, Division
from register.models.publics import Headliner, Partner, Public


# Home page
# ----------------------------------------------------------------------------------------------------------------------
def home(request):
    headliners = Headliner.objects.filter(is_archive=False)[:5]
    programs = Program.objects.all()
    news = Public.objects.filter(public_type='news', faculty=None, department=None, division=None)[:6]
    announcements = Public.objects.filter(public_type='ann', faculty=None, department=None, division=None)[:6]
    academics = Faculty.objects.all()[:6]
    partners = Partner.objects.all()

    context = {
        'headliners': headliners,
        'programs': programs,
        'news': news,
        'announcements': announcements,
        'academics': academics,
        'partners': partners
    }
    return render(request, 'app/page.html', context)


def search(request):
    query = request.GET.get('query', '').strip()

    if not query:
        return render(request, 'components/app/home/search/search_initial.html')

    contents = Content.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    faculties = Faculty.objects.filter(name__icontains=query)
    departments = Department.objects.filter(name__icontains=query)
    divisions = Division.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'contents': contents,
        'faculties': faculties,
        'departments': departments,
        'divisions': divisions,
    }
    return render(request, 'components/app/home/search/search_results.html', context)


# Program page
# ----------------------------------------------------------------------------------------------------------------------
def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug)

    context = {
        'program': program
    }
    return render(request, 'app/programs/page.html', context)


# Blog
# ----------------------------------------------------------------------------------------------------------------------
def blog_rector(request):

    context = {}
    return render(request, 'app/blog_rector/page.html', context)
