# Generated by Django 5.0.6 on 2024-11-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0033_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='division',
            name='about_en',
            field=models.TextField(blank=True, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='division',
            name='about_kk',
            field=models.TextField(blank=True, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='division',
            name='about_ru',
            field=models.TextField(blank=True, null=True, verbose_name='About'),
        ),
        migrations.AddField(
            model_name='division',
            name='name_en',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='division',
            name='name_kk',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='division',
            name='name_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='Name'),
        ),
    ]