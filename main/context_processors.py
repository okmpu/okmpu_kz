from main.content.models import Category
from main.university.models import Faculty


def categories(request):
    qs = Category.objects.filter(parent=None)
    return {
        'categories': qs,
    }


def faculties(request):
    qs = Faculty.objects.all()
    return {
        'faculties': qs,
    }