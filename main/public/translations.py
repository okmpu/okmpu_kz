from modeltranslation.translator import translator, TranslationOptions
from main.public.models import Headliner, Announcement, News, Vacancy, Event


class HeadlinerTranslationOptions(TranslationOptions):
    fields = ('title', 'about', )


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


class VacancyTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


translator.register(Headliner, HeadlinerTranslationOptions)
translator.register(News, NewsTranslationOptions)
translator.register(Announcement, AnnouncementTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(Vacancy, VacancyTranslationOptions)
