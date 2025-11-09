from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from register.validators import validate_file_size, validate_poster
from register.models.university import Faculty, Department, Division


# Resource
# ----------------------------------------------------------------------------------------------------------------------
class Resource(models.Model):
    label = models.CharField(_('Label'), max_length=128)
    url = models.URLField(_('URL'))
    new_tab = models.BooleanField(_('New tab'), default=False)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = _('Resource')
        verbose_name_plural = _('Resources')
        ordering = ('order', )


# Headliner
# ----------------------------------------------------------------------------------------------------------------------
class Headliner(models.Model):
    title = models.CharField(_('Title'), max_length=64)
    poster = models.ImageField(
        _('Poster'), upload_to='register/public/headliners/',
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


# Partner
# ----------------------------------------------------------------------------------------------------------------------
class Partner(models.Model):
    name = models.CharField(_('Partner name'), max_length=255)
    poster = models.ImageField(
        _('Poster'), upload_to='register/public/partners/',
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


# Public
# ----------------------------------------------------------------------------------------------------------------------
class Public(models.Model):
    PUBLIC_TYPE = (
        ('news', _('News')),
        ('ann', _('Announcement')),
    )
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='faculty_publics', verbose_name=_('Faculty'), blank=True, null=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_publics', verbose_name=_('Department'), blank=True, null=True
    )
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE,
        related_name='division_publics', verbose_name=_('Division'), null=True, blank=True,
        help_text=_('Warning! This field is not relevant for faculties and departments')
    )
    title = models.CharField(_('Title'), max_length=255)
    public_type = models.CharField(_('Public type'), max_length=24, choices=PUBLIC_TYPE, default='news')
    poster = models.ImageField(
        _('Poster'), upload_to='register/publics/public/posters/',
        blank=True, null=True, validators=[validate_poster]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Public')
        verbose_name_plural = _('Publics')
        ordering = ('-date_created', )


class PublicFile(models.Model):
    own = models.ForeignKey(Public, on_delete=models.CASCADE, related_name='public_files', verbose_name=_('News'))
    title = models.CharField(_('Title'), max_length=128, default='')
    file = models.FileField(
        _('File'), upload_to='register/publics/public/files/',
        blank=True, null=True, validators=[validate_file_size]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Public file')
        verbose_name_plural = _('Public files')
