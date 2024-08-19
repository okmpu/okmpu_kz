# Generated by Django 5.0.6 on 2024-08-12 09:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_personal_department_specialty_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('file', models.FileField(blank=True, null=True, upload_to='university/projects/files/', verbose_name='File')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='university.department', verbose_name='Department')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]