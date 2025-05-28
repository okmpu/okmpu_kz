from django.db import models
from django.utils.translation import gettext_lazy as _

from main.validators import validate_file_size, validate_poster


# Headliner
# ----------------------------------------------------------------------------------------------------------------------
class Headliner(models.Model):
    title = models.CharField(_('Title'), max_length=64)
    poster = models.ImageField(
        _('Poster'), upload_to='register/headliners/',
        blank=True, null=True, validators=[validate_poster]
    )
    about = models.TextField(_('About'), blank=True, null=True)
    src = models.CharField(_('Source URL'), max_length=128, default='/')
    order = models.PositiveSmallIntegerField(_('Order'), default=0)
    is_archive = models.BooleanField(_('Is archive'), default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Headliner')
        verbose_name_plural = _('Headliners')
        ordering = ('order', )

