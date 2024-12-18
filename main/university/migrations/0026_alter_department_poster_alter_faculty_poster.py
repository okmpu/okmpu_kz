# Generated by Django 5.0.6 on 2024-11-05 07:06

import main.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0025_alter_personal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='university/faculties/posters', validators=[main.validators.validate_poster], verbose_name='Poster'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='university/faculties/posters', validators=[main.validators.validate_poster], verbose_name='Poster'),
        ),
    ]
