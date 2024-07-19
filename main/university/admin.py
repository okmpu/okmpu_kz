from django.contrib import admin

from main.university.models import Faculty


class FacultyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Faculty, FacultyAdmin)
