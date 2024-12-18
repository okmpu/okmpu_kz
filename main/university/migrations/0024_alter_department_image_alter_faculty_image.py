# Generated by Django 5.0.6 on 2024-11-05 06:55

import main.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0023_alter_department_image_alter_department_poster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='university/faculties/avatars', validators=[main.validators.validate_logo], verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='university/faculties/avatars', validators=[main.validators.validate_logo], verbose_name='Image'),
        ),
    ]
