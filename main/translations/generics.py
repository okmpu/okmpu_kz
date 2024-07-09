from modeltranslation.translator import translator, TranslationOptions
from ..models import Category, Topic, Chapter, Content, FileContent, TextContent


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


class TopicTranslationOptions(TranslationOptions):
    fields = ('name', 'description', )


class ChapterTranslationOptions(TranslationOptions):
    fields = ('name', )


class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


class TextContentTranslationOptions(TranslationOptions):
    fields = ('description', )


class FileContentTranslationOptions(TranslationOptions):
    fields = ('title', 'file', )


translator.register(Category, CategoryTranslationOptions)
translator.register(Topic, TopicTranslationOptions)
translator.register(Chapter, ChapterTranslationOptions)
translator.register(Content, ContentTranslationOptions)
translator.register(TextContent, TextContentTranslationOptions)
translator.register(FileContent, FileContentTranslationOptions)
