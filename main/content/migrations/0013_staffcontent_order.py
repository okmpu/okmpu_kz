# Generated by Django 5.0.6 on 2024-08-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_alter_staffcontent_email_alter_staffcontent_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffcontent',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Order'),
        ),
    ]
