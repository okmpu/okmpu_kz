# Generated by Django 5.0.6 on 2025-06-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_remove_document_docs_grid_alter_division_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='public',
            name='public_type',
            field=models.CharField(choices=[('news', 'News'), ('ann', 'Announcement')], default='news', max_length=24, verbose_name='Public type'),
        ),
    ]
