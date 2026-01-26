from django.contrib.admin import register
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from register.forms.university import FacultyForm, DepartmentForm, DivisionForm, ProjectForm, SuccessForm, PersonalForm
from register.models.university import Faculty, Department, Personal, Project, Program, Specialty, Success, MaterialDocs, \
    Material, DocumentFile, Document, Division


# Faculty
# ----------------------------------------------------------------------------------------------------------------------
@register(Faculty)
class FacultyAdmin(TranslationAdmin):
    list_display = ('name', 'faculty_type', 'slug', 'order', )
    list_filter = ('faculty_type', )
    search_fields = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name_en', )}
    form = FacultyForm


# Department
# ----------------------------------------------------------------------------------------------------------------------
@register(Department)
class DepartmentAdmin(TranslationAdmin):
    list_display = ('name', 'faculty', 'slug', )
    list_filter = ('faculty', )
    search_fields = ('name', 'slug', )
    prepopulated_fields = {'slug': ('name_en', )}
    form = DepartmentForm


# Division
# ----------------------------------------------------------------------------------------------------------------------
@register(Division)
class DivisionAdmin(TranslationAdmin):
    list_display = ('name', 'parent', 'div_type', 'order', )
    search_fields = ('name', 'slug', )
    list_filter = ('parent', 'div_type', )
    prepopulated_fields = {'slug': ('name_en',)}
    form = DivisionForm


# FacultyPrograms
# ----------------------------------------------------------------------------------------------------------------------
class FacultySpecialtyTab(TranslationTabularInline):
    model = Specialty
    extra = 0


@register(Program)
class FacultyProgramAdmin(TranslationAdmin):
    list_display = ('name', 'slug', )
    search_fields = ('name', 'slug', )
    inlines = [FacultySpecialtyTab, ]
    prepopulated_fields = {'slug': ('name_en', )}


@register(Specialty)
class FacultySpecialtyAdmin(TranslationAdmin):
    list_display = ('code', 'name', 'program', 'faculty', 'department', )
    list_filter = ('program', 'faculty', 'department', )
    search_fields = ('code', 'name', )


# Projects
# ----------------------------------------------------------------------------------------------------------------------
@register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ('name', 'author', 'faculty', 'department', 'date_created', )
    search_fields = ('name', )
    list_filter = ('faculty', 'department', )
    form = ProjectForm


# Achievements
# ----------------------------------------------------------------------------------------------------------------------
@register(Success)
class SuccessAdmin(TranslationAdmin):
    list_display = ('title', 'faculty', 'department', 'date_created', )
    search_fields = ('title', )
    list_filter = ('faculty', 'department', 'division', )
    form = SuccessForm


# Personals
# ----------------------------------------------------------------------------------------------------------------------
@register(Personal)
class PersonalAdmin(TranslationAdmin):
    list_display = ('full_name', 'profession', 'p_type', 'faculty', 'department', 'order', )
    search_fields = ('full_name', 'profession', )
    list_filter = ('faculty', 'department', 'p_type', 'division', )
    form = PersonalForm


# Materials
# ----------------------------------------------------------------------------------------------------------------------
class MaterialDocsTab(TranslationTabularInline):
    model = MaterialDocs
    extra = 0


@register(Material)
class MaterialAdmin(TranslationAdmin):
    list_display = ('title', 'author', 'date_created', )
    search_fields = ('title', )
    list_filter = ('faculty', 'department', )

    inlines = [MaterialDocsTab, ]


# Documents
# ----------------------------------------------------------------------------------------------------------------------
class DocumentFileTab(TranslationTabularInline):
    model = DocumentFile
    extra = 0


@register(Document)
class DocumentAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'faculty', 'department', )
    search_fields = ('name', )
    list_filter = ('faculty', 'department', 'division', )
    prepopulated_fields = {'slug': ('name_en',)}

    inlines = [DocumentFileTab, ]
