# Generated by Django 5.0.6 on 2024-08-02 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0003_remove_announcement_poster_event'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
    ]