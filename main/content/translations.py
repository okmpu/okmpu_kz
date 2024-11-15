from modeltranslation.translator import translator, TranslationOptions
from .models import Category, Content, TextContent, FileContent, StaffContent, ImageContent


# Category
# ----------------------------------------------------------------------------------------------------------------------
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


# Content
# ----------------------------------------------------------------------------------------------------------------------
class ContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


# Contents
class TextContentTranslationOptions(TranslationOptions):
    fields = ('body', )


class ImageContentTranslationOptions(TranslationOptions):
    fields = ('image', )


class FileContentTranslationOptions(TranslationOptions):
    fields = ('caption', )


class StaffContentTranslationOptions(TranslationOptions):
    fields = ('full_name', 'profession', 'bio', )


translator.register(Category, CategoryTranslationOptions)
translator.register(Content, ContentTranslationOptions)
translator.register(TextContent, TextContentTranslationOptions)
translator.register(FileContent, FileContentTranslationOptions)
translator.register(ImageContent, ImageContentTranslationOptions)
translator.register(StaffContent, StaffContentTranslationOptions)
