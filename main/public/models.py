from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from main.university.models import Department, Faculty, Division
from main.validators import validate_file_size, validate_poster


# Headliner
# ----------------------------------------------------------------------------------------------------------------------
class Headliner(models.Model):
    title = models.CharField(_('Title'), max_length=64)
    poster = models.ImageField(
        _('Poster'), upload_to='public/headliners/',
        blank=True, null=True, validators=[validate_poster]
    )
    about = models.TextField(_('About'), blank=True, null=True)
    src = models.CharField(_('Source URL'), max_length=128, default='/')
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Headliner')
        verbose_name_plural = _('Headliners')
        ordering = ('order', )


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
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE,
        related_name='division_news', verbose_name=_('Division'), null=True, blank=True,
        help_text=_('Warning! This field is not relevant for faculties and departments')
    )
    title = models.CharField(_('Title'), max_length=255)
    poster = models.ImageField(
        _('Poster'), upload_to='public/news/',
        blank=True, null=True, validators=[validate_poster]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ('-date_created', )


class NewsFile(models.Model):
    own = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_files', verbose_name=_('News'))
    title = models.CharField(_('Title'), max_length=128, default='')
    file = models.FileField(
        _('File'), upload_to='public/news/files/',
        blank=True, null=True, validators=[validate_file_size]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News file')
        verbose_name_plural = _('News files')


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
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE,
        related_name='division_announcements', verbose_name=_('Division'), null=True, blank=True,
        help_text=_('Warning! This field is not relevant for faculties and departments')
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


class AnnouncementFile(models.Model):
    own = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='announcement_files', verbose_name=_('Announcement'))
    title = models.CharField(_('Title'), max_length=128, default='')
    file = models.FileField(
        _('File'), upload_to='public/announcement/files/',
        blank=True, null=True, validators=[validate_file_size]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Announcement file')
        verbose_name_plural = _('Announcement files')


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
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE,
        related_name='division_events', verbose_name=_('Division'), null=True, blank=True,
        help_text=_('Warning! This field is not relevant for faculties and departments')
    )
    title = models.CharField(_('Title'), max_length=255)
    poster = models.ImageField(
        _('Poster'), upload_to='public/events/',
        blank=True, null=True, validators=[validate_poster]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ('-date_created',)


class EventFile(models.Model):
    own = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_files', verbose_name=_('Event'))
    title = models.CharField(_('Title'), max_length=128, default='')
    file = models.FileField(
        _('File'), upload_to='public/events/files/',
        blank=True, null=True, validators=[validate_file_size]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Event file')
        verbose_name_plural = _('Event files')


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
    poster = models.ImageField(
        _('Poster'), upload_to='public/journals/',
        blank=True, null=True, validators=[validate_file_size]
    )
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
    poster = models.ImageField(
        _('Poster'), upload_to='public/partners/',
        blank=True, null=True, validators=[validate_file_size]
    )
    url = models.CharField(_('URL'), max_length=255)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Partner')
        verbose_name_plural = _('Partners')
        ordering = ('order', )



# PageView model
# ----------------------------------------------------------------------------------------------------------------------
class PageView(models.Model):
    pathname = models.CharField(_('Pathname'), max_length=255)
    auth_users_count = models.PositiveBigIntegerField(_('Auth users count'), default=0)
    users_count = models.PositiveBigIntegerField(_('Users count'), default=0)
    timestamp = models.DateTimeField(_('Timestamp'), auto_now_add=True)

    def __str__(self):
        return f'Users: {self.users_count} - Auth users: {self.auth_users_count}'
