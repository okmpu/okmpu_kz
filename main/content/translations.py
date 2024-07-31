from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Content, TextContent, FileContent


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


class TextContentTranslationOptions(TranslationOptions):
    fields = ('body', )


class FileContentTranslationOptions(TranslationOptions):
    fields = ('caption', )


translator.register(Category, CategoryTranslationOptions)
translator.register(Content, ContentTranslationOptions)
translator.register(TextContent, TextContentTranslationOptions)
translator.register(FileContent, FileContentTranslationOptions)
