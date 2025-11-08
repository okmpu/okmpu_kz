from modeltranslation.translator import translator, TranslationOptions
from register.models.content import Category, Content, TextContent, FileContent, StaffContent, ImageContent, \
    PopupContent


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
    fields = ('caption', 'source_file', )


class StaffContentTranslationOptions(TranslationOptions):
    fields = ('full_name', 'profession', 'bio', )


class PopupContentTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


translator.register(Category, CategoryTranslationOptions)
translator.register(Content, ContentTranslationOptions)
translator.register(TextContent, TextContentTranslationOptions)
translator.register(FileContent, FileContentTranslationOptions)
translator.register(ImageContent, ImageContentTranslationOptions)
translator.register(StaffContent, StaffContentTranslationOptions)
translator.register(PopupContent, PopupContentTranslationOptions)
