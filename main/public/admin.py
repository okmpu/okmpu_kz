from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django_summernote.admin import SummernoteModelAdmin
from main.public.models import Headliner, News, Announcement, Vacancy


class HeadlinerAdmin(TranslationAdmin):
    list_display = ('title', 'poster', 'src', )


class NewsAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('title', 'user', 'date_created', )
    list_filter = ('user', )


class AnnouncementAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('title', 'user', 'date_created', )
    list_filter = ('user', )


class VacancyAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('title', 'user', 'date_created', )
    list_filter = ('user', )


admin.site.register(Headliner, HeadlinerAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Vacancy, VacancyAdmin)
