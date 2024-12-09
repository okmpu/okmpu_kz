from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Faculty, Department, Personal, Project, FacultyProgram, FacultySpecialty, Success, MaterialDocs, \
    Material, DocumentFile, Document, Division


# Faculty
# ----------------------------------------------------------------------------------------------------------------------
class DepartmentTab(TranslationTabularInline):
    model = Department
    extra = 0
    prepopulated_fields = {'slug': ('name_en',)}


class FacultyAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('name', 'faculty_type', 'slug', )
    list_filter = ('faculty_type', )
    search_fields = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name_en', )}
    inlines = [DepartmentTab, ]


# Department
# ----------------------------------------------------------------------------------------------------------------------
class DepartmentAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('name', 'faculty', 'slug', )
    list_filter = ('faculty', )
    search_fields = ('name', 'slug', )
    prepopulated_fields = {'slug': ('name_en', )}


# Division
# ----------------------------------------------------------------------------------------------------------------------
class DivisionAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('name', 'parent', 'div_type', 'order', )
    search_fields = ('name', 'slug', )
    list_filter = ('parent', 'div_type', )
    prepopulated_fields = {'slug': ('name_en',)}


# FacultyPrograms
# ----------------------------------------------------------------------------------------------------------------------
class FacultySpecialtyTab(TranslationTabularInline):
    model = FacultySpecialty
    extra = 0


class FacultyProgramAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'department', )
    list_filter = ('department', )
    search_fields = ('name', 'slug', )
    inlines = [FacultySpecialtyTab, ]
    prepopulated_fields = {'slug': ('name_en', )}


# Projects
# ----------------------------------------------------------------------------------------------------------------------
class ProjectAdmin(TranslationAdmin):
    list_display = ('name', 'author', 'faculty', 'department', 'date_created', )
    search_fields = ('name', )
    list_filter = ('faculty', 'department', )


# Achievements
# ----------------------------------------------------------------------------------------------------------------------
class SuccessAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('title', 'faculty', 'department', 'date_created', )
    search_fields = ('title', )
    list_filter = ('faculty', 'department', 'division', )


# Personals
# ----------------------------------------------------------------------------------------------------------------------
class PersonalAdmin(TranslationAdmin, SummernoteModelAdmin):
    list_display = ('full_name', 'profession', 'p_type', 'faculty', 'department', )
    search_fields = ('full_name', 'profession', )
    list_filter = ('faculty', 'department', 'p_type', 'division', )


# Materials
# ----------------------------------------------------------------------------------------------------------------------
class MaterialDocsTab(TranslationTabularInline):
    model = MaterialDocs
    extra = 0

class MaterialAdmin(TranslationAdmin):
    list_display = ('title', 'author', 'date_created', )
    search_fields = ('title', 'author', )
    list_filter = ('faculty', 'department', )

    inlines = [MaterialDocsTab, ]


# Documents
# ----------------------------------------------------------------------------------------------------------------------
class DocumentFileTab(TranslationTabularInline):
    model = DocumentFile
    extra = 0

class DocumentAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'faculty', 'department', 'docs_grid', )
    search_fields = ('name', 'docs_grid', )
    list_filter = ('faculty', 'department', 'division', )
    prepopulated_fields = {'slug': ('name_en',)}

    inlines = [DocumentFileTab, ]


admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(FacultyProgram, FacultyProgramAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Success, SuccessAdmin)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Division, DivisionAdmin)
