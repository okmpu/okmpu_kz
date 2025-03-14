# Generated by Django 5.0.6 on 2024-12-17 10:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0049_material_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_materials', to='university.personal', verbose_name='Author'),
        ),
    ]
