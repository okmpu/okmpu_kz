from django.core.exceptions import ValidationError


def validate_file_size(value):
    file_size = value.size

    max_size_mb = 5

    if file_size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла {max_size_mb}MB")
