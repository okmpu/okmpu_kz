from modeltranslation.translator import translator, TranslationOptions
from main.public.models import Headliner, Announcement, News, Vacancy, Event, Program, Specialty


class HeadlinerTranslationOptions(TranslationOptions):
    fields = ('title', 'about', )


class ProgramTranslationOptions(TranslationOptions):
    fields = ('name', )


class SpecialtyTranslationOptions(TranslationOptions):
    fields = ('name', )


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


class AnnouncementTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


class VacancyTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


translator.register(Headliner, HeadlinerTranslationOptions)
translator.register(Program, ProgramTranslationOptions)
translator.register(Specialty, SpecialtyTranslationOptions)
translator.register(News, NewsTranslationOptions)
translator.register(Announcement, AnnouncementTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(Vacancy, VacancyTranslationOptions)
