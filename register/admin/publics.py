from django.contrib import admin
from django.contrib.admin import register
from modeltranslation.admin import TranslationAdmin
from register.forms.publics import PublicForm
from register.models.publics import Headliner, Partner, Public, PublicFile, Resource


# Resource
# ----------------------------------------------------------------------------------------------------------------------
@register(Resource)
class ResourceAdmin(TranslationAdmin):
    list_display = ('label', 'url', 'new_tab', 'order', )
    list_filter = ('new_tab', )


# Headliner
# ----------------------------------------------------------------------------------------------------------------------
@register(Headliner)
class HeadlinerAdmin(TranslationAdmin):
    list_display = ('title', 'poster', 'src', 'order', )
    search_fields = ('title', )


# Partner
# ----------------------------------------------------------------------------------------------------------------------
@register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', )


# Public admin
# ----------------------------------------------------------------------------------------------------------------------
class PublicFileTab(admin.TabularInline):
    model = PublicFile
    extra = 0


@register(Public)
class PublicAdmin(TranslationAdmin):
    list_display = ('title', 'public_type', 'user', 'date_created', )
    search_fields = ('title', )
    list_filter = ('public_type', )
    form = PublicForm
    inlines = (PublicFileTab, )
