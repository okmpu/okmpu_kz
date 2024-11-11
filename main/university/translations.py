from modeltranslation.translator import translator, TranslationOptions
from main.university.models import Faculty, Department, Personal, Project, FacultyProgram, FacultySpecialty, Success, \
    Material, MaterialDocs, DocumentFile, Document


# Faculty
# ----------------------------------------------------------------------------------------------------------------------
class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', 'about', )


# Department
# ----------------------------------------------------------------------------------------------------------------------
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'about', )


# Program
# ----------------------------------------------------------------------------------------------------------------------
class ProgramTranslationOptions(TranslationOptions):
    fields = ('name', )


class SpecialtyTranslationOptions(TranslationOptions):
    fields = ('name', )


# Project
# ----------------------------------------------------------------------------------------------------------------------
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'author', )


# Material
# ----------------------------------------------------------------------------------------------------------------------
class MaterialDocsTranslationOptions(TranslationOptions):
    fields = ('caption', )

class MaterialTranslationOptions(TranslationOptions):
    fields = ('title', 'author', )


# Achievements
# ----------------------------------------------------------------------------------------------------------------------
class SuccessTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


# Personals
# ----------------------------------------------------------------------------------------------------------------------
class PersonalTranslationOptions(TranslationOptions):
    fields = ('full_name', 'profession', 'about', )


# Material
# ----------------------------------------------------------------------------------------------------------------------
class DocumentFileTranslationOptions(TranslationOptions):
    fields = ('title', )

class DocumentTranslationOptions(TranslationOptions):
    fields = ('name', )


translator.register(Faculty, FacultyTranslationOptions)
translator.register(Department, DepartmentTranslationOptions)
translator.register(FacultyProgram, ProgramTranslationOptions)
translator.register(FacultySpecialty, SpecialtyTranslationOptions)
translator.register(Personal, PersonalTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(Material, MaterialTranslationOptions)
translator.register(MaterialDocs, MaterialDocsTranslationOptions)
translator.register(Success, SuccessTranslationOptions)
translator.register(DocumentFile, DocumentFileTranslationOptions)
translator.register(Document, DocumentTranslationOptions)
