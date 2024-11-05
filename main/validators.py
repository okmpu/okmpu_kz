from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image


def validate_file_size(value):
    file_size = value.size

    max_size_mb = 5

    if file_size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {max_size_mb}MB")


# university > faculty | department logo
def validate_logo(image):
    max_size = 1 * 1024 * 1024
    if image.size > max_size:
        raise ValidationError(_('Размер изображения не должен превышать 1MB.'))

    try:
        img = Image.open(image)
        width, height = img.size
        max_resolution = 1024

        if width != height:
            raise ValidationError(_('Изображение должно быть квадратным.'))

        if width > max_resolution or height > max_resolution:
            raise ValidationError(_('Максимальное разрешение изображения: 1024x1024 пикселей.'))

    except Exception as e:
        raise ValidationError(
            _('Не удалось обработать изображение. Убедитесь, что файл является корректным изображением.'))


def validate_poster(image):
    max_size = 2 * 1024 * 1024  # 2MB
    if image.size > max_size:
        raise ValidationError(_('Размер изображения не должен превышать 2MB.'))

    try:
        img = Image.open(image)
        width, height = img.size
        min_width, min_height = 1280, 720

        if width < min_width or height < min_height:
            raise ValidationError(_('Минимальное разрешение изображения: 1280x720 пикселей.'))

        if width <= height:
            raise ValidationError(_('Изображение должно быть в альбомной ориентации (ширина больше высоты).'))

    except Exception:
        raise ValidationError(
            _('Не удалось обработать изображение. Убедитесь, что файл является корректным изображением.'))
