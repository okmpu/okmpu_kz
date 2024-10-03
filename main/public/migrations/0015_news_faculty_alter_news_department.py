# Generated by Django 5.0.6 on 2024-10-03 04:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0014_alter_program_options_program_order'),
        ('university', '0018_alter_facultyprogram_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faculty_news', to='university.faculty', verbose_name='Faculty'),
        ),
        migrations.AlterField(
            model_name='news',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_news', to='university.department', verbose_name='Department'),
        ),
    ]
