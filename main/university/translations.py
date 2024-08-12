from modeltranslation.translator import translator, TranslationOptions
from main.university.models import Faculty, Department, Program, Specialty, Personal, Project


class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', 'about', )


class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'about', )


class ProgramTranslationOptions(TranslationOptions):
    fields = ('name', )


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'author', )


class SpecialtyTranslationOptions(TranslationOptions):
    fields = ('name', )


class PersonalTranslationOptions(TranslationOptions):
    fields = ('profession', 'about', )


translator.register(Faculty, FacultyTranslationOptions)
translator.register(Department, DepartmentTranslationOptions)
translator.register(Program, ProgramTranslationOptions)
translator.register(Specialty, SpecialtyTranslationOptions)
translator.register(Personal, PersonalTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
