from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    APP_NAME = (
        ('content', _('Content app')),
        ('university', _('University app')),
    )
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'), max_length=100)
    app_name = models.CharField(_('App name'), choices=APP_NAME, default='content')
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children',
        null=True, blank=True, verbose_name=_('Parent')
    )
    multiple = models.BooleanField(_('Multiple'), default=False)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('index', )


# Content
class Content(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='contents', verbose_name=_('Category')
    )
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)
    last_update = models.DateTimeField(verbose_name=_('Last update'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Content')
        verbose_name_plural = _('Contents')
        ordering = ('index', )


# Text content
class TextContent(models.Model):
    content = models.ForeignKey(
        Content, on_delete=models.CASCADE,
        related_name='text_contents', verbose_name=_('Content')
    )
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return '{}'.format(self.content)

    class Meta:
        verbose_name = _('Text content')
        verbose_name_plural = _('Text contents')
        ordering = ('index', )


# Popup content
class PopupContent(models.Model):
    content = models.ForeignKey(
        Content, on_delete=models.CASCADE,
        related_name='popup_contents', verbose_name=_('Content')
    )
    trigger = models.CharField(verbose_name=_('Trigger'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return '{} {}'.format(self.content, self.trigger)

    class Meta:
        verbose_name = _('Popup content')
        verbose_name_plural = _('Popup contents')
        ordering = ('index', )


# File content
class FileContent(models.Model):
    content = models.ForeignKey(
        Content, on_delete=models.CASCADE,
        related_name='file_contents', verbose_name=_('Content')
    )
    caption = models.CharField(verbose_name=_('Caption'), max_length=255)
    file = models.FileField(verbose_name=_('File'), upload_to='content/category/files/')
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return '{} {}'.format(self.content, self.caption)

    class Meta:
        verbose_name = _('File content')
        verbose_name_plural = _('File contents')
        ordering = ('index',)


# Staff content
class StaffContent(models.Model):
    content = models.ForeignKey(
        Content, on_delete=models.SET_NULL,
        related_name='staff_contents', null=True, blank=True, verbose_name=_('Content')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    image = models.ImageField(_('Image'), upload_to='content/category/staff/', blank=True, null=True)
    profession = models.CharField(_('Profession'), max_length=255)
    about = models.TextField(_('About'), blank=True, null=True)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return '{} {}'.format(self.content, self.user)

    class Meta:
        verbose_name = _('Staff content')
        verbose_name_plural = _('Staff contents')
        ordering = ('index', )
