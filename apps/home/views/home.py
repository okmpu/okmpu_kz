from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from main.utils import track_page_view
from register.models.content import Content
from register.models.university import Program, Faculty
from register.models.publics import Headliner, Partner, Public


# Home page
# ----------------------------------------------------------------------------------------------------------------------
def home(request):
    track_page_view(request, request.path)
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
    return render(request, 'src/index.html', context)


def search(request):
    query = request.GET.get('query', '')
    results = None

    if query:
        results = Content.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'src/search.html', context)


# Program page
# ----------------------------------------------------------------------------------------------------------------------
def program_detail(request, slug):
    program = get_object_or_404(Program, slug=slug)

    context = {
        'program': program
    }
    return render(request, 'src/programs.html', context)


# Blog
# ----------------------------------------------------------------------------------------------------------------------
def blog_rector(request):

    context = {}
    return render(request, 'src/blog_rector.html', context)
