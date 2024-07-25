from django.db import models
from django.utils.translation import gettext_lazy as _


# Programs
class Program(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    slug = models.SlugField(_('Slug'), max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')


class ProgramItem(models.Model):
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE,
        related_name='program_items', verbose_name=_('Program')
    )
    code = models.CharField(_('Code'), max_length=128)
    name = models.CharField(_('Name'), max_length=128)

    def __str__(self):
        return '{} - {}'.format(self.code, self.name)

