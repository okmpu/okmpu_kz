# Generated by Django 5.0.6 on 2024-07-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_filecontent_textcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='title_kk',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='content',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
    ]
