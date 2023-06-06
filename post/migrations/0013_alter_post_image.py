# Generated by Django 4.1.7 on 2023-03-24 09:34

import blog.storages
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, storage=blog.storages.MediaStorage(), upload_to=''),
        ),
    ]