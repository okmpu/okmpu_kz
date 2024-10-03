from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django_summernote.admin import SummernoteModelAdmin
from main.public.models import Headliner, News, Announcement, Vacancy, Event, Specialty, Program, Journal, Partner


class HeadlinerAdmin(TranslationAdmin):
    list_display = ('title', 'poster', 'src', 'order', )
    search_fields = ('title', )


# Programs
# ----------------------------------------------------------------------------------------------------------------------
class SpecialtyTab(TranslationTabularInline):
    model = Specialty
    extra = 0


class ProgramAdmin(TranslationAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', 'slug', )
    inlines = [SpecialtyTab, ]
    prepopulated_fields = {'slug': ('name_en', )}


class NewsAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('title', 'user', 'faculty', 'department', 'date_created', )
    list_filter = ('user', 'faculty', 'department', )


class AnnouncementAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('title', 'user', 'faculty', 'department', 'date_created', )
    list_filter = ('user', 'faculty', 'department', )


class EventAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('title', 'user', 'faculty', 'department', 'date_created', )
    list_filter = ('user', 'faculty', 'department', )


class VacancyAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('title', 'user', 'date_created', )
    list_filter = ('user', )


class JournalAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', )


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', )


admin.site.register(Headliner, HeadlinerAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Partner, PartnerAdmin)
