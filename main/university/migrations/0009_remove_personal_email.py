# Generated by Django 5.0.6 on 2024-08-12 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0008_personal_email_alter_personal_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='email',
        ),
    ]