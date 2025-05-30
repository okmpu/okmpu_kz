from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from register.models import Headliner, Partner


# Headliner
# ----------------------------------------------------------------------------------------------------------------------
class HeadlinerAdmin(TranslationAdmin):
    list_display = ('title', 'poster', 'src', 'order', )
    search_fields = ('title', )


# Partner
# ----------------------------------------------------------------------------------------------------------------------
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order', )


admin.site.register(Headliner, HeadlinerAdmin)
admin.site.register(Partner, PartnerAdmin)
