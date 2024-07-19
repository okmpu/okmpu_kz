from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django_summernote.admin import SummernoteModelAdminMixin

from .models import Chapter, Subsection, Section, Text, File, Content


# Section admin
# ----------------------------------------------------------------------------------------------------------------------
class SubsectionTabInline(TranslationTabularInline):
    model = Subsection
    extra = 0
    prepopulated_fields = {"slug": ("name_en",)}


class ChapterTabInline(TranslationTabularInline):
    model = Chapter
    extra = 0
    prepopulated_fields = {"slug": ("name_en",)}


class SectionAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'index', 'dropdown', )
    search_fields = ('name', 'slug')
    inlines = [SubsectionTabInline, ChapterTabInline, ]
    prepopulated_fields = {"slug": ("name_en",)}


# Subsection admin
# ----------------------------------------------------------------------------------------------------------------------
class SubsectionAdmin(TranslationAdmin):
    list_display = ('name', 'section', 'slug', 'index', )
    search_fields = ('name', 'section__name', 'slug', )
    list_filter = ('section', )
    inlines = [ChapterTabInline, ]
    prepopulated_fields = {"slug": ("name_en",)}


class ChapterAdmin(TranslationAdmin):
    list_display = ('name', 'section', 'sub_section', 'slug', 'index', )
    search_fields = ('name', 'section', 'sub_section', )
    list_filter = ('section', 'sub_section', )
    prepopulated_fields = {"slug": ("name_en",)}


# Content admin
# ----------------------------------------------------------------------------------------------------------------------
class TextContentTabInline(SummernoteModelAdminMixin, TranslationTabularInline):
    model = Text
    extra = 0


class FileContentTabInline(TranslationTabularInline):
    model = File
    extra = 0


class ContentAdmin(TranslationAdmin):
    list_display = ('title', 'sub_section', 'chapter', 'slug', 'last_update', 'index', )
    search_fields = ('title', 'chapter', )
    list_filter = ('chapter', )
    inlines = [TextContentTabInline, FileContentTabInline, ]

    prepopulated_fields = {"slug": ("title_en",)}


admin.site.register(Section, SectionAdmin)
admin.site.register(Subsection, SubsectionAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Content, ContentAdmin)
