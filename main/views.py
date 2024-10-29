from django.shortcuts import get_object_or_404, render
from main.public.models import Headliner, News, Announcement, Event, Program, Journal, Partner
from main.university.models import Faculty


# Home page
# ----------------------------------------------------------------------------------------------------------------------
def home(request):
    headliners = Headliner.objects.filter()[:5]
    programs = Program.objects.all()
    news = News.objects.filter()[:6]
    announcements = Announcement.objects.filter()[:6]
    events = Event.objects.filter()[:4]
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
    program = get_object_or_404(Program, slug=slug)

    context = {
        'program': program
    }
    return render(request, 'src/programs.html', context)
