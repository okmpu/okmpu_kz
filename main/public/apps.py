from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PublicConfig(AppConfig):
    name = 'main.public'
    verbose_name = _('Main | Public')
