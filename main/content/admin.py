# from django.contrib import admin
# from django.contrib.auth.models import Group
# from modeltranslation.admin import TranslationAdmin
# from modeltranslation.admin import TranslationTabularInline, TranslationStackedInline
# from django_summernote.admin import SummernoteModelAdminMixin
# from .models import Category, Content, TextContent, FileContent, ImageContent, StaffContent
#
#
# # Category
# # ----------------------------------------------------------------------------------------------------------------------
# class CategoryAdmin(TranslationAdmin):
#     list_display = ('name', 'slug', 'app_name', 'parent', 'multiple', 'order', )
#     list_filter = ('parent', 'app_name', 'multiple',)
#     search_fields = ('name', 'slug', )
#     prepopulated_fields = {'slug': ('name_en', )}
#
#
# # Content
# # ----------------------------------------------------------------------------------------------------------------------
# # TextContent
# class TextContentTabular(SummernoteModelAdminMixin, TranslationTabularInline):
#     model = TextContent
#     extra = 0
#
#
# # ImageContent
# class ImageContentTabular(TranslationTabularInline):
#     model = ImageContent
#     extra = 0
#
#
# # FileContent
# class FileContentTabular(TranslationStackedInline):
#     model = FileContent
#     extra = 0
#
#
# # StaffContent
# class StaffContentTabular(SummernoteModelAdminMixin, TranslationStackedInline):
#     model = StaffContent
#     extra = 0
#
#
# class ContentAdmin(TranslationAdmin):
#     list_display = ('title', 'slug', 'category', 'order', )
#     list_filter = ('category',)
#     search_fields = ('title', 'slug', )
#     prepopulated_fields = {'slug': ('title_en', )}
#     inlines = [TextContentTabular, ImageContentTabular, FileContentTabular, StaffContentTabular, ]
#
#
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Content, ContentAdmin)
# admin.site.unregister(Group)
