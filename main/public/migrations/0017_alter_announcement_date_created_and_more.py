# Generated by Django 5.0.6 on 2024-10-04 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0016_announcement_faculty_event_faculty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_created',
            field=models.DateTimeField(verbose_name='Date created'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_created',
            field=models.DateTimeField(verbose_name='Date created'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date_created',
            field=models.DateTimeField(verbose_name='Date created'),
        ),
    ]
