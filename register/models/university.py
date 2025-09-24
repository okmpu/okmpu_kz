from django.db import models
from django.utils.translation import gettext_lazy as _
from register.validators import validate_file_size, validate_logo, validate_poster


# Faculty
# ----------------------------------------------------------------------------------------------------------------------
class Faculty(models.Model):
    FACULTY_TYPE = (
        ('faculty', _('Faculty')),
        ('institute', _('Institute')),
        ('college', _('College')),
    )

    name = models.CharField(_('Name'), max_length=128)
    slug = models.CharField(_('Slug'), max_length=128)
    image = models.ImageField(
        _('Image'), upload_to='register/university/faculty/avatars',
        null=True, blank=True, validators=[validate_logo]
    )
    poster = models.ImageField(
        _('Poster'), upload_to='register/university/faculty/posters',
        null=True, blank=True, validators=[validate_poster]
    )
    faculty_type = models.CharField(_('Faculty type'), choices=FACULTY_TYPE, default='faculty', max_length=16)
    about = models.TextField(_('About the faculty'), blank=True, null=True)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')
        ordering = ('order', )


# Department
# ----------------------------------------------------------------------------------------------------------------------
class Department(models.Model):
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='departments', verbose_name=_('Faculty')
    )
    image = models.ImageField(
        _('Image'), upload_to='register/university/department/avatars',
        null=True, blank=True, validators=[validate_logo]
    )
    poster = models.ImageField(
        _('Poster'), upload_to='register/university/department/posters',
        null=True, blank=True, validators=[validate_poster]
    )
    name = models.CharField(_('Name'), max_length=128)
    slug = models.CharField(_('Slug'), max_length=128)
    about = models.TextField(_('About the department'), blank=True, null=True)
    # order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return '{} - {}'.format(self.faculty.name, self.name)

    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')


# Division
# ----------------------------------------------------------------------------------------------------------------------
class Division(models.Model):
    DIV_TYPE = (
        ('div', _('Division/Center division')),
        ('department', _('Department division')),
        ('management', _('Management division')),
    )

    name = models.CharField(_('Name'), max_length=128)
    slug = models.SlugField(_('Slug'), max_length=128)
    image = models.ImageField(
        _('Image'), upload_to='register/university/division/avatars',
        null=True, blank=True, validators=[validate_logo]
    )
    poster = models.ImageField(
        _('Poster'), upload_to='register/university/division/posters',
        null=True, blank=True, validators=[validate_poster]
    )
    div_type = models.CharField(_('Division type'), choices=DIV_TYPE, default='div')
    about = models.TextField(_('About the division'), blank=True, null=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children',
        null=True, blank=True, verbose_name=_('Parent division')
    )
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Division')
        verbose_name_plural = _('Divisions')
        ordering = ('order', )


# Personals
# ----------------------------------------------------------------------------------------------------------------------
class Personal(models.Model):
    PERSONAL_TYPE = (
        (
            _('Faculty'),
            (
                ('deans_office', _("Dean's office")),
                ('department_manage', _('Department management')),
                ('teacher', _('Teacher/Professors')),
                ('student', _('Active students')),
            ),
        ),
        (
            _('Division'),
            (
                ('head', _('Head of Department')),
                ('employee', _('Employee')),
            )
        )
    )

    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='faculty_personals', verbose_name=_('Faculty'), null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_personals', verbose_name=_('Department'), null=True, blank=True
    )
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE,
        related_name='division_personals', verbose_name=_('Division'), null=True, blank=True,
        help_text=_('Warning! This field is not relevant for faculties and departments')
    )
    full_name = models.CharField(_('Full name'), max_length=128, blank=True, null=True)
    image = models.ImageField(
        _('Image'), upload_to='register/university/personals/',
        blank=True, null=True, validators=[validate_logo]
    )
    profession = models.CharField(_('Profession/Activity'), max_length=128)
    p_type = models.CharField(
        _('Personal type'), max_length=128,
        choices=PERSONAL_TYPE, default='student'
    )
    phone = models.CharField(_('Phone'), max_length=128, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=128, blank=True, null=True)
    about = models.TextField(_('About'), blank=True, null=True)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return '{} - {}'.format(self.full_name, self.profession)

    class Meta:
        verbose_name = _('Personal')
        verbose_name_plural = _('Personals')
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
        Program, on_delete=models.SET_NULL,
        related_name='program_items', verbose_name=_('Program'), null=True, blank=True
    )
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='program_items', verbose_name=_('Faculty'), null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='program_items', verbose_name=_('Department'), null=True, blank=True
    )
    code = models.CharField(_('Code'), max_length=128)
    name = models.CharField(_('Name'), max_length=128)
    url = models.URLField(_('URL'), max_length=128, null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.code, self.name)

    class Meta:
        verbose_name = _('Specialty')
        verbose_name_plural = _('Specialties')


