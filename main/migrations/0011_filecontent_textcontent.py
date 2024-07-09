# Generated by Django 5.0.6 on 2024-07-04 07:49

import django.db.models.deletion
import main.models.generics
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255, verbose_name='Title')),
                ('file', models.FileField(upload_to=main.models.generics.FileContent.file_path, verbose_name='File')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='Priority')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.content', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Text content',
                'verbose_name_plural': 'Text contents',
                'ordering': ('-index',),
            },
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('index', models.PositiveSmallIntegerField(default=0, verbose_name='Priority')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.content', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Text content',
                'verbose_name_plural': 'Text contents',
                'ordering': ('-index',),
            },
        ),
    ]
