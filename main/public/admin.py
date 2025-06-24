# from django.contrib import admin
# from modeltranslation.admin import TranslationAdmin
# from django_summernote.admin import SummernoteModelAdmin
# from main.public.models import Headliner, News, Announcement, Event, Journal, Partner, \
#     NewsFile, AnnouncementFile, EventFile, PageView
#
#
# class HeadlinerAdmin(TranslationAdmin):
#     list_display = ('title', 'poster', 'src', 'order', )
#     search_fields = ('title', )
#
#
# # News
# class NewsFileTab(admin.TabularInline):
#     model = NewsFile
#     extra = 0
#
#
# class NewsAdmin(TranslationAdmin, SummernoteModelAdmin):
#     list_display = ('title', 'user', 'faculty', 'department', 'date_created', )
#     list_filter = ('user', 'faculty', 'department', )
#     search_fields = ('title', )
#     inlines = [NewsFileTab, ]
#
#
# # Announcement
# class AnnouncementFileTab(admin.TabularInline):
#     model = AnnouncementFile
#     extra = 0
#
# class AnnouncementAdmin(TranslationAdmin, SummernoteModelAdmin):
#     list_display = ('title', 'user', 'faculty', 'department', 'date_created', )
#     list_filter = ('user', 'faculty', 'department', )
#     search_fields = ('title', )
#     inlines = [AnnouncementFileTab, ]
#
#
# # Event
# class EventFileTab(admin.TabularInline):
#     model = EventFile
#     extra = 0
#
# class EventAdmin(TranslationAdmin, SummernoteModelAdmin):
#     list_display = ('title', 'user', 'faculty', 'department', 'date_created', )
#     list_filter = ('user', 'faculty', 'department', )
#     search_fields = ('title', )
#     inlines = [EventFileTab, ]
#
#
# class VacancyAdmin(TranslationAdmin, SummernoteModelAdmin):
#     list_display = ('title', 'user', 'date_created', )
#     list_filter = ('user', )
#
#
# class JournalAdmin(admin.ModelAdmin):
#     list_display = ('title', 'date_created', )
#
#
# class PartnerAdmin(admin.ModelAdmin):
#     list_display = ('name', 'url', 'order', )
#
#
# class PageViewAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Headliner, HeadlinerAdmin)
# admin.site.register(News, NewsAdmin)
# admin.site.register(Announcement, AnnouncementAdmin)
# admin.site.register(Event, EventAdmin)
# admin.site.register(Journal, JournalAdmin)
# admin.site.register(Partner, PartnerAdmin)
# admin.site.register(PageView, PageViewAdmin)
