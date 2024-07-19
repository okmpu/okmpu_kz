from django.db import models
from django.utils.translation import gettext_lazy as _


class Faculty(models.Model):
    name = models.CharField(_('Name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')
