# Generated by Django 4.1.7 on 2023-04-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_alter_document_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='version',
            field=models.PositiveIntegerField(),
        ),
    ]
