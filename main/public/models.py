from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Headliner
class Headliner(models.Model):
    title = models.CharField(_('Title'), max_length=64)
    poster = models.ImageField(_('Poster'), upload_to='public/headliners/', blank=True, null=True)
    about = models.TextField(_('About'), blank=True, null=True)
    src = models.CharField(_('Source URL'), max_length=128, default='/')
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Headliner')
        verbose_name_plural = _('Headliners')


# News
class News(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    poster = models.ImageField(_('Poster'), upload_to='public/news/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')


# Announcement
class Announcement(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    poster = models.ImageField(_('Poster'), upload_to='public/announcements/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Announcement')
        verbose_name_plural = _('Announcements')


# Vacancy
class Vacancy(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancies')
