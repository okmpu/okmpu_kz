# Generated by Django 5.0.6 on 2024-07-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='departments',
            field=models.ManyToManyField(blank=True, related_name='programs', to='university.department', verbose_name='Departments'),
        ),
    ]