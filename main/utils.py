# from main.public.models import PageView
#
#
# def track_page_view(request, pathname):
#     is_authenticated = request.user.is_authenticated
#     page_view, created = PageView.objects.get_or_create(pathname=pathname)
#
#     if is_authenticated:
#         page_view.auth_users_count += 1
#     else:
#         page_view.users_count += 1
#
#     page_view.save(update_fields=['auth_users_count', 'users_count'])
