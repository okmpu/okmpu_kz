from modeltranslation.translator import translator, TranslationOptions
from main.university.models import Faculty, Department, Personal, Project, FacultyProgram, FacultySpecialty, Success


class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', 'about', )


class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'about', )


class ProgramTranslationOptions(TranslationOptions):
    fields = ('name', )


class SpecialtyTranslationOptions(TranslationOptions):
    fields = ('name', )


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'author', )


class SuccessTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


class PersonalTranslationOptions(TranslationOptions):
    fields = ('full_name', 'profession', 'about', )


translator.register(Faculty, FacultyTranslationOptions)
translator.register(Department, DepartmentTranslationOptions)
translator.register(FacultyProgram, ProgramTranslationOptions)
translator.register(FacultySpecialty, SpecialtyTranslationOptions)
translator.register(Personal, PersonalTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(Success, SuccessTranslationOptions)
