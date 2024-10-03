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
    image = models.ImageField(_('Image'), upload_to='university/faculties/avatars', null=True, blank=True)
    poster = models.ImageField(_('Poster'), upload_to='university/faculties/posters', null=True, blank=True)
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
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')
        ordering = ('order', )


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
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='faculty_projects', verbose_name=_('Faculty'), null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_projects', verbose_name=_('Department'), null=True, blank=True
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


# Achievements
class Success(models.Model):
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='faculty_achievements', verbose_name=_('Faculty'), null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_achievements', verbose_name=_('Department'), null=True, blank=True
    )
    title = models.CharField(_('Title'), max_length=128)
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Success')
        verbose_name_plural = _('Achievements')


# Personals
class Personal(models.Model):
    PERSONAL_TYPE = (
        ('STUDENT', _('Student')),
        ('TEACHER', _('Teacher')),
        ('MANAGEMENT', _('Management')),
    )

    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='faculty_personals', verbose_name=_('Faculty'), null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_personals', verbose_name=_('Department'), null=True, blank=True
    )
    full_name = models.CharField(_('Full name'), max_length=128, blank=True, null=True)
    image = models.ImageField(_('Image'), upload_to='university/personals/', blank=True, null=True)
    profession = models.CharField(_('Profession'), max_length=128)
    p_type = models.CharField(_('Personal type'), max_length=128, choices=PERSONAL_TYPE, default='MANAGEMENT')
    phone = models.CharField(_('Phone'), max_length=64, blank=True, null=True)
    about = models.TextField(_('About'), blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.full_name, self.profession)

    class Meta:
        verbose_name = _('Personal')
        verbose_name_plural = _('Personals')
