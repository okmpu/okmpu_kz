# Generated by Django 5.0.6 on 2024-09-24 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0017_facultyprogram_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facultyprogram',
            options={'ordering': ('order',), 'verbose_name': 'Program', 'verbose_name_plural': 'Programs'},
        ),
    ]
