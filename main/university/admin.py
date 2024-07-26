from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Faculty, Department, Program, Specialty


# Faculty
# ----------------------------------------------------------------------------------------------------------------------
class DepartmentTab(TranslationTabularInline):
    model = Department
    extra = 0


class FacultyAdmin(TranslationAdmin):
    list_display = ('name', 'faculty_type', 'slug', )
    list_filter = ('faculty_type', )
    prepopulated_fields = {'slug': ('name_en', )}
    inlines = [DepartmentTab, ]


# Department
# ----------------------------------------------------------------------------------------------------------------------
class DepartmentAdmin(TranslationAdmin):
    list_display = ('name', 'faculty', 'slug', )
    list_filter = ('faculty', )
    prepopulated_fields = {'slug': ('name_en', )}


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Program)
