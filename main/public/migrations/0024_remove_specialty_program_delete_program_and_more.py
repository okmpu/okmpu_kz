# Generated by Django 5.0.6 on 2025-02-04 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0023_alter_specialty_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialty',
            name='program',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.DeleteModel(
            name='Specialty',
        ),
    ]
