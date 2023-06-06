# Generated by Django 4.1.7 on 2023-04-03 07:50

import blog.storages
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_alter_document_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(storage=blog.storages.MediaStorage(), upload_to='media/'),
        ),
    ]
