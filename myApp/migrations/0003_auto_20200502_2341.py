# Generated by Django 3.0.5 on 2020-05-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_auto_20200430_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='Image',
            field=models.ImageField(default=None, upload_to='post_images'),
        ),
    ]
