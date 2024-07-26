from modeltranslation.translator import translator, TranslationOptions
from main.university.models import Faculty, Department, Program, Specialty


class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', 'about', )


class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'about', )


class ProgramTranslationOptions(TranslationOptions):
    fields = ('name', )


class SpecialtyTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(Faculty, FacultyTranslationOptions)
translator.register(Department, DepartmentTranslationOptions)
translator.register(Program, ProgramTranslationOptions)
translator.register(Specialty, SpecialtyTranslationOptions)
