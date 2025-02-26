from main.public.models import PageView


def track_page_view(request, pathname):
    """ Қолданушының белгілі бір бетке кіргенін тіркеу """
    is_authenticated = request.user.is_authenticated  # Аутентификация тексеру

    # Базадан жазбаны алу немесе жаңасын жасау
    page_view, created = PageView.objects.get_or_create(pathname=pathname)

    # Статистиканы жаңарту
    if is_authenticated:
        page_view.auth_users_count += 1
    else:
        page_view.users_count += 1

    # Өзгерістерді сақтау
    page_view.save(update_fields=['auth_users_count', 'users_count'])
