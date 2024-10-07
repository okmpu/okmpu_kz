# Generated by Django 5.0.6 on 2024-10-03 04:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0015_news_faculty_alter_news_department'),
        ('university', '0018_alter_facultyprogram_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faculty_announcements', to='university.faculty', verbose_name='Faculty'),
        ),
        migrations.AddField(
            model_name='event',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faculty_events', to='university.faculty', verbose_name='Faculty'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_announcements', to='university.department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='event',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_events', to='university.department', verbose_name='Department'),
        ),
    ]