# Generated by Django 5.0.6 on 2024-07-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_category_name_en_category_name_kk_category_name_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='index',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Priority'),
        ),
    ]
