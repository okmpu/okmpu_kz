from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin
from register.models.publics import Headliner, Partner, Public, PublicFile


# Headliner
# ----------------------------------------------------------------------------------------------------------------------
class HeadlinerAdmin(TranslationAdmin):
    list_display = ('title', 'poster', 'src', 'order', )
    search_fields = ('title', )


# Partner
# ----------------------------------------------------------------------------------------------------------------------
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', )


# Public
# ----------------------------------------------------------------------------------------------------------------------
class PublicFileTab(admin.TabularInline):
    model = PublicFile
    extra = 0


class PublicAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('title', 'public_type', 'user', 'date_created', )
    search_fields = ('title', )
    list_filter = ('public_type', )

    inlines = (PublicFileTab, )


admin.site.register(Headliner, HeadlinerAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Public, PublicAdmin)
