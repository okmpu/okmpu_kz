from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from register.models import Headliner


class HeadlinerAdmin(TranslationAdmin):
    list_display = ('title', 'poster', 'src', 'order', )
    search_fields = ('title', )


admin.site.register(Headliner, HeadlinerAdmin)
