# Generated by Django 2.1 on 2018-09-30 18:42

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180930_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
