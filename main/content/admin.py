from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from django_summernote.admin import SummernoteModelAdminMixin
from .models import Category, Content, TextContent, FileContent, PopupContent, StaffContent


class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'app_name', 'parent', 'index', )
    list_filter = ('parent',)
    search_fields = ('name', 'slug', )
    prepopulated_fields = {'slug': ('name_en', )}


class TextContentInline(SummernoteModelAdminMixin, TranslationTabularInline):
    model = TextContent
    extra = 0


class FileContentInline(TranslationTabularInline):
    model = FileContent
    extra = 0


class PopupContentInline(TranslationTabularInline):
    model = PopupContent
    extra = 0


class StaffContentInline(TranslationTabularInline):
    model = StaffContent
    extra = 0


class ContentAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'category', 'index', )
    list_filter = ('category',)
    search_fields = ('title', 'slug', )
    inlines = [TextContentInline, FileContentInline, PopupContentInline, StaffContentInline, ]
    prepopulated_fields = {'slug': ('title_en', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Content, ContentAdmin)
