# Generated by Django 5.0.6 on 2024-12-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0044_alter_personal_p_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='p_type',
            field=models.CharField(choices=[('Faculty', [('deans_office', "Dean's office"), ('department_manage', 'Department management'), ('teacher', 'Teacher'), ('student', 'Student')]), ('Division', [('employee', 'Employee')])], default='student', max_length=128, verbose_name='Personal type'),
        ),
    ]