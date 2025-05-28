from modeltranslation.translator import translator, TranslationOptions
from register.models import Headliner


class HeadlinerTranslationOptions(TranslationOptions):
    fields = ('title', 'about', )


translator.register(Headliner, HeadlinerTranslationOptions)
