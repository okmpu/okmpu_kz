from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Content, TextContent, FileContent, StaffContent


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


class TextContentTranslationOptions(TranslationOptions):
    fields = ('body', )


class FileContentTranslationOptions(TranslationOptions):
    fields = ('caption', )


class StaffContentTranslationOptions(TranslationOptions):
    fields = ('full_name', 'profession', 'bio', )


translator.register(Category, CategoryTranslationOptions)
translator.register(Content, ContentTranslationOptions)
translator.register(TextContent, TextContentTranslationOptions)
translator.register(FileContent, FileContentTranslationOptions)
translator.register(StaffContent, StaffContentTranslationOptions)
