from register.models.content import Category
from register.models.publics import Resource
from register.models.university import Faculty, Division


def global_context(request):
    categories = Category.objects.filter(parent__isnull=True).order_by('order').prefetch_related('children')
    resources = Resource.objects.all().order_by('order')
    faculties = Faculty.objects.all()
    divisions = Division.objects.filter(parent__isnull=True)
    return {
        'categories': categories,
        'resources': resources,
        'faculties': faculties,
        'divisions': divisions,
    }
