from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Faculty, Department, Personal, Project, FacultyProgram, FacultySpecialty


# Faculty
# ----------------------------------------------------------------------------------------------------------------------
class DepartmentTab(TranslationTabularInline):
    model = Department
    extra = 0
    prepopulated_fields = {'slug': ('name_en',)}


class FacultyAdmin(TranslationAdmin):
    list_display = ('name', 'faculty_type', 'slug', )
    list_filter = ('faculty_type', )
    search_fields = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name_en', )}
    inlines = [DepartmentTab, ]


# Department
# ----------------------------------------------------------------------------------------------------------------------
class DepartmentAdmin(TranslationAdmin):
    list_display = ('name', 'faculty', 'slug', )
    list_filter = ('faculty', )
    search_fields = ('name', 'slug', 'faculty', )
    prepopulated_fields = {'slug': ('name_en', )}


# FacultyPrograms
# ----------------------------------------------------------------------------------------------------------------------
class FacultySpecialtyTab(TranslationTabularInline):
    model = FacultySpecialty
    extra = 0


class FacultyProgramAdmin(TranslationAdmin):
    list_display = ('name', 'slug', )
    list_filter = ('department', )
    search_fields = ('name', 'slug', )
    inlines = [FacultySpecialtyTab, ]
    prepopulated_fields = {'slug': ('name_en', )}


class ProjectAdmin(TranslationAdmin):
    list_display = ('name', 'author', 'department', 'date_created', )
    search_fields = ('name', 'author', 'department', )
    list_filter = ('department', )


class PersonalAdmin(TranslationAdmin):
    list_display = ('user', 'profession', 'department', 'phone', )
    search_fields = ('user', 'profession', 'department', )
    list_filter = ('department', )


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(FacultyProgram, FacultyProgramAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Personal, PersonalAdmin)
