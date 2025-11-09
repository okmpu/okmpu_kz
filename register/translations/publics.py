from modeltranslation.translator import translator, TranslationOptions
from register.models.publics import Headliner, Public, Resource


# Resource
class ResourceTranslationOptions(TranslationOptions):
    fields = ('label', )

# Headliner
class HeadlinerTranslationOptions(TranslationOptions):
    fields = ('title', 'about', )


# Public
class PublicTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


translator.register(Headliner, HeadlinerTranslationOptions)
translator.register(Public, PublicTranslationOptions)
translator.register(Resource, ResourceTranslationOptions)