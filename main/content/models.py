from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


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


# ContentItem
class ContentItem(models.Model):
    content = models.ForeignKey(Content, related_name='items', on_delete=models.CASCADE, verbose_name=_('Content'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(_('Object ID'))
    content_object = GenericForeignKey('content_type', 'object_id')
    order = models.PositiveIntegerField(_('Order'), default=0)

    class Meta:
        verbose_name = _('Content item')
        verbose_name_plural = _('Content items')
        ordering = ('order', )


# Text content
class TextContent(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name=_('Content'))
    body = models.TextField(verbose_name=_('Body'), blank=True, null=True)

    def __str__(self):
        return 'ID: {} '.format(self.pk) + _('Text content')

    class Meta:
        verbose_name = _('Text content')
        verbose_name_plural = _('Text contents')


# File content
class ImageContent(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name=_('Content'))
    image = models.ImageField(verbose_name=_('Image'), upload_to='content/category/images/')

    def __str__(self):
        return 'ID: {} '.format(self.pk) + _('Image content')

    class Meta:
        verbose_name = _('Image content')
        verbose_name_plural = _('Image contents')


# File content
class FileContent(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name=_('Content'))
    caption = models.CharField(verbose_name=_('Caption'), max_length=255)
    file = models.FileField(verbose_name=_('File'), upload_to='content/category/files/')

    def __str__(self):
        return 'ID: {} '.format(self.pk) + _('File content')

    class Meta:
        verbose_name = _('File content')
        verbose_name_plural = _('File contents')
