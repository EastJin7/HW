# Generated by Django 3.2.5 on 2022-03-25 22:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_alter_photo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
