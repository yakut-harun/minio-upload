# Generated by Django 4.1.7 on 2023-03-30 11:52

import blog.storages
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0014_file_fileversion_remove_post_user_delete_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Ad Soyad')),
                ('content', models.TextField(verbose_name='Yorum')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('content', ckeditor.fields.RichTextField(verbose_name='İçerik')),
                ('publishing_date', models.DateTimeField(auto_now_add=True, verbose_name='Yayımlanma Tarihi')),
                ('image', models.FileField(blank=True, null=True, storage=blog.storages.MediaStorage(), upload_to='')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publishing_date', 'id'],
            },
        ),
        migrations.RemoveField(
            model_name='fileversion',
            name='file',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='FileVersion',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.post'),
        ),
    ]
