from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django_summernote.admin import SummernoteModelAdmin, SummernoteModelAdminMixin
from ..models import Category, Topic, Chapter, Content, TextContent, FileContent


class TopicTabInline(TranslationTabularInline):
    model = Topic
    extra = 1


class ChapterTabInline(TranslationTabularInline):
    model = Chapter
    extra = 1


class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'src', 'index', 'dropdown', )
    search_fields = ('name', )
    inlines = [TopicTabInline, ]


class TopicAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('name', 'category', 'src', 'index', )
    search_fields = ('name', 'category', )
    list_filter = ('category', )
    inlines = [ChapterTabInline, ]


class TextContentTabInline(SummernoteModelAdminMixin, TranslationTabularInline):
    model = TextContent
    extra = 1


class FileContentTabInline(TranslationTabularInline):
    model = FileContent
    extra = 1


class ContentAdmin(TranslationAdmin):
    list_display = ('title', 'chapter', 'last_update', 'index', )
    search_fields = ('title', 'chapter', )
    list_filter = ('chapter', )

    inlines = [TextContentTabInline, FileContentTabInline, ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Content, ContentAdmin)
