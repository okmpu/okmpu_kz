# Generated by Django 5.0.6 on 2024-07-31 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headliner',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Order'),
        ),
    ]