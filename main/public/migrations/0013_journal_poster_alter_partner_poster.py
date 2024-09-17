# Generated by Django 5.0.6 on 2024-09-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0012_journal_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='public/journals/', verbose_name='Poster'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='public/partners/', verbose_name='Poster'),
        ),
    ]
