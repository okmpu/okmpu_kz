from django.urls import path
from .views import home, public, content


urlpatterns = [
    path('', home.home, name='home'),
    path('search/', home.search, name='search'),
    path('programs/<slug>/', home.program_detail, name='program_detail'),
    path('blog-rector/', home.blog_rector, name='blog_rector'),

    # public app urls...
    path('publics/news/', public.news_view, name='news'),
    path('publics/news/<pk>/', public.news_view, name='news_detail'),
    path('publics/announcements/', public.announcement_view, name='announcements'),
    path('publics/announcements/<pk>/', public.announcement_view, name='announcement'),

    # content urls
    path('content/<category_slug>/<sub_category_slug>/<section_slug>/<content_slug>/', content.content_detail,
         name='content_detail'),
    path('university/division/<slug>/', content.division_detail, name='division_detail'),
    path('university/division/<slug>/about', content.division_about, name='division_about'),
]
