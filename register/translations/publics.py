from modeltranslation.translator import translator, TranslationOptions
from register.models.publics import Headliner, Public


# Headliner
# ----------------------------------------------------------------------------------------------------------------------
class HeadlinerTranslationOptions(TranslationOptions):
    fields = ('title', 'about', )


# Public
# ----------------------------------------------------------------------------------------------------------------------
class PublicTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


translator.register(Headliner, HeadlinerTranslationOptions)
translator.register(Public, PublicTranslationOptions)
