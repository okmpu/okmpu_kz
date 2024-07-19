from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContentConfig(AppConfig):
    name = 'main.content'
    verbose_name = _('Main | Contents')
