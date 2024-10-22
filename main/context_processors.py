from main.content.models import Category

def categories(request):
    qs = Category.objects.filter(parent=None)
    return {
        'categories': qs,
    }