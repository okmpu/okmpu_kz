from modeltranslation.translator import translator, TranslationOptions
from .models import Section, Chapter, Subsection, Content, Text, File


class SectionTranslationOptions(TranslationOptions):
    fields = ('name', )


class SubsectionTranslationOptions(TranslationOptions):
    fields = ('name', )


class ChapterTranslationOptions(TranslationOptions):
    fields = ('name', )


class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


class TextTranslationOptions(TranslationOptions):
    fields = ('description', )


class FileTranslationOptions(TranslationOptions):
    fields = ('title', )


translator.register(Section, SectionTranslationOptions)
translator.register(Subsection, SubsectionTranslationOptions)
translator.register(Chapter, ChapterTranslationOptions)
translator.register(Content, ContentTranslationOptions)
translator.register(Text, TextTranslationOptions)
translator.register(File, FileTranslationOptions)
