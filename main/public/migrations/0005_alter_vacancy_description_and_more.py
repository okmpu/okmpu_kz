# Generated by Django 5.0.6 on 2024-08-05 03:48

import django_summernote.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_alter_event_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=django_summernote.fields.SummernoteTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description_en',
            field=django_summernote.fields.SummernoteTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description_kk',
            field=django_summernote.fields.SummernoteTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description_ru',
            field=django_summernote.fields.SummernoteTextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]