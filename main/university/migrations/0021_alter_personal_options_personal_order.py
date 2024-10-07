# Generated by Django 5.0.6 on 2024-10-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0020_success_description_en_success_description_kk_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personal',
            options={'ordering': ('order',), 'verbose_name': 'Personal', 'verbose_name_plural': 'Personals'},
        ),
        migrations.AddField(
            model_name='personal',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Order'),
        ),
    ]