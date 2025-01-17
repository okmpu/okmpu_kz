from django.db import models
from django.utils.translation import gettext_lazy as _
from main.validators import validate_logo


# Category
# ----------------------------------------------------------------------------------------------------------------------
class Category(models.Model):
    APP_NAME = (
        ('none', _('None')),
        ('content', _('Content app')),
        ('university', _('University app')),
    )
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'), max_length=100)
    app_name = models.CharField(_('App name'), choices=APP_NAME, default='none')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children',
        null=True, blank=True, verbose_name=_('Parent')
    )
    multiple = models.BooleanField(_('Multiple'), default=False)
    url = models.CharField(_('URL'), max_length=128, blank=True, null=True)
    target = models.BooleanField(_('Target'), default=False)
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('order', )


# Content
class Content(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='contents', verbose_name=_('Category')
    )
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    last_update = models.DateTimeField(verbose_name=_('Last update'), auto_now=True)
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Content')
        verbose_name_plural = _('Contents')
        ordering = ('order', )


# Text content
class TextContent(models.Model):
    content = models.ForeignKey(
        Content, on_delete=models.CASCADE,
        related_name='text_contents', verbose_name=_('Content')
    )
    body = models.TextField(verbose_name=_('Body'), blank=True, null=True)
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return 'ID: {} '.format(self.pk) + _('Text content')

    class Meta:
        verbose_name = _('Text content')
        verbose_name_plural = _('Text contents')
        ordering = ('order',)

# File content
class ImageContent(models.Model):
    content = models.ForeignKey(
        Content, on_delete=models.CASCADE,
        related_name='image_contents', verbose_name=_('Content')
    )
    image = models.ImageField(verbose_name=_('Image'), upload_to='content/category/images/')
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return 'ID: {} '.format(self.pk) + _('Image content')

    class Meta:
        verbose_name = _('Image content')
        verbose_name_plural = _('Image contents')
        ordering = ('order', )

# File content
class FileContent(models.Model):
    content = models.ForeignKey(
        Content, on_delete=models.CASCADE,
        related_name='file_contents', verbose_name=_('Content')
    )
    caption = models.CharField(verbose_name=_('Caption'), max_length=255)
    # file = models.FileField(verbose_name=_('File'), upload_to='content/category/files/')
    source_file = models.FileField(_('Source file'), upload_to='content/category/files/', blank=True, null=True)
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return 'ID: {} '.format(self.pk) + _('File content')

    class Meta:
        verbose_name = _('File content')
        verbose_name_plural = _('File contents')
        ordering = ('order', )

# Staff content
class StaffContent(models.Model):
    content = models.ForeignKey(
        Content, on_delete=models.CASCADE,
        related_name='staff_contents', verbose_name=_('Content')
    )
    full_name = models.CharField(verbose_name=_('Full name'), max_length=128)
    image = models.ImageField(
        verbose_name=_('Image'), upload_to='content/category/staff/',
        validators=[validate_logo], blank=True, null=True
    )
    profession = models.CharField(verbose_name=_('Profession'), max_length=128)
    bio = models.TextField(verbose_name=_('Bio'), blank=True, null=True)
    phone = models.CharField(verbose_name=_('Phone'), max_length=32, blank=True, null=True)
    email = models.EmailField(verbose_name=_('Email'), max_length=64, blank=True, null=True)
    order = models.PositiveIntegerField(_('Order'), default=0)

    def __str__(self):
        return 'ID: {} '.format(self.pk) + _('Staff content')

    class Meta:
        verbose_name = _('Staff content')
        verbose_name_plural = _('Staff contents')
        ordering = ('order', )
