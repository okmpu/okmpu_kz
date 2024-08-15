from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Faculty
class Faculty(models.Model):
    FACULTY_TYPE = (
        ('DEFAULT', _('Default')),
        ('INSTITUTE', _('Institute')),
        ('COLLEGE', _('College')),
    )
    name = models.CharField(_('Name'), max_length=128)
    slug = models.CharField(_('Slug'), max_length=128)
    image = models.ImageField(_('Image'), upload_to='university/faculties/avatars', null=True, blank=True)
    poster = models.ImageField(_('Poster'), upload_to='university/faculties/posters', null=True, blank=True)
    faculty_type = models.CharField(_('Faculty type'), choices=FACULTY_TYPE, default='DEFAULT', max_length=16)
    about = models.TextField(_('About'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')


# Department
class Department(models.Model):
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='departments', verbose_name=_('Faculty')
    )
    name = models.CharField(_('Name'), max_length=128)
    slug = models.CharField(_('Slug'), max_length=128)
    about = models.TextField(_('About'), blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.faculty.name, self.name)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')


# Programs
class FacultyProgram(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    slug = models.SlugField(_('Slug'), max_length=64)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='programs', verbose_name=_('Department')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')


class FacultySpecialty(models.Model):
    program = models.ForeignKey(
        FacultyProgram, on_delete=models.CASCADE,
        related_name='program_items', verbose_name=_('Program')
    )
    code = models.CharField(_('Code'), max_length=128)
    name = models.CharField(_('Name'), max_length=128)

    def __str__(self):
        return '{} - {}'.format(self.code, self.name)

    class Meta:
        verbose_name = _('Specialty')
        verbose_name_plural = _('Specialties')


# Projects
class Project(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='projects', verbose_name=_('Department')
    )
    name = models.CharField(_('Name'), max_length=128)
    author = models.CharField(_('Author'), max_length=128)
    file = models.FileField(_('File'), upload_to='university/faculties/projects/', null=True, blank=True)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


# Personals
class Personal(models.Model):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_personals', verbose_name=_('Department')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    image = models.ImageField(_('Image'), upload_to='university/personals/', blank=True, null=True)
    profession = models.CharField(_('Profession'), max_length=128)
    phone = models.CharField(_('Phone'), max_length=64, blank=True, null=True)
    about = models.TextField(_('About'), blank=True, null=True)

    def __str__(self):
        return '{} {} - {}'.format(self.user.first_name, self.user.last_name, self.profession)

    class Meta:
        verbose_name = _('Personal')
        verbose_name_plural = _('Personals')
