# Generated by Django 5.0.6 on 2025-01-22 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0052_division_image_division_poster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='div_type',
            field=models.CharField(choices=[('div', 'Division/Center division'), ('department', 'Department division'), ('management', 'Management division')], default='div', verbose_name='Division type'),
        ),
    ]
