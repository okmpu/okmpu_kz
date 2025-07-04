# Generated by Django 5.0.6 on 2025-06-24 05:23

import django.db.models.deletion
import register.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_alter_headliner_poster_alter_partner_poster_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('name_kk', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, verbose_name='Slug')),
                ('app_name', models.CharField(choices=[('none', 'None'), ('content', 'Content app'), ('university', 'University app')], default='none', verbose_name='App name')),
                ('multiple', models.BooleanField(default=False, verbose_name='Multiple')),
                ('url', models.CharField(blank=True, max_length=128, null=True, verbose_name='URL')),
                ('target', models.BooleanField(default=False, verbose_name='Target')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='register.category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_kk', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_kk', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last update')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='register.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Contents',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='FileContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=360, verbose_name='Caption')),
                ('caption_kk', models.CharField(max_length=360, null=True, verbose_name='Caption')),
                ('caption_ru', models.CharField(max_length=360, null=True, verbose_name='Caption')),
                ('caption_en', models.CharField(max_length=360, null=True, verbose_name='Caption')),
                ('source_file', models.FileField(blank=True, null=True, upload_to='register/content/category/files/', verbose_name='Source file')),
                ('source_file_kk', models.FileField(blank=True, null=True, upload_to='register/content/category/files/', verbose_name='Source file')),
                ('source_file_ru', models.FileField(blank=True, null=True, upload_to='register/content/category/files/', verbose_name='Source file')),
                ('source_file_en', models.FileField(blank=True, null=True, upload_to='register/content/category/files/', verbose_name='Source file')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_contents', to='register.content', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'File content',
                'verbose_name_plural': 'File contents',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='ImageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='register/content/category/images/', verbose_name='Image')),
                ('image_kk', models.ImageField(null=True, upload_to='register/content/category/images/', verbose_name='Image')),
                ('image_ru', models.ImageField(null=True, upload_to='register/content/category/images/', verbose_name='Image')),
                ('image_en', models.ImageField(null=True, upload_to='register/content/category/images/', verbose_name='Image')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_contents', to='register.content', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Image content',
                'verbose_name_plural': 'Image contents',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='StaffContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128, verbose_name='Full name')),
                ('full_name_kk', models.CharField(max_length=128, null=True, verbose_name='Full name')),
                ('full_name_ru', models.CharField(max_length=128, null=True, verbose_name='Full name')),
                ('full_name_en', models.CharField(max_length=128, null=True, verbose_name='Full name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='register/content/category/staff/', validators=[register.validators.validate_logo], verbose_name='Image')),
                ('profession', models.CharField(max_length=128, verbose_name='Profession')),
                ('profession_kk', models.CharField(max_length=128, null=True, verbose_name='Profession')),
                ('profession_ru', models.CharField(max_length=128, null=True, verbose_name='Profession')),
                ('profession_en', models.CharField(max_length=128, null=True, verbose_name='Profession')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('bio_kk', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('bio_ru', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('bio_en', models.TextField(blank=True, null=True, verbose_name='Bio')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=64, null=True, verbose_name='Email')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_contents', to='register.content', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Staff content',
                'verbose_name_plural': 'Staff contents',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('body_kk', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('body_ru', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('body_en', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_contents', to='register.content', verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Text content',
                'verbose_name_plural': 'Text contents',
                'ordering': ('order',),
            },
        ),
    ]
