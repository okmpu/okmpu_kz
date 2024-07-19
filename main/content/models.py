from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Section
class Section(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)
    dropdown = models.BooleanField(verbose_name=_('Dropdown'), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ('index', )


# Subsection
class Subsection(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('Section'))
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Subsection')
        verbose_name_plural = _('Subsections')
        ordering = ('index', )


# Chapter
class Chapter(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('Section'))
    sub_section = models.ForeignKey(Subsection, on_delete=models.CASCADE, verbose_name=_('Subsection'))

    name = models.CharField(verbose_name=_('Name'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)
    multiple_content = models.BooleanField(verbose_name=_('Multiple content'), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Chapter')
        verbose_name_plural = _('Chapters')
        ordering = ('index', )


# Content
class Content(models.Model):
    sub_section = models.ForeignKey(Subsection, on_delete=models.CASCADE, verbose_name=_('Subsection'))
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name=_('Chapter'))

    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)
    last_update = models.DateTimeField(verbose_name=_('Last update'), auto_now=True)

    # settings

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Content')
        verbose_name_plural = _('Contents')
        ordering = ('index', )


# ----------------------------------------------------------------------------------------------------------------------
# Text content
class Text(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name=_('Content'))

    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return '{}'.format(self.content)

    class Meta:
        verbose_name = _('Text content')
        verbose_name_plural = _('Text contents')
        ordering = ('-index', )


# According content
class According(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name=_('Content'))

    title = models.CharField(verbose_name=_('Title'), max_length=255)
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _('According content')
        verbose_name_plural = _('According contents')
        ordering = ('-index', )


# File content
class File(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name=_('Content'))

    title = models.CharField(verbose_name=_('Title'), max_length=255)
    file = models.FileField(verbose_name=_('File'), upload_to='category/topic/content/files/')
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return '{} {}'.format(self.content, self.title)

    class Meta:
        verbose_name = _('File content')
        verbose_name_plural = _('File contents')
        ordering = ('-index',)


# Staff content
class Staff(models.Model):
    content = models.ForeignKey(Content, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Content'))

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    image = models.ImageField(_('Image'), upload_to='staff/', blank=True, null=True)
    profession = models.CharField(_('Profession'), max_length=255)
    about = models.TextField(_('About'), blank=True, null=True)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return '{} {}'.format(self.content, self.user)

    class Meta:
        verbose_name = _('Staff content')
        verbose_name_plural = _('Staff contents')
        ordering = ('index', )