# Projects
# ----------------------------------------------------------------------------------------------------------------------
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
    file = models.FileField(
        _('File'), upload_to='register/university/projects/',
        null=True, blank=True, validators=[validate_file_size]
    )
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


# Materials
# ----------------------------------------------------------------------------------------------------------------------
class Material(models.Model):
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='faculty_materials', verbose_name=_('Faculty'), null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_materials', verbose_name=_('Department'), null=True, blank=True
    )
    title = models.CharField(_('Title'), max_length=128)
    author = models.ForeignKey(
        Personal, on_delete=models.CASCADE, related_name='author_materials',
        verbose_name=_('Author'), blank=True, null=True
    )
    date_created = models.DateTimeField(_('Date created'), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Edu material')
        verbose_name_plural = _('Edu materials')


class MaterialDocs(models.Model):
    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, verbose_name=_('Edu material'),
        related_name='material_files'
    )
    caption = models.CharField(_('Name'), max_length=128)
    file = models.FileField(
        _('File'), upload_to='register/university/materials/',
        null=True, blank=True, validators=[validate_file_size]
    )

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = _('Edu material')
        verbose_name_plural = _('Edu materials')


# Achievements
# ----------------------------------------------------------------------------------------------------------------------
class Success(models.Model):
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='faculty_achievements', verbose_name=_('Faculty'), null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_achievements', verbose_name=_('Department'), null=True, blank=True
    )
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE,
        related_name='division_achievements', verbose_name=_('Division'), null=True, blank=True,
        help_text=_('Warning! This field is not relevant for faculties and departments')
    )
    title = models.CharField(_('Title'), max_length=128)
    file = models.FileField(
        _('File'), upload_to='register/university/achievements/',
        null=True, blank=True, validators=[validate_file_size]
    )
    description = models.TextField(_('Description'), blank=True, null=True)
    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Success')
        verbose_name_plural = _('Achievements')


# Documents
# ----------------------------------------------------------------------------------------------------------------------
class Document(models.Model):
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE,
        related_name='faculty_documents', verbose_name=_('Faculty'), null=True, blank=True
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='department_documents', verbose_name=_('Department'), null=True, blank=True
    )
    division = models.ForeignKey(
        Division, on_delete=models.CASCADE,
        related_name='division_documents', verbose_name=_('Division'), null=True, blank=True,
        help_text=_('Warning! This field is not relevant for faculties and departments')
    )
    name = models.CharField(_('Name'), max_length=128)
    slug = models.CharField(_('Slug'), max_length=128)
    description = models.TextField(_('Description'), blank=True, null=True)
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
        ordering = ('order', )


class DocumentFile(models.Model):
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, verbose_name=_('Document'),
        related_name='document_files'
    )
    title = models.CharField(_('Title'), max_length=128)
    file = models.FileField(
        _('File'), upload_to='register/university/documents/',
        null=True, blank=True, validators=[validate_file_size]
    )
    order = models.PositiveSmallIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Document file')
        verbose_name_plural = _('Document files')
        ordering = ('-order', )
