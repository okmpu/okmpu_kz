from django.contrib.admin import register
from modeltranslation.admin import TranslationAdmin
from modeltranslation.admin import TranslationTabularInline, TranslationStackedInline
from register.forms.content import TextContentForm, StaffContentForm, PopupContentForm
from register.models.content import Category, Content, TextContent, FileContent, ImageContent, StaffContent, \
    PopupContent


# Category
# ----------------------------------------------------------------------------------------------------------------------
@register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'app_name', 'parent', 'multiple', 'order', )
    list_filter = ('parent', 'app_name', 'multiple',)
    search_fields = ('name', 'slug', )
    prepopulated_fields = {'slug': ('name_en', )}


# Content
# ----------------------------------------------------------------------------------------------------------------------
# TextContent
class TextContentTabular(TranslationStackedInline):
    model = TextContent
    form = TextContentForm
    extra = 0


# ImageContent
class ImageContentTabular(TranslationTabularInline):
    model = ImageContent
    extra = 0


# FileContent
class FileContentTabular(TranslationStackedInline):
    model = FileContent
    extra = 0


# StaffContent
class StaffContentTabular(TranslationStackedInline):
    model = StaffContent
    form = StaffContentForm
    extra = 0


# PopupContent
class PopupContentInline(TranslationStackedInline):
    model = PopupContent
    form = PopupContentForm
    extra = 0


# ContentAdmin
@register(Content)
class ContentAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'category', 'order', )
    list_filter = ('category',)
    search_fields = ('title', 'slug', )
    prepopulated_fields = {'slug': ('title_en', )}
    inlines = [
        TextContentTabular,
        ImageContentTabular,
        FileContentTabular,
        StaffContentTabular,
        PopupContentInline,
    ]
