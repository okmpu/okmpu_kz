from django.db import models
from django.utils.translation import gettext_lazy as _


# Main navigation
class Category(models.Model):
    name = models.CharField(verbose_name=_('Category name'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, default='slug')
    src = models.CharField(verbose_name=_('Source URL'), max_length=255, default='/')
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)
    dropdown = models.BooleanField(verbose_name=_('Dropdown'), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('index', )


# Topic
class Topic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    name = models.CharField(verbose_name=_('Topic name'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, default='slug')
    src = models.CharField(verbose_name=_('Source URL'), max_length=255, default='/')
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Topic')
        verbose_name_plural = _('Topics')
        ordering = ('index', )


class Chapter(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name=_('Topic'))
    name = models.CharField(verbose_name=_('Chapter name'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, default='slug')
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)
    multiple_content = models.BooleanField(verbose_name=_('Multiple content'), default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Chapter')
        verbose_name_plural = _('Chapters')
        ordering = ('-index', )


class Content(models.Model):
    CONTENT_TYPE = (
        ('TXT', _('Is text content')),
        ('FL', _('Is file content')),
        ('IMG', _('Is image content')),
        ('ALL', _('Is all content')),
    )

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name=_('Chapter'))
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'), max_length=255, default='slug')
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)
    last_update = models.DateTimeField(verbose_name=_('Last update'), auto_now=True)

    # settings
    content_type = models.CharField(verbose_name=_('Content type'), choices=CONTENT_TYPE, default=CONTENT_TYPE[0][1])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Content')
        verbose_name_plural = _('Contents')
        ordering = ('-index', )


class TextContent(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name=_('Content'))
    description = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return self.content.title

    class Meta:
        verbose_name = _('Text content')
        verbose_name_plural = _('Text contents')
        ordering = ('-index', )


class FileContent(models.Model):
    def file_path(self):
        return '/category/{}/{}/{}'.format(self.content.chapter.topic, self.content.chapter, self.content)

    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name=_('Content'))
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    file = models.FileField(verbose_name=_('File'), upload_to=file_path)
    index = models.PositiveSmallIntegerField(verbose_name=_('Priority'), default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('File content')
        verbose_name_plural = _('File contents')
        ordering = ('-index',)
