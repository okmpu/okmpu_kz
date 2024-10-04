from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from main.university.models import Department, Faculty


# Headliner
# ----------------------------------------------------------------------------------------------------------------------
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
        ordering = ('order', )


# Programs
# ----------------------------------------------------------------------------------------------------------------------
class Program(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    slug = models.SlugField(_('Slug'), max_length=64)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')
        ordering = ('order', )


class Specialty(models.Model):
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE,
        related_name='program_items', verbose_name=_('Program')
    )
    code = models.CharField(_('Code'), max_length=128)
    name = models.CharField(_('Name'), max_length=128)

    def __str__(self):
        return '{} - {}'.format(self.code, self.name)

    class Meta:
        verbose_name = _('Specialty')
        verbose_name_plural = _('Specialties')


# News
# ----------------------------------------------------------------------------------------------------------------------
class News(models.Model):
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='faculty_news', verbose_name=_('Faculty'), blank=True, null=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_news', verbose_name=_('Department'), blank=True, null=True
    )
    title = models.CharField(_('Title'), max_length=255)
    poster = models.ImageField(_('Poster'), upload_to='public/news/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ('-date_created', )


# Announcement
# ----------------------------------------------------------------------------------------------------------------------
class Announcement(models.Model):
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='faculty_announcements', verbose_name=_('Faculty'), blank=True, null=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_announcements', verbose_name=_('Department'), blank=True, null=True
    )
    title = models.CharField(_('Title'), max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Announcement')
        verbose_name_plural = _('Announcements')
        ordering = ('-date_created',)


# Events
# ----------------------------------------------------------------------------------------------------------------------
class Event(models.Model):
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='faculty_events', verbose_name=_('Faculty'), blank=True, null=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_events', verbose_name=_('Department'), blank=True, null=True
    )
    title = models.CharField(_('Title'), max_length=255)
    poster = models.ImageField(_('Poster'), upload_to='public/events/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ('-date_created',)


# Vacancy
# ----------------------------------------------------------------------------------------------------------------------
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
        ordering = ('-date_created',)


# Journal
# ----------------------------------------------------------------------------------------------------------------------
class Journal(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    poster = models.ImageField(_('Poster'), upload_to='public/journals/', blank=True, null=True)
    file = models.FileField(_('File'), upload_to='public/journals/', blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Journal')
        verbose_name_plural = _('Journals')
        ordering = ('-date_created',)


# Journal
# ----------------------------------------------------------------------------------------------------------------------
class Partner(models.Model):
    name = models.CharField(_('Partner name'), max_length=255)
    poster = models.ImageField(_('Poster'), upload_to='public/partners/', blank=True, null=True)
    url = models.CharField(_('URL'), max_length=255)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')
        ordering = ('order', )
