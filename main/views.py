from django.shortcuts import get_object_or_404, render

from main.context_processors import divisions
from main.public.models import Headliner, News, Announcement, Event, Journal, Partner
from main.university.models import Faculty, FacultyProgram
from main.utils import track_page_view


# Home page
# ----------------------------------------------------------------------------------------------------------------------
def home(request):
    track_page_view(request, request.path)
    headliners = Headliner.objects.filter()[:5]
    programs = FacultyProgram.objects.all()
    news = News.objects.filter(faculty=None, department=None, division=None)[:6]
    announcements = Announcement.objects.filter(faculty=None, department=None, division=None)[:6]
    events = Event.objects.filter(faculty=None, department=None, division=None)[:4]
    journals = Journal.objects.filter()[:6]
    academics = Faculty.objects.all()[:6]
    partners = Partner.objects.all()

    context = {
        'headliners': headliners,
        'programs': programs,
        'news': news,
        'announcements': announcements,
        'events': events,
        'journals': journals,
        'academics': academics,
        'partners': partners
    }
    return render(request, 'src/index.html', context)


# Program page
# ----------------------------------------------------------------------------------------------------------------------
def program_detail(request, slug):
    program = get_object_or_404(FacultyProgram, slug=slug)

    context = {
        'program': program
    }
    return render(request, 'src/programs.html', context)


# Blog
# ----------------------------------------------------------------------------------------------------------------------
def blog_rector(request):

    context = {}
    return render(request, 'src/blog_rector.html', context)
